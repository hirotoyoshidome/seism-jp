import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import Any
import csv


# convert to csv file from txt.
# credit :
# https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200101.html
# https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200102.html

# CONST
DOWNLOAD_PATH = "./data/"

# MAIN
def main() -> None:
    urls = [
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200101.html",
        "https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200102.html",
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

        # get_lonlat_list(df)


# FUNCTION
def get_data_from_web(url:str, key: str) -> str:
    """
    Get Seism data from web that JMA.
    """
    selector = "#menu > li > ul > pre"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
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


if __name__ == "__main__":
    main()
