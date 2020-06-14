import tator

def get_images(file_path, media_or_state, num_images=None, width=None, height=None):
    """ Loads image saved by :meth:`tator.TatorApi.get_frame` or 
        :meth:`tator.TatorApi.get_state_graphic` into a list of
        :class:`PIL.Image.Image`.

    :param file_path: Path to image file.
    :param media_or_state: :class:`tator.Media` or :class:`tator.State` object.
    :param num_images: [Optional] The number of images to unwrap if this
        is an image saved by :meth:`tator.TatorApi.get_frame`.
    :param width: [Optional] Width of ROI if this is an image saved by 
        :meth:`tator.TatorApi.get_frame`.
    :param height: [Optional] Height of ROI if this is an image saved by 
        :meth:`tator.TatorApi.get_frame`.
    """
    try:
        from PIL import Image
    except:
        raise RuntimeError("Utility get_images requires pillow to be installed: `pip install pillow`")
    # Read in raw image.
    img = Image.open(file_path)

    # Get tile width/height.
    if isinstance(media_or_state, tator.State):
        num_localizations = len(media_or_state.localizations)
        width = int(img.width / num_localizations)
        height = img.height
    elif isinstance(media_or_state, tator.Media):
        if width is None:
            width = media_or_state.width
        if height is None:
            height = media_or_state.height
    
    # Make list of crops.
    images = []
    for top in range(0, img.height, height):
        for left in range(0, img.width, width):
            image = img.crop((left, top, left+width, top+height))
            images.append(image)
    if num_images:
        images = images[:num_images]
    return images
