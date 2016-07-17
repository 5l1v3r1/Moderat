import os
import sqlite3
import hashlib


class ModeratorsManagment:

    def __init__(self):

        print '[+] Initializing Database'
        self.conn = sqlite3.connect('Moderators.db')
        self.cur = self.conn.cursor()

        check_table = self.cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Moderators"')
        self.conn.commit()
        if len(check_table.fetchall()) == 0:
            print '[+] Creating Table'
            self.create_table()

    def create_table(self):
        self.cur.execute('CREATE TABLE Moderators (moderator_id VARCHAR(100), moderator_password VARCHAR(100))')
        self.conn.commit()

    def create_user(self, moderator_id, moderator_password):
        password_hash = hashlib.md5()
        password_hash.update(moderator_password)
        check_moderators = self.cur.execute('SELECT * FROM Moderators WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        if len(check_moderators.fetchall()) == 0:
            self.cur.execute('INSERT INTO Moderators VALUES (?,?)', (moderator_id, password_hash.hexdigest()))
            self.conn.commit()
            return True
        else:
            return False

    def check_user(self, moderator_id, moderator_password):
        pass

    def delete_user(self):
        pass


a = ModeratorsManagment()
a.create_user('administrator2', '5297a52972')