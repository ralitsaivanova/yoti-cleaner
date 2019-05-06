import os
import psycopg2

from app.config import database

if __name__ == '__main__':

    conn = psycopg2.connect(user=database["username"])
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE DATABASE cleaning")
    except psycopg2.errors.DuplicateDatabase:
        pass

    create_table = """CREATE TABLE IF NOT EXISTS cleaning_session(
            session_id serial PRIMARY KEY,
            room_size json NOT NULL,
            starting_position json NOT NULL,
            final_position json NOT NULL,
            dirty_patches json NOT NULL,
            num_patches_cleaned integer NOT NULL,
            instructions VARCHAR NOT NULL
        )
        """

    cursor.execute(create_table)
