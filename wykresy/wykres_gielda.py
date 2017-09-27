# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv  # moduł do obsługi formatu csv
from mtools import *



def wykres(ax, x, y, **kwargs):
    """
    Funkcja wizualizuje wykres funkcji, której argumenty zawiera lista x
    a wartości lista y i ew. dodatkowe listy w parametrze *extra
    """
    out = ax.plot(x, y, **kwargs)
    return out


plik = "dane_gielda.csv"
dane = dane_z_pliku(plik)

etykiety = dane.pop(0)
dane = wyczysc_dane(dane)
print(dane)
