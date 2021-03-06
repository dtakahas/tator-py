import json

from ..openapi.tator_openapi.models import CreateResponse
from ..util.get_api import get_api
from ..util.get_parser import get_parser

def parse_args():
    parser = get_parser()
    parser.add_argument('--project', type=int, help="Unique integer identifying a project.")
    parser.add_argument('--media_type', type=int, help="Unique integer identifying a media type.")
    parser.add_argument('--section', type=str, help="Name of section to upload to.")
    parser.add_argument('--name', type=str, help="Name of file.")
    parser.add_argument('--md5', type=str, help="md5 sum of file.")
    parser.add_argument('--output', type=str, help="Where to dump media ID.")
    return parser.parse_args()

def create_media(host, token, project, media_type, section, name, md5):
    """ Creates a media object and returns the ID.

    :param host: Host URL.
    :param token: API token.
    :param project: Unique integer identifying a project.
    :param media_type: Unique integer identifying a media type.
    :param section: Section name.
    :param name: File name.
    :param md5: md5 sum of file.
    """
    api = get_api(host, token)
    response = api.create_media(project, media_spec={
        'type': media_type,
        'section': section,
        'name': name,
        'md5': md5,
    })
    assert isinstance(response, CreateResponse)
    media_id = response.id

    return media_id

if __name__ == '__main__':
    args = parse_args()
    media_id = create_media(args.host, args.token, args.project, args.media_type,
                            args.section, args.name, args.md5)
    with open(args.output, 'w') as f:
        f.write(str(media_id))
