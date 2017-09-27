#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mtools import *


def wybory():
    dane = czytaj_csv("../dane/dane_wybory.csv")
    etykiety = [row[0] for row in dane]
    frakcje = [row[1] for row in dane]
    kolory = ['grey', 'green', 'blue', 'red']
    explode = [0, 0, 0, 0.05]

    fig, ax = plt.subplots()
    fig.set_size_inches(9, 7)
    fig.canvas.set_window_title("Wykres kołowy")

    # patches – lista części graficznych wykresu (wycinków koła)
    # t1, t2 – listy etykiet tekstowych i numerycznych wykresu
    patches, t1, t2 = ax.pie(frakcje, explode=explode, labels=etykiety,
                             colors=kolory, autopct='%.2f%%', shadow=True,
                             startangle=180)
    ax.axis('equal')
    # fig.savefig('test2png.png', dpi=100)
    plt.legend(patches, etykiety, loc="upper right")
    plt.tight_layout()
    plt.show()


def main(args):
    wybory()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
