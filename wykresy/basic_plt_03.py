#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


t1 = np.arange(0, 11, 1)
t2 = np.arange(0., 10.5, 0.5)

plt.figure(1)
plt.subplot(121)
plt.plot(t1, t1**2, 'bo', t2, t2**2, 'k')
plt.title('Kwadrat liczb')
plt.xlabel('x = <0, 10>')
plt.ylabel('y = x^2')
# plt.text(1, 90, 'Ładny wykres?')

plt.subplot(122)
plt.plot(t1, t1**3, 'r--')
plt.xlabel('x = <0, 10>', fontsize=20, color='blue')
plt.ylabel('y = x^3')
plt.axis([0, 10, 0, 1000])
plt.grid(True)
# plt.yscale('log')
# plt.tight_layout()

# plt.subplot(223)
# plt.plot(t1 / 10, t1, 'go')
# plt.xlabel(r'$\frac{x}{10}$')
plt.show()
