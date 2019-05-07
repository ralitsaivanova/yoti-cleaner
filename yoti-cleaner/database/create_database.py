import psycopg2

from app.config import database_credentials

if __name__ == '__main__':

    conn = psycopg2.connect(
        host="localhost",
        user=database_credentials["username"])
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE DATABASE cleaning")
    except psycopg2.errors.DuplicateDatabase:
        pass

    conn.close()

    conn = psycopg2.connect(
        host=database_credentials["host"],
        database=database_credentials["dbname"],
        user=database_credentials["username"])

    cursor = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS cleaning_session(
            session_id serial PRIMARY KEY,
            room_width integer NOT NULL,
            room_length integer NOT NULL,
            starting_x integer NOT NULL,
            starting_y integer NOT NULL,
            final_x integer NOT NULL,
            final_y integer NOT NULL,
            dirty_patches VARCHAR NOT NULL,
            num_patches_cleaned integer NOT NULL,
            instructions VARCHAR NOT NULL
        );
        """
    cursor.execute(create_table)
    conn.commit()
    conn.close()
