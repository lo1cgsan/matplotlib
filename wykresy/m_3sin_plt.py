#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def f1(t1):
    return np.sin(t1)


def f2(t1):
    return [np.sin(3 * x) for x in t1]


def f3(t1):
    return 3 * np.sin(t1)


t1 = np.arange(-360., 365., 5.)
# t1 = np.linspace(-360, 365, 146)
t1_radiany = [x * np.pi / 180 for x in t1]

# plt.subplot(311)
plt.plot(t1, f1(t1_radiany), 'r-')

# plt.subplot(312)
plt.plot(t1, f2(t1_radiany), 'g-')

# plt.subplot(313)
plt.plot(t1, f3(t1_radiany), 'b-')

plt.xlabel('Stopnie')
plt.axis([-360, 360, -3, 3.5])
plt.grid(True, axis='y')

plt.show()
