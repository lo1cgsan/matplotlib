Matplotlib – wybrane metody
=============================

pyplot
------

```python
import matplotlib.pyplot as plt
```

- `plt.title('tytuł', y=1.05)` – tytuł wykresu
- `plt.ylabel('oś y')` – etykieta osi y
- `plt.xlabel('oś x')` – etykieta osi x
- `plt.axhline(linewidth=1.0, color="black")` – oś x układu współrzędnych
- `plt.axvline(linewidth=1.0, color="black")` – oś y układu współrzędnych
- `plt.tight_layout()` – automatyczne dostosowanie prametrów wykresu
- `plt.xticks(ile, etykiety)` – ustawia położenie i etykiety na osi x

axes
----

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