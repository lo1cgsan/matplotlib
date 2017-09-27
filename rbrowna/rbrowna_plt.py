#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np  # import biblioteki do obliczeń naukowych
import matplotlib.pyplot as plt  # import biblioteki do tworzenia wykresów
from random import randint


def wykres(x, y, tytul="Wykres funkcji", *extra):
    """
    Funkcja wizualizuje wykres funkcji, której argumenty zawiera lista x
    a wartości lista y i ew. dodatkowe listy w parametrze *extra
    """
    if len(extra):
        plt.plot(x, y, extra[0], extra[1])  # dwa wykresy na raz
    else:
        plt.plot(x, y, "o:", color="blue", linewidth=3, alpha=0.8)
    plt.title(tytul)
    plt.grid(True)
    plt.show()


def rBrowna():

    n = int(input("Ile ruchów? "))
    r = int(input("Krok przesunięcia? "))

    x = y = 0
    lx = [0]  # lista odciętych
    ly = [0]  # lista rzędnych

    for i in range(0, n):
        # losujemy kąt i zamieniamy na radiany
        rad = float(randint(0, 360)) * np.pi / 180
        x = x + r * np.cos(rad)  # wylicz współrzędną x
        y = y + r * np.sin(rad)  # wylicz współrzędną y
        lx.append(x)
        ly.append(y)

    # oblicz wektor końcowego przesunięcia
    s = np.fabs(np.sqrt(x**2 + y**2))
    print("Wektor przesunięcia: {:.2f}".format(s))

    wykres(lx, ly, "Ruchy Browna")


def main():
    rBrowna()
    return 0


if __name__ == '__main__':
    main()
