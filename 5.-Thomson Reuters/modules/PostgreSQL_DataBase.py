# -*- coding: utf-8 -*-

import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname='c1_AI_ChatHistory',
            user='postgres',
            password='Diego1234',
            host='127.0.0.1',
            port='5432'
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_tables():
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS chat_sessions (
                    id SERIAL PRIMARY KEY,
                    session_id VARCHAR(255) UNIQUE NOT NULL
                );
                CREATE TABLE IF NOT EXISTS chat_messages (
                    id SERIAL PRIMARY KEY,
                    session_id VARCHAR(255) NOT NULL,
                    role VARCHAR(50) NOT NULL,
                    content TEXT NOT NULL,
                    FOREIGN KEY (session_id) REFERENCES chat_sessions(session_id) ON DELETE CASCADE
                );
                """)
                conn.commit()
        except Exception as e:
            print(f"Error creating tables: {e}")
        finally:
            conn.close()

create_tables()