#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random


def rbrowna():
    n = int(input("Ile ruchów? "))
    x, y = 0, 0
    lx = [0]
    ly = [0]
    # zapisz_csv("rbrowna.csv", [['x', 'y']])  # zapisz etykiety
    for i in range(0, n):
        rad = float(random.randint(0, 360)) * np.pi / 180
        x = x + np.cos(rad)
        y = y + np.sin(rad)
        print(x, y)
        lx.append(x)
        ly.append(y)

    # zapisz_csv("rbrowna.csv", zip(lx, ly), "a")
    # print(list(zip(lx, ly)))

    s = np.sqrt(x**2 + y**2)  # obliczenie wektoru przesunięcia
    print("Wektor przesunięcia: {:.2f}".format(s))
    fig, ax = plt.subplots()
    ax.plot(lx, ly, 'go-', lw=1.0)
    fig.canvas.set_window_title("Ruchy Browna")
    ax.set_title("Ruchy Browna")
    ax.grid()
    ax.set_xlabel("lx")
    ax.set_ylabel("ly")
    ax.legend(
        ["x = {:.2f}, y = {:.2f}\nPrzemieszczenie: {:.2f}".format(x, y, s)],
        loc="upper left")
    # ax.arrow(0, 0, lx.pop(), ly.pop(), head_width=0.15, color="red")
    ax.quiver(0, 0, lx.pop(), ly.pop(), angles='xy', scale_units='xy',
              scale=1)
    plt.show()


def main(args):
    rbrowna()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
