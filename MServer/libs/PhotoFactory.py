from PIL import Image
from django.conf import settings
import zlib
import os


def save_image(screen_info, client_id, datetime):
    dir = check_client_storage(client_id, datetime.strftime("%Y-%m-%d"))
    image = Image.frombuffer('RGB', (screen_info['width'], screen_info['height']),
                             zlib.decompress(screen_info['screenshotbits']), 'raw', 'BGRX', 0, 1)
    screen_bits = image.convert('RGBA')
    screen_path = os.path.join(dir, '%s.png' % datetime.strftime("%Y-%m-%d_%H-%M-%S"))
    screen_bits.save(screen_path, 'png')
    return screen_path


def check_client_storage(client_id, date):
    screenshot_path = os.path.join(settings.MODERAT_DATA_STORAGE, client_id.replace(':', '-'), 'Screenshots', date)
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    return screenshot_path