#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return t**2
    # return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0, 11, 1)
t2 = np.arange(0., 10.5, 0.5)

# t1 = np.arange(0., 5., 0.1)
# t2 = np.arange(0., 5., 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t1, t1**3, 'r--')

# druga figura
plt.figure(2)
plt.plot(t2, np.sqrt(t2))  # domyślnie subplot(111)

plt.title('Wiele wykresów')
plt.show()
plt.close('all')  # zwolnienie pamięci
