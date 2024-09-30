import sqlite3


def connect_to_db(db_name="data.db"):
    return sqlite3.connect(db_name)
