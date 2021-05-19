#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mtools import *


def main(args):
    dane = czytaj_csv('../dane/pisemne.csv')
    print(dane)
    seria = [int(row[1]) for row in dane]
    print(seria)
    n, bins, patches = plt.hist(seria, 10, facecolor='green')

    plt.xlabel('Wyniki w pkt')
    plt.ylabel('Częstość')
    # plt.axis([0, 50, 0, 0.1])
    plt.show()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
