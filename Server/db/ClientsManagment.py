import os
import sqlite3
import datetime


class ClientsManagment:

    def __init__(self):

        self.conn = sqlite3.connect('ModeratServer.db')
        self.cur = self.conn.cursor()

        check_table = self.cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Clients"')
        self.conn.commit()
        if len(check_table.fetchall()) == 0:
            self.create_clients_table()

    def set_status_zero(self):
        self.cur.execute('UPDATE Clients SET client_status=0')
        self.conn.commit()

    def create_clients_table(self):
        self.cur.execute('''CREATE TABLE Clients (
                          moderator_id VARCHAR(100),
                          client_id VARCHAR(100),
                          client_alias VARCHAR(100),
                          client_ip VARCHAR(100),
                          last_connected DATETIME(100),
                          client_status INTEGER(10))'''),
        self.conn.commit()

    def get_alias(self, client_id):
        alias = self.cur.execute('SELECT client_alias FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()
        return alias.fetchone()[0]

    def get_ip_address(self, client_id):
        alias = self.cur.execute('SELECT client_ip FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()
        return alias.fetchone()[0]

    def get_last_online(self, client_id):
        alias = self.cur.execute('SELECT last_connected FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()
        return alias.fetchone()[0]

    def set_alias(self, client_id, client_alias):
        self.cur.execute('UPDATE Clients SET client_alias=? WHERE client_id=?', (client_alias, client_id))
        self.conn.commit()
        return 'Success'

    def set_moderator(self, client_id, moderator_id):
        self.cur.execute('UPDATE Clients SET moderator_id=? WHERE client_id=?', (moderator_id, client_id))
        self.conn.commit()
        return 'Success'

    def create_client(self, moderator_id, client_id, client_ip):
        check_clients = self.cur.execute('SELECT * FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()
        if len(check_clients.fetchall()) == 0:
            self.cur.execute('INSERT INTO Clients VALUES (?,?,?,?,?,?)', (moderator_id, client_id, '', client_ip, datetime.datetime.now(), 1))
            self.conn.commit()
            return True
        else:
            return False

    def get_clients(self, moderator_id):
        clients = self.cur.execute('SELECT client_id FROM Clients WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        return clients.fetchall()

    # Administrator Query
    def get_all_clients(self):
        clients = self.cur.execute('SELECT client_id FROM Clients')
        self.conn.commit()
        return clients.fetchall()

    def set_client_online(self, client_id):
        self.cur.execute('UPDATE Clients SET client_status=1 WHERE client_id=?', (client_id,))
        self.conn.commit()

    def set_client_offline(self, client_id):
        check_clients = self.cur.execute('SELECT * FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()
        if len(check_clients.fetchall()) != 0:
            self.cur.execute('UPDATE Clients SET client_status=0 WHERE client_id=?', (client_id,))
            self.conn.commit()

    def delete_client(self, client_id):
        self.cur.execute('DELETE FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()

    def is_online(self, client_id):
        client_status = self.cur.execute('SELECT client_status FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()
        status = client_status.fetchall()[0]
        if status == 1:
            return True
        else:
            return False

    def get_offline_clients(self, moderator_id):
        client_status = self.cur.execute('SELECT * FROM Clients WHERE moderator_id=? AND client_status=0', (moderator_id,))
        self.conn.commit()
        status = client_status.fetchall()
        return status

    # Administrator Query
    def get_all_offline_clients(self):
        client_status = self.cur.execute('SELECT * FROM Clients WHERE client_status=0')
        self.conn.commit()
        status = client_status.fetchall()
        return status

    def get_moderator(self, client_id):
        moderator = self.cur.execute('SELECT moderator_id FROM Clients WHERE client_id=?', (client_id,))
        self.conn.commit()
        return moderator.fetchone()[0]