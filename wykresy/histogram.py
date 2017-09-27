#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mtools import *


def main(args):
    dane = czytaj_csv('../dane/pisemne.csv')
    seria = [int(row[1]) for row in dane]
    n, bins, patches = plt.hist(seria, 15, normed=1, facecolor='green')

    # y = mlab.normpdf(bins, 15, 66)
    # l = plt.plot(bins, y, 'r--', linewidth=1)

    plt.xlabel('Wyniki w pkt')
    plt.ylabel('Częstość')
    plt.axis([0, 50, 0, 0.1])
    plt.show()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
