import numpy as np
import csv
import matplotlib.pyplot as plt


# credit : https://www.data.jma.go.jp/svd/eqev/data/kyoshin/jishin/110311_tohokuchiho-taiheiyouoki/wave/L311E081.png

filepath = "./20110311-ishinomaki.csv"
start_row = 7

# sampling cycle.
# 5min data.
# all datapoint count is 30,000
# 300s / 30,000 = 0.01s/1datapoint.
dt = 0.01
# Hz
f0 = 0.5
f1 = 100

np.set_printoptions(threshold=np.inf)


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
    ns = np.array(NS).astype(np.float128)
    ew = np.array(EW).astype(np.float128)
    ud = np.array(UD).astype(np.float128)

    # ns_max = np.amax(ns)
    # ew_max = np.amax(ew)
    # ud_max = np.amax(ud)

    # print("NS MAX : ", ns_max)
    # print("EW MAX : ", ew_max)
    # print("UD MAX : ", ud_max)

    # generate_image(ns, "NS")
    # generate_image(ew, "EW")
    # generate_image(ud, "UD")

    F_ns = np.fft.fft(ns)
    N_ns = F_ns.shape[0]
    Freq_ns = np.fft.fftfreq(N_ns, d=dt)
    X_ns = Freq_ns / 10

    fh = high_filter(X_ns)
    fl = low_filter(Freq_ns)
    # fc = fc_filter(Freq_ns)
    # fa = fc * fh * fl
    # print(fa)

    # generate_image(F_ns, "sample")
    # generate_image(Freq_ns, "sample")


def generate_image(datapoint, name):
    fig = plt.figure(figsize=(20, 4), dpi=72, facecolor="white", linewidth=5, edgecolor="orange")
    X = [x * dt for x in range(datapoint.shape[0])]
    Y = datapoint
    ax = fig.add_subplot(1, 1, 1, xlabel="second", ylabel=name)
    ax.plot(X, Y)
    plt.savefig("output/{0}.png".format(name))


def high_filter(datapoint):
    return 1 / np.sqrt(
        1
        + 0.694 * datapoint ** 2
        + 0.241 * datapoint ** 4
        + 0.0557 * datapoint ** 6
        + 0.009664 * datapoint ** 8
        + 0.00134 * datapoint ** 10
        + 0.000155 * datapoint ** 12
    )


def fc_filter(freq):
    return np.sqrt(1 / freq)


def low_filter(freq):
    return np.sqrt(1 - np.exp(-((freq / f0) ** 3)))


if __name__ == "__main__":
    main()
