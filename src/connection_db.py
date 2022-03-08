import psycopg2

import json

# buka file JSON
file_json = open("config/config.json")

# parsing data JSON
database = json.loads(file_json.read())

# ==============================
#       Connect to DB
# ==============================


def connect_db():
    db_conn = psycopg2.connect(f"dbname={database['db_name']} user={database['user']} password={database['pass']} host={database['host']} port={database['port']}")
    cursor = db_conn.cursor()
    return db_conn, cursor

# ==============================
#       Close DB
# ==============================


def closeDB(db_conn, cursor):
    cursor.close()
    db_conn.close()