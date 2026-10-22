# Oppslagsark IT2 – filer, JSON, pandas, figurer og klasser

Lov å bruke på prøven fredag i uke 44. Skriv det gjerne ut og legg til egne notater.

## Funksjoner

```python
def snitt(tall):
    '''Returnerer gjennomsnittet av tallene i lista.'''
    sum_tall = 0
    for t in tall:
        sum_tall += t
    return sum_tall / len(tall)


resultat = snitt([4, 8, 6])
```

- `return` sender verdien ut. `print` bare viser den, og da kan den ikke brukes videre.
- Standardverdier står sist: `def pris(antall, enhetspris=25):`
- En variabel som lages inne i en funksjon, finnes bare der.

## Regne med løkke

```python
storst = tall[0]
for t in tall:
    if t > storst:
        storst = t
```

Trenger du navnet som hører til, gå gjennom indeksene:

```python
storst_navn = navn[0]
storst = tall[0]
for i in range(len(tall)):
    if tall[i] > storst:
        storst = tall[i]
        storst_navn = navn[i]
```

Liste med dem som er over en grense:

```python
over = []
for i in range(len(tall)):
    if tall[i] > grense:
        over.append(navn[i])
```

## Lese en tekstfil

```python
with open('data/fil.txt', encoding='utf-8') as fil:
    for linje in fil:
        deler = linje.strip().split(' ')
```

- `strip()` fjerner linjeskiftet. `split(';')` deler ved skilletegnet.
- Tekst fra fil er alltid tekst. Bruk `float()` eller `int()`.

## Lese en CSV-fil

```python
import csv

maneder = []
verdier = []

with open('data/fil.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)  # hopp over overskriftene
    for rad in innhold:
        maneder.append(rad[0])
        verdier.append(float(rad[1]))
```

| Ser du dette | Gjør dette |
|---|---|
| `﻿` foran første overskrift | `encoding='utf-8-sig'` |
| `UnicodeDecodeError` | prøv `encoding='latin-1'` |
| overskriftene havner i lista | `next(innhold)` før løkka |
| `TypeError` når du regner | glemt `float()` |

## Skrive til fil

```python
with open('resultat.txt', 'w', encoding='utf-8') as fil:
    for navn in liste:
        fil.write(f'{navn}\n')
```

`'w'` lager fila på nytt. `'a'` legger til på slutten. `\n` er linjeskift.

## JSON

```python
import json

with open('data/skole.json', encoding='utf-8') as fil:
    skole = json.load(fil)

print(skole['klasser'][0]['navn'])
for klasse in skole['klasser']:
    print(klasse['navn'], klasse['antall'])
```

JSON blir ordbøker og lister. Les én klamme om gangen, fra venstre: `skole['klasser']` er en liste, `[0]` er den første ordboka i lista.

## Pandas

```python
import pandas as pd

tabell = pd.read_csv('data/fil.csv', sep=';')
print(tabell.head())       # de fem første radene
print(tabell.shape)        # (rader, kolonner)
print(tabell.describe())   # snitt, minste, største per kolonne
```

En stygg fil fra SSB. Se på fila først, og velg innstillingene ut fra det du ser:

```python
medier = pd.read_csv(
    'data/ssbmedier.csv',
    skiprows=1,          # hopp over tittellinja
    sep=';',             # semikolon mellom verdiene
    index_col=0,         # første kolonne blir navn på radene
    na_values='..',      # .. blir NaN
    encoding='latin-1',  # fila er ikke utf-8
)
medier.columns = range(2013, 2026)  # like mange navn som kolonner
```

| Vil du | Skriv |
|---|---|
| hente en kolonne | `tabell['poeng']` |
| hente en rad med navn | `medier.loc['Radio']` |
| snitt, største, minste | `tabell['poeng'].mean()`, `.max()`, `.min()` |
| filtrere | `tabell[tabell['poeng'] > 40]` |
| to betingelser | `tabell[(tabell['a'] > 1) & (tabell['b'] == 'x')]` |
| telle forekomster | `tabell['klasse'].value_counts()` |
| snitt per gruppe | `tabell.groupby('klasse')['poeng'].mean()` |
| navnene på radene | `tabell.index` |

- I pandas er `mean()` lov. På vanlige lister regner du med løkke.
- `NaN` betyr at tallet mangler. `mean()` hopper over det, og i en figur blir det hull i linja.
- En kolonne kan gis rett til `plt.plot` og `plt.bar`, akkurat som en liste.

## Figurer

```python
import matplotlib.pyplot as plt

plt.plot(x, y, marker='o', label='Pris')
plt.axhline(snittpris, color='grey', linestyle='--', label='Snitt')
plt.title('Strømpris per måned')
plt.xlabel('Måned')
plt.ylabel('Øre per kWh')
plt.legend()
plt.grid()
plt.show()
```

| Figur | Kommando |
|---|---|
| kurve | `plt.plot(x, y)` |
| søyler | `plt.bar(x, y)` |
| liggende søyler | `plt.barh(x, y)` |
| punkter | `plt.scatter(x, y)` |
| histogram | `plt.hist(verdier)` |
| sektor | `plt.pie(verdier, labels=navn)` |

To figurer i samme vindu, den ene over den andre:

```python
plt.subplot(2, 1, 1)  # 2 rader, 1 kolonne, nummer 1
plt.bar(maneder, forbruk)
plt.title('Forbruk')

plt.subplot(2, 1, 2)
plt.plot(maneder, pris)
plt.title('Pris')

plt.tight_layout()
plt.savefig('figur.png')  # FØR show
plt.show()
```

- En figur uten tittel og aksetitler er ikke ferdig.
- `savefig` etter `show` lagrer et tomt bilde.
- `plt.xticks(rotation=45)` når navnene på x-aksen overlapper.

## Klasser

```python
class Konto:
    '''En bankkonto med eier og saldo.'''

    def __init__(self, eier, saldo=0):
        self.eier = eier
        self._saldo = saldo

    def sett_inn(self, belop):
        if belop < 0:
            raise ValueError('Beløpet kan ikke være negativt.')
        self._saldo += belop

    def vis_saldo(self):
        return self._saldo

    def __str__(self):
        return f'{self.eier}: {self._saldo:.2f} kr'


konto = Konto('Kari', 500)  # __init__ kjører
konto.sett_inn(250)         # self sendes ikke med
print(konto)                # bruker __str__
```

| Ord | Betyr |
|---|---|
| `class` | oppskriften |
| objekt | én ting laget fra oppskriften: `Konto('Kari', 500)` |
| `__init__` | kjører når objektet lages, og gir det attributtene |
| `self` | dette objektet. Står først i hver metode, men sendes ikke med i kallet |
| attributt | en verdi objektet har: `self.eier` |
| metode | en funksjon i klassen: `sett_inn` |
| `__str__` | bestemmer hva `print` viser. Uten den: `<__main__.Konto object at 0x…>` |
| `_saldo` | understrek: ikke endre denne utenfra, bruk metodene |
| `raise ValueError('…')` | stopper programmet med din egen feilmelding |

Objekter i en liste:

```python
kontoer = [Konto('Kari', 500), Konto('Ola'), Konto('Ali', 120)]
for k in kontoer:
    print(k)
```

Teste at en feil blir kastet:

```python
try:
    konto.sett_inn(-100)
except ValueError as feil:
    print('Feil fanget:', feil)
```

## Vanlige feilmeldinger

| Feilmelding | Vanlig årsak |
|---|---|
| `IndentationError` | feil innrykk, ofte `return` inne i løkka |
| `NameError: name 'x' is not defined` | skrivefeil, eller variabelen finnes bare inne i en funksjon |
| `IndexError: list index out of range` | indeksen er for stor, eller en tom linje i fila |
| `TypeError: '>' not supported between 'str' and 'int'` | glemt `float()` eller `int()` |
| `missing 1 required positional argument` | glemt `self`, eller for få argumenter |
| `FileNotFoundError` | feil filnavn, eller fila ligger ikke i `data/` ved siden av koden |
