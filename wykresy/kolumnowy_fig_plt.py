#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from mtools import *


def p2f(x):
    return float(x.strip('%')) / 100


def klasy():
    dane = czytaj_csv("../dane/dane_klasa1A.csv")
    dane.pop(0)  # usunięcie etykiet
    klasy = [row[0] for row in dane]
    srednie = [float(row[1].replace(',', '.')) for row in dane]

    ile = np.arange(len(klasy))
    szerokosc = 0.5
    plt.bar(ile, srednie, szerokosc)
    plt.ylim([0.1, 6.0])
    # ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xticks(ile, klasy)

    # dodanie etykiet nad kolumnami
    # rects = ax1.patches
    # for rect, label in zip(rects, srednie):
    #     height = rect.get_height()
    #     ax1.text(rect.get_x() + rect.get_width() / 2, height, label,
    #              ha='center', va='bottom')

    frek = [p2f(row[2]) for row in dane]
    plt.twinx()
    plt.plot(frek, color="red")
    wartosci = plt.yticks()
    plt.ylabel(['{(x * 100):2.0f}%' for x in wartosci])
    plt.show()


klasy()
