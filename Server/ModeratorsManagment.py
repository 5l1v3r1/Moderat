import os
import sqlite3
import hashlib
import datetime


class ModeratorsManagment:

    def __init__(self):

        self.conn = sqlite3.connect('Moderators.db')
        self.cur = self.conn.cursor()

        check_table = self.cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Moderators"')
        self.conn.commit()
        if len(check_table.fetchall()) == 0:
            print '[+] Creating Table Moderators'
            self.create_moderators_table()

    def create_moderators_table(self):
        self.cur.execute('''CREATE TABLE Moderators (
                                moderator_id VARCHAR(100),
                                 moderator_password VARCHAR(100),
                                 moderator_privs INTEGER(10),
                                 moderator_status INTEGER DEFAULT 0,
                                 moderator_last_online DATETIME(100))''')
        self.conn.commit()

    def create_user(self, moderator_id, moderator_password, moderator_privs):
        password_hash = hashlib.md5()
        password_hash.update(moderator_password)
        check_moderators = self.cur.execute('SELECT * FROM Moderators WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        if len(check_moderators.fetchall()) == 0:
            self.cur.execute('INSERT INTO Moderators VALUES (?,?,?,?,?)', (moderator_id, password_hash.hexdigest(), moderator_privs, 0, datetime.datetime.now()))
            self.conn.commit()
            return True
        else:
            return False

    def login_user(self, moderator_id, moderator_password):
        check_user = self.cur.execute('SELECT * FROM Moderators WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        if len(check_user.fetchall()) == 0:
            return False
        else:
            password_hash = hashlib.md5()
            password_hash.update(moderator_password)
            db_password_hash = self.cur.execute('SELECT moderator_password FROM Moderators WHERE moderator_id=?', (moderator_id,))
            self.conn.commit()
            if db_password_hash.fetchone()[0] == password_hash.hexdigest():
                return True
            else:
                return False

    def change_password(self, moderator_id, new_password):
        check_user = self.cur.execute('SELECT * FROM Moderators WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        if len(check_user.fetchall()) == 0:
            return False
        else:
            generate_hash = hashlib.md5()
            generate_hash.update(new_password)
            self.cur.execute('UPDATE Moderators SET moderator_password=? WHERE moderator_id=?', (generate_hash.hexdigest(), moderator_id))
            self.conn.commit()
            return True

    def delete_user(self, moderator_id):
        check_moderator_id = self.cur.execute('SELECT * FROM Moderators WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        if len(check_moderator_id.fetchall()) == 0:
            return False
        else:
            self.cur.execute('DELETE FROM Moderators WHERE moderator_id=?', (moderator_id,))
            self.conn.commit()
            return True

    def get_privs(self, moderator_id):
        check_moderator_id = self.cur.execute('SELECT * FROM Moderators WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        if len(check_moderator_id.fetchall()) == 0:
            return False
        else:
            priv = self.cur.execute('SELECT moderator_privs FROM Moderators WHERE moderator_id=?', (moderator_id,))
            self.conn.commit()
            return priv.fetchone()[0]

    def set_last_online(self, moderator_id, date):
        self.cur.execute('UPDATE Moderators SET moderator_last_online=? WHERE moderator_id=?', (date, moderator_id))
        self.conn.commit()


    def set_status(self, moderator_id, status):
        self.cur.execute('UPDATE Moderators SET moderator_status=? WHERE moderator_id=?', (status, moderator_id))
        self.conn.commit()

    def get_moderators(self):
        moderators = self.cur.execute('SELECT * FROM Moderators')
        self.conn.commit()
        return moderators.fetchall()


ModeratorsManagment().create_user('admin', '1234', 1)
ModeratorsManagment().create_user('user', '1234', 0)

