import psycopg2

from app.config import database_credentials

def get_connection():
    conn = psycopg2.connect(
        host="localhost", 
        database=database_credentials["dbname"], 
        user=database_credentials["username"]
    )
    return conn


conn = get_connection()
