#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ZADANIE: wykonaj wykres funkcji f(x), gdzie x = <-10;10> z krokiem 0.5
# f(x) = x/-3 + a dla x <= 0
# f(x) = x*x/3 dla x >= 0

from matplotlib import pyplot as plt
import numpy as np

lx = np.arange(-10, 10.5, 0.5)  # lista argumentów x
a = int(input("Podaj współczynnik a: "))

lx1 = [x for x in lx if x <= 0]
ly1 = [x / -3 + a for x in lx1]

lx2 = [x for x in lx if x >= 0]
ly2 = [x**2 / 3 for x in lx2]

# pylab.plot(lx[:len(ly1)], ly1, lx[-len(ly2):], ly2)
plt.plot(lx1, ly1, lx2, ly2)
plt.title('Wykres f(x)')
plt.grid(True)
plt.show()
