from flask import Flask, render_template
from typing import Any
from .db import connect_db, close_connect_db


app = Flask(__name__)


@app.route("/")
def index() -> Any:
    conn, cur = connect_db()
    sql = """
    SELECT *
    FROM jma
    LIMIT 1;
    """
    cur.execute(sql, ())
    jma = cur.fetchone()
    close_connect_db(conn, cur)

    data = {"test": "aaa"}
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
