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