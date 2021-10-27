# convert to csv file from txt.
# credit :
# https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200101.html
# https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200102.html


def main():
    filepath = "./data/2020-02.txt"
    with open(filepath, "r") as fil:
        next(fil)
        next(fil)
        print("date_time, lat, lng, depth, magnitude, area")
        for row in fil:
            cols = [x for x in row.replace("\n", "").split(" ") if len(x) > 0]
            if len(cols) == 0:
                continue

            date_time = "{0}-{1}-{2} {3}:{4}".format(cols[0], cols[1], cols[2], cols[3], cols[4])

            lat = None
            lng = None
            index = None
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

            depth = cols[index]
            magnitude = cols[index + 1]
            area = cols[index + 2]

            print(date_time, lat, lng, depth, magnitude, area, sep=",")


if __name__ == "__main__":
    main()
