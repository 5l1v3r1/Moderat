import sqlite3

class KeyloggerManager:

    def __init__(self):

        self.conn = sqlite3.connect('ModeratServer.db')
        self.cur = self.conn.cursor()

        check_table = self.cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Keylogger"')
        self.conn.commit()
        if len(check_table.fetchall()) == 0:
            print '[+] Creating Table Keylogger'
            self.create_keylogger_table()

    def create_keylogger_table(self):
        self.cur.execute('''CREATE TABLE Keylogger (
                                keylogger_client_id VARCHAR(100),
                                 keylogger_datetime VARCHAR(100),
                                 keylogger_date VARCHAR(1000),
                                 keylogger_html_path VARCHAR(1000),
                                 keylogger_status VARCHAR(100))''')
        self.conn.commit()

    def save_keylog(self, client_id, datetime, html_path):
        self.cur.execute('INSERT INTO Keylogger VALUES (?,?,?,?,?)', (client_id, datetime, datetime.split('_')[0], html_path, 0))
        self.conn.commit()

    def get_keylogs_count_0(self, client_id, date):
        keylogs = self.cur.execute('SELECT COUNT(*) FROM Keylogger WHERE keylogger_client_id=? AND keylogger_date=? AND keylogger_status=0', (client_id, date))
        self.conn.commit()
        return keylogs.fetchone()[0]

    def get_keylogs_count_1(self, client_id, date):
        keylogs = self.cur.execute('SELECT COUNT(*) FROM Keylogger WHERE keylogger_client_id=? AND keylogger_date=? AND keylogger_status=1', (client_id, date))
        self.conn.commit()
        return keylogs.fetchone()[0]