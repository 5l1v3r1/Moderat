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