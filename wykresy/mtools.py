#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


def czytaj_csv(plik, separator=';'):
    """
    Zwraca wiersze z pliku csv w postaci listy list (rekordów)
    @params: plik - nazwa pliku, separator – znak używany jako delimiter
    """
    dane = []
    with open(plik, newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for lista in tresc:
            dane.append(lista)
    return dane


def zapisz_csv(plik, dane, tryb="w"):
    """
    Zapis danych w formacie csv do pliku
    @params: plik - nazwa pliku, dane - lista list(rekordów),
    tryb - "w"-zapis, "a"-dopisywanie
    """
    with open(plik, tryb, newline='') as plikcsv:
        tresc = csv.writer(plikcsv)
        for lista in dane:
            tresc.writerow(lista)


def wyczysc_dane(dane, pole):
    """
    Przygotowanie wartości finansowych do zapisania w bazie
    @params: dane – lista rekordów, pole – numer pola do oczyszczenia
    """
    for i, rekord in enumerate(dane):
        el = rekord[pole]
        el = el.replace('zł', '')  # usuń zł
        el = el.replace(' ', '')  # usun spacje
        el = el.replace(',', '.')  # zamien przecinki na kropki
        dane[i][pole] = el
    return dane


def wykres(ax, x, y, **kwargs):
    """
    Funkcja rysuje i zwraca obiekt wykresu
    @params: ax - obiekt Axes, x, y – listy wartości x i y
    **kwargs – opcjonalny słownik z nazwanymi parametrami wykresu
    """
    out = ax.plot(x, y, **kwargs)
    return out
