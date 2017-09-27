#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab as p
import math
import random

n = int(input("Ile ruchów? "))
x = y = 0
lx = [0]
ly = [0]
with open("rbrowna.xls", "w") as plik:
    print("x\ty", file=plik)
    print(str(x) + "\t" + str(y), file=plik)
    for i in range(0, n):
        rad = float(random.randint(0, 360)) * math.pi / 180
        x = x + math.cos(rad)
        y = y + math.sin(rad)
        print(str(x) + "\t" + str(y), file=plik)
        lx.append(x)
        ly.append(y)

s = math.sqrt(x**2 + y**2)
p.plot(wx, wy, "o:", color="green", linewidth=3, alpha=0.5)
# r:., r:+, r., r+, o:, +:, color="green"
p.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
p.xlabel("Wsp_x")
p.ylabel("Wsp_y")
p.title("Ruchy Browna")
p.grid(True)
p.show()
