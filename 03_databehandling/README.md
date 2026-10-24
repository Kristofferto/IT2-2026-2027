# 3 Databehandling — oppsummering

Graftegning (3A, uke 42), filer og datasett (3B, uke 43), Datalabben (fagdagen i uke 44) og dataanalyse der brukeren velger (uke 47).

Hvert tema har en typisk oppgave nederst. Prøv selv før du åpner løsningen. **På eksamen** viser hvilke eksamensoppgaver som tester temaet. Oppgaver som leser en fil, lagrer du i `3B_filer_og_datasett`, så finner de `data/`.

Filene fra timene står nederst, under [Filene i kapittelet](#filene-i-kapittelet).

[Diagramtyper](#1-diagramtypene) ·
[Pynt](#2-tekst-rutenett-og-forklaring) ·
[Subplot](#3-flere-figurer-og-lagring) ·
[Tekstfiler](#4-lese-en-tekstfil) ·
[Skrive](#5-skrive-til-fil) ·
[CSV](#6-csv-med-csvreader) ·
[Encoding](#7-encoding) ·
[JSON](#8-json) ·
[Pandas](#9-pandas) ·
[Stygge filer](#10-stygge-filer) ·
[Filtrere](#11-filtrere-og-gruppere) ·
[Kjeden](#12-hele-kjeden) ·
[Feller](#13-fellene-som-tar-flest)

---

## 1. Diagramtypene

```python
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()
```

`plot()` tegner, `show()` viser. Alt som tegnes før `show()`, havner i samme figur.

| Figur | Kommando | Bruk når |
|---|---|---|
| linjegraf | `plt.plot(x, y)` | noe utvikler seg, for eksempel over tid |
| punktdiagram | `plt.scatter(x, y)` | du vil se sammenhengen mellom to målinger |
| søylediagram | `plt.bar(navn, verdier)` | du sammenligner kategorier |
| liggende søyler | `plt.barh(navn, verdier)` | navnene er lange |
| sektordiagram | `plt.pie(verdier, labels=navn)` | du viser andeler av en helhet |
| histogram | `plt.hist(verdier, bins=…)` | du vil se fordelingen |

**Histogram mot søylediagram:** histogrammet teller selv hvor mange verdier som havner i hvert intervall. Søylediagrammet tegner tall du allerede har.

### Oppgave

Karakterene i en klasse er `[4, 5, 3, 6, 4, 4, 2, 5, 6, 3, 4, 5, 4, 3, 5, 6, 2, 4]`. Tegn et histogram der hver karakter får sin egen søyle.

<details><summary>Løsning</summary>

```python
import matplotlib.pyplot as plt

karakterer = [4, 5, 3, 6, 4, 4, 2, 5, 6, 3, 4, 5, 4, 3, 5, 6, 2, 4]

plt.hist(karakterer, bins=[1, 2, 3, 4, 5, 6, 7])
plt.title('Karakterfordeling')
plt.xlabel('Karakter')
plt.ylabel('Antall elever')
plt.show()
```

`bins` er grensene. Med grenser fra 1 til 7 får hver karakter sitt eget intervall.

</details>

---

## 2. Tekst, rutenett og forklaring

```python
plt.plot(maneder, oslo, color='tomato', linestyle='--', marker='o', label='Oslo')
plt.plot(maneder, bergen, color='steelblue', marker='s', label='Bergen')
plt.title('Middeltemperatur')
plt.xlabel('Måned')
plt.ylabel('Grader celsius')
plt.axhline(0, color='grey')      # vannrett hjelpelinje
plt.grid()
plt.legend()                      # trenger label= på hver kurve
plt.xlim(0, 5)                    # utsnitt av x-aksen
plt.xticks(rotation=45)           # skrå navn som ikke overlapper
plt.show()
```

**En figur uten tittel og aksetitler er ikke ferdig.** Det er det første sensor ser etter.

### Oppgave

Tegn temperaturen i Oslo `[-3.2, -2.1, 1.8, 6.4, 12.1, 16.3]` og Bergen `[1.4, 1.9, 3.6, 6.1, 10.2, 13.0]` for januar til juni i samme figur. Ta med markører, forklaring, rutenett og en linje på null grader.

<details><summary>Løsning</summary>

```python
import matplotlib.pyplot as plt

maneder = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun']
oslo = [-3.2, -2.1, 1.8, 6.4, 12.1, 16.3]
bergen = [1.4, 1.9, 3.6, 6.1, 10.2, 13.0]

plt.plot(maneder, oslo, marker='o', label='Oslo')
plt.plot(maneder, bergen, marker='s', label='Bergen')
plt.axhline(0, color='grey', linestyle='--')
plt.title('Middeltemperatur første halvår')
plt.xlabel('Måned')
plt.ylabel('Grader celsius')
plt.grid()
plt.legend()
plt.show()
```

</details>

---

## 3. Flere figurer og lagring

```python
plt.subplot(2, 1, 1)          # 2 rader, 1 kolonne, nummer 1
plt.bar(maneder, nedbor)
plt.title('Nedbør')

plt.subplot(2, 1, 2)          # nummer 2
plt.plot(maneder, temperatur)
plt.title('Temperatur')

plt.tight_layout()            # luft mellom figurene
plt.savefig('vaer.png')       # FØR show
plt.show()
```

`subplot(rader, kolonner, nummer)` kalles **før** hver figur. `savefig` etter `show` lagrer et tomt bilde.

### Oppgave

Sett temperaturen i Oslo og Bergen fra forrige oppgave i hver sin figur ved siden av hverandre, og lagre som `byer.png`.

<details><summary>Løsning</summary>

```python
import matplotlib.pyplot as plt

maneder = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun']
oslo = [-3.2, -2.1, 1.8, 6.4, 12.1, 16.3]
bergen = [1.4, 1.9, 3.6, 6.1, 10.2, 13.0]

plt.subplot(1, 2, 1)
plt.plot(maneder, oslo, marker='o')
plt.title('Oslo')
plt.xlabel('Måned')
plt.ylabel('Grader celsius')

plt.subplot(1, 2, 2)
plt.plot(maneder, bergen, marker='o')
plt.title('Bergen')
plt.xlabel('Måned')
plt.ylabel('Grader celsius')

plt.tight_layout()
plt.savefig('byer.png')
plt.show()
```

</details>

---

## 4. Lese en tekstfil

```python
maneder = []
temperaturer = []

with open('data/temperaturer.txt', encoding='utf-8') as fil:
    for linje in fil:
        deler = linje.strip().split(' ')
        maneder.append(deler[0])
        temperaturer.append(float(deler[1]))
```

`with` lukker fila av seg selv, også hvis noe krasjer. `strip()` fjerner linjeskiftet, `split()` deler linja.

**Tekst fra fil er alltid tekst.** Skal du regne, må du bruke `float()` eller `int()`.

### Oppgave

Les `data/temperaturer.txt`. Skriv ut hvor mange måneder som har minusgrader, og hvilken måned som er varmest. Regn ut med løkke.

<details><summary>Løsning</summary>

```python
maneder = []
temperaturer = []

with open('data/temperaturer.txt', encoding='utf-8') as fil:
    for linje in fil:
        deler = linje.strip().split(' ')
        maneder.append(deler[0])
        temperaturer.append(float(deler[1]))

antall_minus = 0
varmest = 0
for i in range(len(temperaturer)):
    if temperaturer[i] < 0:
        antall_minus += 1
    if temperaturer[i] > temperaturer[varmest]:
        varmest = i

print(f'{antall_minus} måneder med minusgrader')
print(f'Varmest: {maneder[varmest]} med {temperaturer[varmest]} grader')
```

Her husker løkka **plassen** til den varmeste, så både navn og temperatur kan hentes etterpå.

</details>

---

## 5. Skrive til fil

```python
with open('resultat.txt', 'w', encoding='utf-8') as fil:
    fil.write('Varme måneder\n')
    for i in range(len(maneder)):
        if temperaturer[i] > 10:
            fil.write(f'{maneder[i]}\t{temperaturer[i]}\n')
```

`'w'` lager fila på nytt hver gang. `'a'` legger til på slutten. `\n` er linjeskift, `\t` er tabulator.

### Oppgave

Lag fila `kalde_maneder.txt` med alle månedene under null grader fra forrige oppgave, én per linje. Legg så til en linje nederst med antallet, ved å åpne fila på nytt med `'a'`.

<details><summary>Løsning</summary>

```python
maneder = []
temperaturer = []

with open('data/temperaturer.txt', encoding='utf-8') as fil:
    for linje in fil:
        deler = linje.strip().split(' ')
        maneder.append(deler[0])
        temperaturer.append(float(deler[1]))

antall = 0
with open('kalde_maneder.txt', 'w', encoding='utf-8') as fil:
    for i in range(len(maneder)):
        if temperaturer[i] < 0:
            fil.write(f'{maneder[i]}\n')
            antall += 1

with open('kalde_maneder.txt', 'a', encoding='utf-8') as fil:
    fil.write(f'Til sammen {antall} måneder\n')
```

Kjører du programmet to ganger, blir fila lik begge gangene, fordi `'w'` starter på nytt.

</details>

---

## 6. CSV med csv.reader

```python
import csv

maneder = []
nedbor = []

with open('data/vaer_oslo.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)                       # hopp over overskriftene
    for rad in innhold:
        maneder.append(rad[0])
        nedbor.append(int(rad[2]))
```

`csv.reader` deler hver linje ved skilletegnet og gir en liste. `next()` henter én linje — her overskriftene, så løkka får resten.

**På eksamen:** dataanalysen leser alltid en CSV- eller JSON-fil fra forberedelsen: YouTube-kanaler (H2023), tidsbruk (V2024), befolkning (H2024), friluftsliv (V2025) og elevtall per fag (H2025). De siste fire årene skal brukeren også angi eller velge noe, for eksempel et fylke, og da trenger du `input()`.

### Oppgave

Les `data/vaer_oslo.csv`. La brukeren skrive inn en måned, og skriv ut temperaturen og nedbøren den måneden. Finnes ikke måneden, skal programmet si det.

<details><summary>Løsning</summary>

```python
import csv

vaer = {}

with open('data/vaer_oslo.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)
    for rad in innhold:
        vaer[rad[0].lower()] = [float(rad[1]), int(rad[2])]

valg = input('Hvilken måned? ').strip().lower()

if valg in vaer:
    temperatur, nedbor = vaer[valg]
    print(f'{valg}: {temperatur} grader og {nedbor} mm nedbør')
else:
    print(f'Fant ikke {valg}. Prøv for eksempel januar.')
```

En ordbok med måneden som nøkkel gjør oppslaget enkelt. `.lower()` på begge sider gjør at `Januar` og `januar` virker likt.

</details>

---

## 7. Encoding

Encoding er oppskriften tegnene ble lagret med. Du må lese med samme oppskrift.

| Ser du dette | Gjør dette |
|---|---|
| `﻿` foran første overskrift | `encoding='utf-8-sig'` — fila har vært innom Excel |
| `UnicodeDecodeError` | prøv `encoding='latin-1'` |
| `BlÃ¥bÃ¦r` i stedet for `Blåbær` | du leser en utf-8-fil som latin-1 |
| `�` i VS Code | fila er ikke utf-8 |

Start med `utf-8`. Krasjer det, prøv `latin-1`.

---

## 8. JSON

```python
import json

with open('data/skole.json', encoding='utf-8') as fil:
    skole = json.load(fil)

print(skole['klasser'][0]['navn'])
print(json.dumps(skole, indent=2, ensure_ascii=False))   # lesbar utskrift
```

JSON blir ordbøker og lister, som du kan fra før. Les én klamme om gangen, fra venstre: `skole['klasser']` er en liste, `[0]` er den første ordboka, og `['navn']` er navnet i den.

### Oppgave

Les `data/skole.json`. Skriv ut hver klasse med antall elever, regn ut hvor mange elever det er til sammen, og lag en liste med alle fagene uten gjentakelser.

<details><summary>Løsning</summary>

```python
import json

with open('data/skole.json', encoding='utf-8') as fil:
    skole = json.load(fil)

totalt = 0
alle_fag = []

for klasse in skole['klasser']:
    print(f'{klasse["navn"]:<6}{klasse["antall"]:>4} elever')
    totalt += klasse['antall']
    for fag in klasse['fag']:
        if fag not in alle_fag:
            alle_fag.append(fag)

print(f'Til sammen {totalt} elever')
print(alle_fag)
```

</details>

---

## 9. Pandas

```python
import pandas as pd

trening = pd.read_csv('data/treningsdata.csv')

print(trening.head())        # de fem første radene
print(trening.shape)         # (rader, kolonner)
print(trening.describe())    # antall, snitt, minste og største per kolonne

trening.columns = ['Varighet', 'Puls', 'Makspuls', 'Kalorier']
print(trening['Puls'].mean())

plt.plot(trening.index + 1, trening['Puls'])   # en kolonne virker som en liste
```

Pandas leser hele fila inn i én tabell, en **DataFrame**. Ti linjer med `csv.reader` blir til én.

**Regneregelen:** i pandas er `mean()`, `max()` og `min()` lov. På vanlige lister regner du fortsatt med løkke.

Tomme felt blir `NaN`, «ikke et tall». `mean()` hopper over dem.

### Oppgave

Les `data/treningsdata.csv`. Gi kolonnene norske navn, finn snittpulsen og den høyeste kaloriverdien, og tegn kalorier mot varighet som punktdiagram.

<details><summary>Løsning</summary>

```python
import matplotlib.pyplot as plt
import pandas as pd

trening = pd.read_csv('data/treningsdata.csv')
trening.columns = ['Varighet', 'Puls', 'Makspuls', 'Kalorier']

print(f'Snittpuls: {trening["Puls"].mean():.1f}')
print(f'Flest kalorier: {trening["Kalorier"].max()}')

plt.scatter(trening['Varighet'], trening['Kalorier'])
plt.title('Kalorier mot varighet')
plt.xlabel('Varighet (minutter)')
plt.ylabel('Kalorier')
plt.grid()
plt.show()
```

</details>

---

## 10. Stygge filer

Filer fra SSB har tittellinje, semikolon, `..` der tall mangler, og er ofte lagret som latin-1. **Åpne fila og se på den først.** Hver innstilling svarer til noe du ser:

```python
medier = pd.read_csv(
    'data/ssbmedier.csv',
    skiprows=1,          # hopp over tittellinja
    sep=';',             # semikolon mellom verdiene
    index_col=0,         # første kolonne blir navn på radene
    na_values='..',      # .. blir NaN
    encoding='latin-1',  # fila er ikke utf-8
)
medier.columns = range(2013, 2026)    # like mange navn som kolonner

print(medier.loc['TV'])               # en rad med navnet
print(medier.loc['Internett'].mean())
```

Hent rader med **navn** med `loc`, ikke med nummer. SSB endrer tabellene, og da flytter radene seg.

`NaN` blir **hull** i en linjegraf. Med `marker='o'` ser du også punkter som står alene.

**Innstillingene må passe fila.** Kopierer du kode fra nettet med feil innstillinger, får du ofte ingen feilmelding, bare en tom eller rar tabell.

**På eksamen:** H2024 oppgave 9 ber deg i en kommentar øverst beskrive hvordan du forberedte datasettet. Det er nettopp disse innstillingene.

### Oppgave

Les `data/ssbmedier.csv`. Tegn tiden brukt på internett, TV og radio fra 2013 til 2025 i samme figur, og finn ut hvilket av de tre som har økt mest.

<details><summary>Løsning</summary>

```python
import matplotlib.pyplot as plt
import pandas as pd

medier = pd.read_csv(
    'data/ssbmedier.csv',
    skiprows=1,
    sep=';',
    index_col=0,
    na_values='..',
    encoding='latin-1',
)
arstall = range(2013, 2026)
medier.columns = arstall

for medietype in ['Internett', 'TV', 'Radio']:
    plt.plot(arstall, medier.loc[medietype], marker='o', label=medietype)
    endring = medier.loc[medietype, 2025] - medier.loc[medietype, 2013]
    print(f'{medietype:<10}{endring:>+6.0f} minutter')

plt.title('Tid brukt på medier')
plt.xlabel('År')
plt.ylabel('Minutter per dag')
plt.legend()
plt.grid()
plt.show()
```

Internett har økt med 160 minutter. TV og radio har gått ned.

</details>

---

## 11. Filtrere og gruppere

```python
turer = pd.read_csv('data/sykkelturer.csv', sep=';')

lange = turer[turer['varighet_min'] > 30]                       # én betingelse
to_ting = turer[(turer['startstasjon'] == 'Majorstuen') & (turer['varighet_min'] > 30)]
vest = turer[turer['startstasjon'].isin(['Majorstuen', 'Bislett'])]

turer['startstasjon'].value_counts()                     # telle
turer.groupby('startstasjon')['varighet_min'].mean()     # snitt per gruppe

turer['maned'] = turer['dato'].str[5:7].astype(int)       # ny kolonne
```

Betingelsen inni klammene sjekkes for hver rad, og radene der den er sann, blir med. `&` betyr og, og **hver betingelse må stå i sin egen parentes**.

`value_counts()` er ordbok-trikset for å telle, ferdig skrevet. `groupby()` deler radene i grupper og regner ut for hver.

### Oppgave

Les `data/sykkelturer.csv`. Finn hvor mange turer som varte under fem minutter, hvilken stasjon som har flest avganger, og tegn antall turer per startstasjon som liggende søylediagram.

<details><summary>Løsning</summary>

```python
import matplotlib.pyplot as plt
import pandas as pd

turer = pd.read_csv('data/sykkelturer.csv', sep=';')

korte = turer[turer['varighet_min'] < 5]
print(f'{len(korte)} turer under fem minutter')

per_stasjon = turer['startstasjon'].value_counts()
print(f'Flest avganger: {per_stasjon.index[0]} med {per_stasjon.values[0]}')

plt.barh(per_stasjon.index, per_stasjon.values)
plt.title('Turer per startstasjon')
plt.xlabel('Antall turer')
plt.ylabel('Startstasjon')
plt.tight_layout()
plt.show()
```

`value_counts()` sorterer med den største først, så `index[0]` er stasjonen med flest.

</details>

---

## 12. Hele kjeden

Hent → rydd → regn → plott. Det er de fire stegene i nesten all databehandling, fra en skoleoppgave til en masteroppgave med gigabyte med satellittdata.

1. **Hent:** les fila med `csv.reader`, `json.load` eller `pd.read_csv`.
2. **Rydd:** riktig encoding, hopp over overskrifter, gjør tekst til tall, håndter tall som mangler.
3. **Regn:** snitt, største, telling og gruppering.
4. **Plott:** en figur med tittel, aksetitler og forklaring.

Datalabben på fagdagen gjorde det samme med objekter: hver rad i fila ble et `Sykkeltur`-objekt, og `tur.varighet` erstattet `rad[4]`.

---

## 13. Fellene som tar flest

| Felle | Hva som skjer |
|---|---|
| glemt `show()` | ingenting vises |
| `savefig` etter `show` | tomt bilde |
| figur uten aksetitler | ikke ferdig |
| `legend()` uten `label=` | tom forklaring |
| glemt `float()` på tall fra fil | `TypeError` når du regner |
| glemt `next(innhold)` | overskriftene blir med som data |
| glemt `strip()` | linjeskiftet henger med i teksten, og utskriften får blanke linjer |
| `encoding='utf-8'` på en Excel-fil | `﻿` foran første overskrift |
| `'w'` når du ville legge til | fila starter på nytt |
| `pd.read_csv` med feil `sep` | én kolonne med alt i |
| `and` i stedet for `&` i pandas | `ValueError` |
| betingelser uten parentes rundt | feil svar eller feilmelding |
| radnummer i stedet for `loc['navn']` | feil rad når tabellen endres |

---

## Filene i kapittelet

| Mappe | Uke | Innhold |
|---|---|---|
| [`3A_graftegning`](3A_graftegning) | 42 | `plot`, `scatter`, `bar`, `barh`, `pie`, `hist`, tittel og aksetitler, `legend`, `grid`, `subplot`, `savefig` |
| [`3B_filer_og_datasett`](3B_filer_og_datasett) | 43 | lese og skrive filer, `encoding`, CSV med `csv.reader`, JSON, pandas: lese, filtrere, gruppere |
| [`datalabben`](datalabben) | 44 | fagdagen: 600 bysykkelturer gjort om til objekter og analysert |

### 3A Graftegning

| Fil | Hva det er |
|---|---|
| `3A_okt1_gjennomgang.py` | diagramtypene |
| `3A_okt2_gjennomgang.py` | tekst, rutenett, akser, flere kurver, subplot og lagring |
| `3A_oppgaver.py` | oppgavene |
| `3A_losning.py` | løsningsforslag |

### 3B Filer og datasett

| Fil | Hva det er |
|---|---|
| `3B_okt1_gjennomgang.py` | tekstfiler, CSV, encoding og JSON |
| `3B_okt2_gjennomgang.py` | pandas: lese, rydde, filtrere, gruppere og tegne |
| `3B_oppgaver.py` | oppgave 1–5 hører til mandag, 6–11 til onsdag |
| `3B_losning.py` | løsningsforslag |
| `data/` | datafilene, blant annet `vaer_oslo.csv`, `skole.json`, `ssbmedier.csv` og `sykkelturer.csv` |

### Datalabben

| Fil | Hva det er |
|---|---|
| `datalabben_skall.py` | skallet dere jobbet i på fagdagen |
