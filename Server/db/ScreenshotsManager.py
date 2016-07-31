import sqlite3

class ScreenshotsManager:

    def __init__(self):

        self.conn = sqlite3.connect('ModeratServer.db')
        self.cur = self.conn.cursor()

        check_table = self.cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Screenshots"')
        self.conn.commit()
        if len(check_table.fetchall()) == 0:
            print '[+] Creating Table Screenshots'
            self.create_screenshots_table()

    def create_screenshots_table(self):
        self.cur.execute('''CREATE TABLE Screenshots (
                                screenshot_client_id VARCHAR(100),
                                 screenshot_name VARCHAR(100),
                                 screenshot_path VARCHAR(100),
                                 screenshot_window_title VARCHAR(1000),
                                 screenshot_date VARCHAR(100),
                                 screenshot_status INTEGER)''')
        self.conn.commit()

    def save_image(self, client_id, screenshot_name, screenshot_path, window_title, date):
        self.cur.execute('INSERT INTO Screenshots VALUES (?,?,?,?,?,?)', (client_id, screenshot_name, screenshot_path, window_title, date, 0))
        self.conn.commit()

    def get_screenshots_count_0(self, client_id, date):
        screenshots = self.cur.execute('SELECT COUNT(*) FROM Screenshots WHERE screenshot_client_id=? AND screenshot_date=? AND screenshot_status=0', (client_id, date))
        self.conn.commit()
        return screenshots.fetchone()[0]

    def get_screenshots_count_1(self, client_id, date):
        screenshots = self.cur.execute('SELECT COUNT(*) FROM Screenshots WHERE screenshot_client_id=? AND screenshot_date=? AND screenshot_status=1', (client_id, date))
        self.conn.commit()
        return screenshots.fetchone()[0]

    def get_all_screenshots(self, client_id, date, filter):
        screenshots = self.cur.execute('SELECT * FROM Screenshots WHERE screenshot_client_id=? AND screenshot_date=? AND screenshot_status=?', (client_id, date, filter))
        self.conn.commit()
        return screenshots.fetchone()[0]