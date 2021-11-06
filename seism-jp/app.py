from flask import Flask, render_template, request
from typing import Any
from .db import connect_db, close_connect_db
import json


app = Flask(__name__)


@app.route("/")
def index() -> Any:
    conn, cur = connect_db()

    datetime_format = "%Y-%m-%d %h:%i:%s"
    datetime_from = "2020-01-01"
    datetime_to = "2020-01-02"
    limit = 5

    sql = """
    SELECT id,
           area,
           lat,
           lng,
           depth,
           magnitude,
           date_time
    FROM jma
    WHERE STR_TO_DATE(date_time, %(fmt)s) BETWEEN %(from)s and %(to)s
    LIMIT %(limit)s;
    """

    g_from = request.args.get("from", None)
    g_to = request.args.get("to", None)
    g_limit = request.args.get("limit", None)

    if g_from is not None:
        datetime_from = g_from
    if g_to is not None:
        datetime_to = g_to
    if g_limit is not None:
        limit = int(g_limit)

    params = {
        "fmt": datetime_format,
        "from": datetime_from,
        "to": datetime_to,
        "limit": limit,
    }
    cur.execute(sql, params)
    result = cur.fetchall()
    close_connect_db(conn, cur)

    seism_data_list = []
    for r in result:
        seism_data_list.append(
            [r["lng"], r["lat"], r["date_time"], r["depth"], r["area"], r["magnitude"]]
        )

    # TODO tmp
    fil = open("batch/output/saitama.geojson", "r")
    geo_data = json.load(fil)

    data = {
        "seism_data_list": json.dumps({"data": seism_data_list}),
        "geo_data": json.dumps(geo_data),
    }
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
