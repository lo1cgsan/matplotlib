# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def fn1():
    """
    Wykres funkcji liniowej: y = a * x + b
    """
    a = 1
    b = 2
    lx = list(range(-10, 11))  # lista argumentów x
    ly = [a * x + b for x in lx]
    plt.plot(lx, ly, 'b^')


def fn2():
    lx = np.arange(-10, 10.5, 0.5)  # lista argumentów x
    a = int(input("Podaj współczynnik a: "))
    ly1 = [x / -3 + a for x in lx if x <= 0]
    ly2 = [x**2 / 3 for x in lx if x >= 0]

    print(lx, len(lx))
    print(ly1, len(ly1))
    plt.plot(lx[:len(ly1)], ly1, lx[-len(ly2):], ly2)


def fn3():
    lx = list(range(-10, 11))
    a = 1
    b = -3
    c = 1
    ly = [a * (x**2) + b * x + c for x in lx]
    plt.plot(lx, ly)


plt.figure(1)
fig = plt.gcf()
fig.set_size_inches(4, 8)
plt.subplot(311)
fn1()
plt.subplot(312)
fn2()
plt.subplot(313)
fn3()
plt.show()
