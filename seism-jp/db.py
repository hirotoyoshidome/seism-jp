import mysql.connector
from typing import Any


# CONSTS
DB_HOST = "seismjp_mysql"
DB_PORT = 3306
DB_NAME = "seismjp"
DB_USER = "root"
DB_PASSWORD = "root"


def connect_db() -> Any:
    """
    connect db.
    """
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        use_unicode=True,
        # charset="utf8mb4",
    )
    conn.autocommit = True
    if not conn.is_connected():
        conn.close()
        print("Can not connect DB.")
        exit(1)
    cur = conn.cursor(dictionary=True)
    return conn, cur


def close_connect_db(conn: Any, cur: Any) -> None:
    """
    close connection.
    """
    cur.close()
    conn.close()
