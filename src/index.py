# credit : https://www.data.jma.go.jp/svd/eqev/data/daily_map/20200101.html

with open("./data/sample.txt", "r") as fil:
    for row in fil:
        cols = [x for x in row.replace("\n", "").split(" ") if len(x) > 0]
        if len(cols) == 0:
            continue

        print(cols)
