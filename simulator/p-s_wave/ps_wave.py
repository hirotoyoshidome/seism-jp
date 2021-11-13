import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# CONSTS
step = 50
dt = 1


def main():
    # generate_image(p_wave, s_wave, "wave")
    generate_animation()


# FUNCTION.
def p_wave(t):
    return 4 * t


def s_wave(t):
    return 8 * t


def generate_image(f, f2, name):
    fig = plt.figure(figsize=(12, 8), dpi=72, facecolor="white", linewidth=5, edgecolor="orange")
    X = [i + 1 for i in range(step)]
    pY = [f(i + 1) for i in range(step)]
    sY = [f2(i + 1) for i in range(step)]
    ax = fig.add_subplot(1, 1, 1, xlabel="time (s)", ylabel="distance (km)")
    ax.plot(X, pY, label="P-Wave")
    ax.plot(X, sY, label="S-wave")
    plt.legend(loc="best")
    plt.savefig("./{0}.png".format(name))


def generate_animation():
    fig, ax = plt.subplots()
    ax.set_xlim(0, step)
    ax.set_ylim(0, step * 10)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("distance (km)")
    ax.set_title("p-wave, s-wave")
    anim = FuncAnimation(
        fig, update_anim_wave, frames=range(step), interval=dt * 1000, blit=True, repeat=True
    )
    # plt.show()
    anim.save("time-distanct.gif", writer="imagemagick")


def update_anim_wave(t):
    (obj1,) = plt.plot([], [], "o", label="P-Wave")
    (obj2,) = plt.plot([], [], "^", label="S-Wave")
    obj1.set_data(t, p_wave(t))
    obj2.set_data(t, s_wave(t))
    return (
        obj1,
        obj2,
    )


if __name__ == "__main__":
    main()
