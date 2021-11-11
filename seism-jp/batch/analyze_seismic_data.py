import numpy as np
import csv
import matplotlib.pyplot as plt
import math


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

# second
tau = 0.3

# np.set_printoptions(threshold=np.inf)


# MAIN
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

    # generate_image(ns, "NS")
    # generate_image(ew, "EW")
    # generate_image(ud, "UD")

    # ns_max = np.amax(ns)
    # ew_max = np.amax(ew)
    # ud_max = np.amax(ud)
    # print("NS MAX : ", ns_max)
    # print("EW MAX : ", ew_max)
    # print("UD MAX : ", ud_max)

    # NOTE: fault.
    # Freq = np.fft.fftfreq(N, d=dt)
    # X = Freq / 10
    # fh = high_filter(X)
    # fl = low_filter(Freq)
    # fc = fc_filter(Freq)
    # fa = fc * fh * fl
    # IF = F * fa
    # f2 = np.fft.ifft(IF)

    # fourier -> filtering -> inverse fourier.
    ns2 = filter_with_fourier(ns)
    ew2 = filter_with_fourier(ew)
    ud2 = filter_with_fourier(ud)

    # generate_image(ns2, "NS2")
    # generate_image(ew2, "EW2")
    # generate_image(ud2, "UD2")

    # composition of vectors.
    C = composition_vectors(ns2, ew2, ud2)
    # sort desc.
    sC = -np.sort(-C)

    tau_index = math.floor(tau / dt) - 1
    mI = calc_measured_seismic_intensity(sC[tau_index])
    I = predict_seismic_intensity(mI)
    print("measured_seismic_intensity is {0}, seismic_intensity is {1}".format(mI, I))


# FUNCTIONS
def generate_image(datapoint, name):
    fig = plt.figure(figsize=(20, 4), dpi=72, facecolor="white", linewidth=5, edgecolor="orange")
    X = [x * dt for x in range(datapoint.shape[0])]
    Y = datapoint
    ax = fig.add_subplot(1, 1, 1, xlabel="second", ylabel=name)
    ax.plot(X, Y)
    plt.savefig("output/{0}.png".format(name))


def filter_with_fourier(datapoint):
    F = np.fft.fft(datapoint)
    N = F.shape[0]
    # because Gaussian distribution, reduce calclation.
    N2 = N / 2

    for i in range(1, int(N2) + 1):
        freq = i / (N * dt)
        x = freq / 10

        fh = high_filter(x)
        fl = low_filter(freq)
        fc = fc_filter(freq)
        fa = fc * fh * fl

        F[i - 1] = F[i - 1] * fa
        F[N - i] = F[N - i] * fa

    F2 = np.fft.ifft(F)
    return F2


def composition_vectors(f1, f2, f3):
    return np.sqrt(f1 ** 2 + f2 ** 2 + f3 ** 2)


def calc_measured_seismic_intensity(alpha):
    return 2 * math.log10(alpha) + 0.94


def predict_seismic_intensity(mi):
    if mi < 0.5:
        return 0
    elif mi < 1.5:
        return 1
    elif mi < 2.5:
        return 2
    elif mi < 3.5:
        return 3
    elif mi < 4.5:
        return 4
    elif mi < 5:
        return -5
    elif mi < 5.5:
        return 5
    elif mi < 6:
        return -6
    elif mi < 6.5:
        return 6
    elif mi > 6.5:
        return 7


def high_filter(x):
    return 1 / math.sqrt(
        1
        + 0.694 * x ** 2
        + 0.241 * x ** 4
        + 0.0557 * x ** 6
        + 0.009664 * x ** 8
        + 0.00134 * x ** 10
        + 0.000155 * x ** 12
    )


def fc_filter(freq):
    return np.sqrt(1 / freq)


def low_filter(freq):
    return math.sqrt(1 - math.exp(-((freq / f0) ** 3)))


# numpy ver .
# def high_filter(datapoint):
#     return 1 / np.sqrt(
#         1
#         + 0.694 * datapoint ** 2
#         + 0.241 * datapoint ** 4
#         + 0.0557 * datapoint ** 6
#         + 0.009664 * datapoint ** 8
#         + 0.00134 * datapoint ** 10
#         + 0.000155 * datapoint ** 12
#     )
# numpy ver .
# def fc_filter(freq):
#     return np.sqrt(1 / freq)
# numpy ver .
# def low_filter(freq):
#     max_freq = np.max(freq)
#     return np.sqrt(1 - np.exp(-(((freq - max_freq) / (f0 - max_freq)) ** 3)))


if __name__ == "__main__":
    main()
