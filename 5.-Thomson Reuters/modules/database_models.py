# -*- coding: utf-8 -*-

import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseModels:
    def __init__(self, dbname, user, password, host = '127.0.0.1', port = '5432'):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory = RealDictCursor)
        self._create_tables()

    def _create_tables(self):
        chat_session_table = """
        CREATE TABLE IF NOT EXISTS chat_sessions (
            id SERIAL PRIMARY KEY
        );
        """
        message_table = """
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT,
            role VARCHAR(10),  -- 'user' o 'assistant'
            chat_session_id INTEGER REFERENCES chat_sessions(id)
        );
        """
        self.cursor.execute(chat_session_table)
        self.cursor.execute(message_table)

    def create_chat_session(self):
        self.cursor.execute("INSERT INTO chat_sessions DEFAULT VALUES RETURNING id;")
        return self.cursor.fetchone()['id']

    def add_message(self, content, role, chat_session_id):
        self.cursor.execute("""
        INSERT INTO messages (content, role, chat_session_id)
        VALUES (%s, %s, %s) RETURNING id;
        """, (content, role, chat_session_id))
        return self.cursor.fetchone()['id']

    def get_chat_history(self, chat_session_id):
        self.cursor.execute("""
        SELECT content, role FROM messages WHERE chat_session_id = %s ORDER BY id;
        """, (chat_session_id,))
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
