import pandas as pd


# convert to csv file from txt.
# credit :
# https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200101.html
# https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200102.html


# MAIN
def main() -> None:
    # If you exist csv file, this function is commented out.
    # convert_csv_from_txt()

    df = pd.read_csv("./output/2020-01.csv")

    # Latitude.
    df["lat"] = df["lat"].apply(lambda x: convert_location(x))
    # Longitude.
    df["lng"] = df["lng"].apply(lambda x: convert_location(x))
    print(df.head())


# FUNCTION
def convert_csv_from_txt() -> None:
    """
    Convert csv file from txt file.
    This txt file is copied from credit.
    """
    filepath = "./data/2020-02.txt"
    with open(filepath, "r") as fil:
        next(fil)
        next(fil)
        print("date_time,lat,lng,depth,magnitude,area")
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

            print(date_time, lat, lng, depth, magnitude, area, sep=",")


def convert_location(loc: str) -> float:
    """
    Convert 60-ary to decimal.
    """
    t: str = loc.replace("N", "").replace("E", "")
    li = t.split("°")
    return float(li[0]) + (float(li[1].replace("'", "")) / 60)


def convert_geodetic_datum() -> None:
    """
    Convert japanese geodetic system to global geodetic system.
    """
    pass


if __name__ == "__main__":
    main()
