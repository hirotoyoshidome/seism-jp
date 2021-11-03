from flask import Flask, render_template
from typing import Any
from .db import connect_db, close_connect_db
import json


app = Flask(__name__)


@app.route("/")
def index() -> Any:
    conn, cur = connect_db()
    sql = """
    SELECT *
    FROM jma;
    """
    cur.execute(sql, ())
    result = cur.fetchall()
    close_connect_db(conn, cur)

    seism_data_list = []
    for r in result:
        seism_data_list.append(
            [r["lng"], r["lat"], r["date_time"], r["depth"], r["area"], r["magnitude"]]
        )

    data = {
        "seism_data_list": json.dumps({"data": seism_data_list}),
    }
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
