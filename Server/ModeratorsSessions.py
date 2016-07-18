import os
import sqlite3
import datetime


class SessionsManagment:

    def __init__(self):

        print '[+] Initializing Sessions Database'
        self.conn = sqlite3.connect('Moderators.db')
        self.cur = self.conn.cursor()

        check_table = self.cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Sessions"')
        self.conn.commit()
        if len(check_table.fetchall()) == 0:
            print '[+] Creating Table Sessions'
            self.create_sessions_table()

    def create_sessions_table(self):
        self.cur.execute('CREATE TABLE Sessions (moderator_id VARCHAR(100), session_id VARCHAR(100))')
        self.conn.commit()

    def create_session(self, moderator_id, session_id):
        check_session = self.cur.execute('SELECT * FROM Sessions WHERE moderator_id=?', (moderator_id,))
        self.conn.commit()
        if len(check_session.fetchall()) == 0:
            self.cur.execute('INSERT INTO Sessions VALUES (?,?)', (moderator_id, session_id))
            self.conn.commit()
        else:
            self.cur.execute('UPDATE Sessions SET session_id=? WHERE moderator_id=?', (session_id, moderator_id))
            self.conn.commit()

    def get_session(self, session_id):
        print session_id
        username = self.cur.execute('SELECT moderator_id FROM Sessions WHERE session_id=?', (session_id,))
        self.conn.commit()
        return username.fetchone()[0]