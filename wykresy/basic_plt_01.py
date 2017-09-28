#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
print(t)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

# właściwości: keyword arguments
plt.plot(t, t, 'r--', linewidth=3, label='Linia 1')
plt.legend()
# właściwości: metody obiektu(ów) line(s)
# linia, = plt.plot(t, t, 'r--')
# linia.set_lw(3)

# właściwości: metoda setp() jak w MATLAB
# linia, = plt.plot(t, t, 'r--')
# plt.setp(linia, linewidth='3')

plt.show()
