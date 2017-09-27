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
    srednie = [row[1].replace(',', '.') for row in dane]

    ile = np.arange(len(klasy))
    szerokosc = 0.5
    fig, ax1 = plt.subplots()
    ax1.bar(ile, srednie, szerokosc, align="center")
    ax1.set_ylim([0.1, 6.0])
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xticks(ile, klasy)

    # dodanie etykiet nad kolumnami
    # rects = ax1.patches
    # for rect, label in zip(rects, srednie):
    #     height = rect.get_height()
    #     ax1.text(rect.get_x() + rect.get_width() / 2, height, label,
    #              ha='center', va='bottom')

    # frek = [p2f(row[2]) for row in dane]
    # ax2 = ax1.twinx()
    # ax2.plot(frek, color="red")
    # wartosci = ax2.get_yticks()
    # ax2.set_yticklabels(['{:2.0f}%'.format(x * 100) for x in wartosci])
    plt.show()


klasy()
