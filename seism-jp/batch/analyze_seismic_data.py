import numpy as np
import csv
import matplotlib.pyplot as plt


# credit : https://www.data.jma.go.jp/svd/eqev/data/kyoshin/jishin/110311_tohokuchiho-taiheiyouoki/wave/L311E081.png

filepath = "./20110311-ishinomaki.csv"
start_row = 7

# 5min data.
# all datapoint count is 30,000
# 300s / 30,000 = 0.01s/1datapoint.
dt = 0.01


def main():
    NS, EW, UD = [], [], []

    with open(filepath, "r") as fil:
        reader = csv.reader(fil)
        # skip.
        for i in range(start_row):
            next(reader)

        for row in reader:
            NS.append(row[0])
            EW.append(row[1])
            UD.append(row[2])

    # numpy array.
    ns = np.array(NS).astype(np.float)
    ew = np.array(EW).astype(np.float)
    ud = np.array(UD).astype(np.float)

    ns_max = np.amax(ns)
    ew_max = np.amax(ew)
    ud_max = np.amax(ud)

    print("NS MAX : ", ns_max)
    print("EW MAX : ", ew_max)
    print("UD MAX : ", ud_max)

    generate_image(ns, "NS")
    generate_image(ew, "EW")
    generate_image(ud, "UD")


def generate_image(datapoint, name):
    fig = plt.figure(figsize=(20, 4), dpi=72, facecolor="white", linewidth=5, edgecolor="orange")
    X = [x * dt for x in range(datapoint.shape[0])]
    Y = datapoint
    ax = fig.add_subplot(1, 1, 1, xlabel="second", ylabel=name)
    ax.plot(X, Y)
    plt.savefig("output/{0}.png".format(name))


if __name__ == "__main__":
    main()
