from PIL import Image


def save_image(screen_info):
    image = Image.frombuffer('RGB', (screen_info['width'], screen_info['height']), screen_info['screen_bits'], 'raw', 'BGRX', 0, 1)
    screen_bits = image.convert('RGBA')
    screen_bits.save('%s.png' % screen_info['date'], 'png')
