#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0.0, 100.0, 1)
y = 5 * np.sin(0.1 * np.pi * x)
y = [round(i, 4) for i in y]
plt.title('Wykres: y = 5 * sin(0.1 * PI * x)')
plt.plot(x, y)
plt.show()
