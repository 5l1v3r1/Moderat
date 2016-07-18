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
        self.cur.execute('CREATE TABLE Moderators (moderator_id VARCHAR(100), moderator_password VARCHAR(100), moderator_privs INTEGER(10))')
        self.conn.commit()

    def create_user(self, moderator_id, moderator_password, moderator_privs):
        password_hash = hashlib.md5()
        password_hash.update(moderator_password)
        check_moderators = self.cur.execute('SELECT * FROM Moderators WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        if len(check_moderators.fetchall()) == 0:
            self.cur.execute('INSERT INTO Moderators VALUES (?,?,?)', (moderator_id, password_hash.hexdigest(), moderator_privs))
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
            priv = self.cur.executeself.cur.execute('SELECT moderator_privs FROM Moderators WHERE moderator_id=?', (moderator_id,))
            self.conn.commit()
            return priv.fetchone()[0]