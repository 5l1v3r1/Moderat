from PIL import Image

import zlib


def save_image(screen_info):
    print zlib.decompress(screen_info['screen_bits'])
    image = Image.frombuffer('RGB', (screen_info['width'], screen_info['height']), zlib.decompress(screen_info['screen_bits']), 'raw', 'BGRX', 0, 1)
    screen_bits = image.convert('RGBA')
    screen_bits.save('%s.png' % screen_info['date'], 'png')
