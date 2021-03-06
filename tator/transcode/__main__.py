#!/usr/bin/env python

import argparse
import os
from uuid import uuid1
import logging

from progressbar import progressbar

from ..util import md5sum

from .create_media import create_media
from .determine_transcode import determine_transcode
from .transcode import convert_streaming
from .transcode import convert_archival
from .transcode import convert_audio
from .make_thumbnails import make_thumbnails
from .upload_transcoded_video import upload_transcoded_video

logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description='Full transcode pipeline on a directory of files.')
    parser.add_argument('path', type=str, help='Path to directory containing video files, or a video file.')
    parser.add_argument('--extension', type=str, default='mp4', help='File extension to upload. '
                                                                     'Ignored if path is a file.')
    parser.add_argument('--host', type=str, default='https://www.tatorapp.com', help='Host URL.')
    parser.add_argument('--token', type=str, help='REST API token.')
    parser.add_argument('--project', type=int, help='Unique integer specifying project ID.')
    parser.add_argument('--type', type=int, help='Unique integer specifying a media type.')
    parser.add_argument('--section', type=str, help='Media section name.')
    return parser.parse_args()

def get_file_paths(path):
    base, _ = os.path.splitext(path)
    paths = {
        'original': path,
        'transcoded': base + '_transcoded',
        'thumbnail': base + '_thumbnail.jpg',
        'thumbnail_gif': base + '_thumbnail_gif.gif',
        'segments': base + '_segments.json',
    }
    return paths

def transcode_single(path, args, gid):
    """Transcodes a single file.
    """
    paths = get_file_paths(path)

    # Get md5 for the file.
    md5 = md5sum(paths['original'])

    # Get base filename.
    name = os.path.basename(paths['original'])

    # Create the media object.
    media_id = create_media(args.host, args.token, args.project, args.type, args.section, name, md5)

    # Make thumbnails.
    make_thumbnails(args.host, args.token, media_id, paths['original'], paths['thumbnail'],
                    paths['thumbnail_gif'])

    # Determine transcodes that need to be done.
    workloads = determine_transcode(args.host, args.token, args.type, path, group_to=1080)

    # Transcode the video file.
    for workload in workloads:
        category = workload['category']
        del workload['category']
        if category == 'streaming':
            convert_streaming(**workload, host=args.host, token=args.token, media=media_id,
                              outpath=paths['transcoded'], gid=gid, uid=str(uuid1()))
        elif category == 'archival':
            del workload['resolutions']
            convert_archival(**workload, host=args.host, token=args.token, media=media_id,
                             outpath=paths['transcoded'])
        elif category == 'audio':
            del workload['resolutions']
            del workload['raw_width']
            del workload['raw_height']
            convert_audio(**workload, host=args.host, token=args.token, media=media_id,
                          outpath=paths['transcoded'])
    
if __name__ == '__main__':
    args = parse_args()
    gid = str(uuid1())
    if os.path.isdir(args.path):
        file_list = []
        for root, dirs, files in os.walk(args.path):
            for fname in files:
                if fname.endswith(args.extension):
                    path = os.path.join(root, fname)
                    file_list.append(path)
        for path in progressbar(file_list):
            transcode_single(path, args, gid)
    else:
        transcode_single(args.path, args, gid)
