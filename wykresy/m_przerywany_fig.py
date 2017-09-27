#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ZADANIE: wykonaj wykres funkcji f(x) = 1 / (x^2 - 1)
# dla x = <-5;5> z krokiem 0,1

import numpy as np
import matplotlib.pyplot as plt


lx = np.arange(-5, 5.1, 0.1)  # lista argumentów x
lx = [round(x, 1) for x in lx]
ly = []
for x in lx:
    if x == -1 or x == 1:
        ly.append(None)
    else:
        ly.append(1 / (x**2 - 1))


fig, ax = plt.subplots()
fig.canvas.set_window_title('y = 1 / (x^2 - 1)')
ax.set_facecolor('lightgrey')
ax.axis([-6, 6, -6, 6])
ax.axhline(linewidth=1.0, color="black")
ax.axvline(linewidth=1.0, color="black")
ax.text(0, 6.2, 'y', ha='center')
ax.text(6.1, 0, 'x', va='center')
ax.plot(lx, ly, lw=3)
plt.title('Wykres funkcji: y = 1/(x^2 -1)', y=1.05)
plt.ylabel('y = 1/(x^2 -1)')
plt.xlabel('x = <-5;5>)')

plt.show()
