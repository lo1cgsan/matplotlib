Matplotlib – wybrane metody
=============================

## pyplot


```python
import matplotlib.pyplot as plt
```

- `plt.title('tytuł', y=1.05)` – tytuł wykresu
- `plt.ylabel('oś y')` – etykieta osi y
- `plt.xlabel('oś x')` – etykieta osi x
- `plt.text(x, y, 'tekst')` - daodaje tekst w określonym miejscu
` `plt.yscale('log')` – określa rodzaj skali, np. logarytmiczny
- `plt.xticks(np.arange(5), ('a', 'b', 'c', 'd', 'f'))` – ustawia ilość znaczników osi x i opcjonalnie ich etykiety
- `plt.axis([xmin, xmax, ymin, ymax])` – określa widoczną część wykresu
- `plt.axhline(linewidth=1.0, color="black")` – oś x układu współrzędnych
- `plt.axvline(linewidth=1.0, color="black")` – oś y układu współrzędnych
- `plt.tight_layout()` – automatyczne dostosowanie prametrów wykresu
- `plt.xticks(ile, etykiety)` – ustawia położenie i etykiety na osi x
- `plt.gcf()` – zwraca aktualną figurę
- `plt.gca()` – zwraca aktualny obszar wykresu
– `plt.clf()` – czyści aktualną figurę
– `plt.cla()` – czyści aktualny obszar wykresu

## axes

```python
fig, ax = plt.subplots()
```


- `ax.set_facecolor('lightgrey')` – kolor tła wykresu
- `ax.axis([-6, 6, -6, 6])` – zakres skal x i y
- `ax.axhline(linewidth=1.0, color="black")` – oś x układu współrzędnych
- `ax.axvline(linewidth=1.0, color="black")` – oś y układu współrzędnych
- `ax.plot(lx, ly, c='green', ls='dotted', lw=2, marker='o')`
- `ax.text(x, y, tekst, ha='center', va='bottom')` – umieszcza tekst w podanych współrzędnych

– lub:

```python
opcje = dict(c='green', ls='dotted', lw=2, marker='x')
ax.plot(lx, ly, **opcje**)
```

### Opcje (wybór)

- `color` (`c`) – kolor
- `label` – etykieta drukowana za pomocą operatora `%s` do autolegendy (`legend()`)
- `linestyle` (`ls`) – 'solid' ('-'), 'dashed' ('--'), 'dashdot' ('-.'), 'dotted' (':')
- `linewidth` (`lw`) – wartość float w punktach
- `marker` – '.' (punkt), ',' (piksel), 'o' (kółko), '^', 'v', '<', '>' – trójkąty, 's' – kwadrat, '\*' – gwiazdka
- `autoptc` – ciąg formatujący (`fmt%pct`) lub funkcja używana do etykietowania części wykresu (ang. *wedges*) (kolumna, wycinek koła)