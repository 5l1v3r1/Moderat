import os
import sqlite3
import datetime


class ClientsManagment:

    def __init__(self):

        print '[+] Initializing Clients Database'
        self.conn = sqlite3.connect('Moderators.db')
        self.cur = self.conn.cursor()

        check_table = self.cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Clients"')
        self.conn.commit()
        if len(check_table.fetchall()) == 0:
            print '[+] Creating Table Clients'
            self.create_clients_table()

    def create_clients_table(self):
        self.cur.execute('''CREATE TABLE Clients (
                          moderator_id VARCHAR(100),
                          client_id VARCHAR(100),
                          client_alias VARCHAR(100),
                          client_ip VARCHAR(100),
                          last_connected DATETIME(100))''')
        self.conn.commit()

    def create_client(self, moderator_id, client_id, client_ip):
        check_moderators = self.cur.execute('SELECT * FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()
        if len(check_moderators.fetchall()) == 0:
            self.cur.execute('INSERT INTO Clients VALUES (?,?,?,?,?)', (moderator_id, client_id, '', client_ip, datetime.datetime.now()))
            self.conn.commit()
            return True
        else:
            return False

    def get_clients(self, moderator_id):
        clients = self.cur.execute('SELECT client_id FROM Clients WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        return clients.fetchall()


    # TODO:
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