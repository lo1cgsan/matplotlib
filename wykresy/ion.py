#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# polecenia przeznaczone do wykonania po kolei w konsoli

plt.ion()
plt.plot([1.6, 2.7])
plt.title("tryb interaktywy")
plt.xlabel("index")
ax = plt.gca()
ax.plot([3.1, 2.2])
plt.draw()
