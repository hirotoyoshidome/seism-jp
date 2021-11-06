import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import Any
import csv
import time
import mysql.connector


# convert to csv file from txt.
# and insert db.
# credit :
# https://www.data.jma.go.jp/svd/eqev/data/daily_map/index.html

# CONST
DOWNLOAD_PATH = "./data/"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "seismjp"
DB_USER = "root"
DB_PASSWORD = "root"


# MAIN
def main() -> None:
    conn, cur = connect_db()
    urls = [
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200501.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200502.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200503.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200504.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200505.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200506.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200507.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200508.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200509.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200510.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200511.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200512.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200513.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200514.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200515.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200516.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200517.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200518.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200519.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200520.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200521.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200522.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200523.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200524.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200525.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200526.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200527.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200528.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200529.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200530.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200531.html",
    ]

    for url in urls:
        key = url.split("/")[-1].replace(".html", "")
        # get txt file.
        txt_file_path = get_data_from_web(url, key)
        if txt_file_path is None:
            print("Txt File Download Error.")
            exit(1)

        # convert csv file.
        csv_file_path = convert_csv_from_txt(txt_file_path, key)

        df = pd.read_csv(csv_file_path)

        # Latitude.
        lat_list = df["lat"].apply(lambda x: convert_location(x)).to_numpy()
        # Longitude.
        lng_list = df["lng"].apply(lambda x: convert_location(x)).to_numpy()

        # Convert geodetic datum.
        convd_lat = []
        convd_lng = []
        for lat, lng in zip(lat_list, lng_list):
            conv = convert_geodetic_datum(lat, lng)
            convd_lat.append(conv[0])
            convd_lng.append(conv[1])

        df["convd_lat"] = convd_lat
        df["convd_lng"] = convd_lng

        df = df.drop(["lat", "lng"], axis=1)

        insert_data_from_hypocenter(cur, df)

        # get_lonlat_list(df)
        print(url, " is inserted.")
        time.sleep(5)

    close_connect_db(conn, cur)


# FUNCTION
def get_data_from_web(url: str, key: str) -> str:
    """
    Get Seism data from web that JMA.
    """
    selector = "#menu > li > ul > pre"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.select(selector)[0]
    if data is not None:
        data = str(data).replace("<pre>\n", "").replace("</pre>", "")
        txt_file_path = DOWNLOAD_PATH + key + ".txt"
        with open(txt_file_path, "w") as fil:
            fil.write(data)
            fil.close()
        return txt_file_path
    else:
        return None


def convert_csv_from_txt(txt_file_path: str, key: str) -> str:
    """
    Convert csv file from txt file.
    This txt file is copied from credit.
    """
    data = []
    with open(txt_file_path, "r") as fil:
        next(fil)
        next(fil)
        for row in fil:
            cols = [x for x in row.replace("\n", "").split(" ") if len(x) > 0]
            if len(cols) == 0:
                continue

            date_time: str = "{0}-{1}-{2} {3}:{4}".format(
                cols[0], cols[1], cols[2], cols[3], cols[4]
            )

            lat: str = ""
            lng: str = "None"
            index: int = 0
            if len(cols) == 10:
                lat = cols[5]
                lng = cols[6]
                index = 7
            elif len(cols) == 11:
                if "N" not in cols[5]:
                    lat = cols[5] + cols[6]
                    if "E" not in cols[7]:
                        lng = cols[7] + cols[8]
                        index = 9
                    else:
                        lng = cols[7]
                        index = 8
                else:
                    lat = cols[5]
                    if "E" not in cols[6]:
                        lng = cols[6] + cols[7]
                        index = 8
                    else:
                        lng = cols[6]
                        index = 7
            elif len(cols) == 12:
                lat = cols[5] + cols[6]
                lng = cols[7] + cols[8]
                index = 9

            depth: str = cols[index]
            magnitude: str = cols[index + 1]
            area: str = cols[index + 2]

            data.append(
                {
                    "date_time": date_time,
                    "lat": lat,
                    "lng": lng,
                    "depth": depth,
                    "magnitude": magnitude,
                    "area": area,
                }
            )
    # output
    csv_file_path = DOWNLOAD_PATH + key + ".csv"
    with open(csv_file_path, "w") as fil:
        writer = csv.DictWriter(fil, fieldnames=data[0].keys())
        writer.writeheader()
        for d in data:
            writer.writerow(d)
        fil.close()

    return csv_file_path


def convert_location(loc: str) -> float:
    """
    Convert 60-ary to decimal.
    """
    t: str = loc.replace("N", "").replace("E", "")
    li = t.split("°")
    return float(li[0]) + (float(li[1].replace("'", "")) / 60)


def convert_geodetic_datum(latitude: float, longitude: float) -> tuple:
    """
    Convert japanese geodetic system to global geodetic system.
    type = 1 latitude
    type = 2 longitude
    """
    converted_latitude: float = (
        latitude - 0.00010695 * latitude + 0.000017464 * longitude + 0.0046017
    )
    converted_longitude: float = (
        longitude - 0.000046038 * latitude - 0.000083043 * longitude + 0.01004
    )
    return (converted_latitude, converted_longitude)


def get_lonlat_list(df: Any) -> None:
    """
    get lonlat list for open street map.
    """
    nda = df.loc[
        :, ["convd_lng", "convd_lat", "date_time", "depth", "area", "magnitude"]
    ].to_numpy()
    res = []
    for d in nda:
        tmp = "[{0},{1},'{2}',{3},'{4}',{5}]".format(
            d[0], d[1], d[2], d[3], d[4], (d[5] if d[5] != "-" else 0)
        )
        res.append(tmp)
    print(",\n".join(res))


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


def insert_data_from_hypocenter(cur: Any, df: Any) -> None:
    """
    insert data to db from hypocenter.
    """
    nda = df.to_numpy()
    sql = """
    INSERT INTO hypocenter (area, lat, lng, depth, magnitude, date_time)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    date_time_idx = 0
    depth_idx = 1
    magnitude_idx = 2
    area_idx = 3
    lat_idx = 4
    lng_idx = 5

    for d in nda:
        cur.execute(
            sql,
            (
                d[area_idx],
                d[lat_idx],
                d[lng_idx],
                d[depth_idx],
                d[magnitude_idx],
                d[date_time_idx],
            ),
        )


if __name__ == "__main__":
    main()
