#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab as p
x = p.arange(0.0, 100.0, 1)
y = 5 * p.sin(0.1 * p.pi * x)
y = [round(i, 4) for i in y]
p.title('Wykres: y = 5 * sin(0.1 * PI * x)')
p.plot(x, y)
p.show()
