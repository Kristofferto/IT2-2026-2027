# IT2 — oppsummering

Alt vi har vært gjennom så langt. Kapittel 1A til fagdagen.

Hvert tema har en typisk oppgave nederst. Prøv selv før du åpner løsningen.

[Variabler](#1-variabler-og-datatyper) ·
[Formatering](#2-utskrift-og-formatering) ·
[Operatorer](#3-operatorer) ·
[Tekst](#4-tekst-og-indeksering) ·
[Input](#5-input-fra-bruker) ·
[Betingelser](#6-valg-og-betingelser) ·
[Løkker](#7-løkker) ·
[Lister](#8-lister) ·
[2D](#9-2d-lister) ·
[Ordbøker](#10-ordbøker) ·
[Bibliotek](#11-biblioteker) ·
[Feil](#12-feil-og-feilmeldinger) ·
[Feller](#13-fellene-som-tar-flest)

---

## 1. Variabler og datatyper

```python
navn = 'Kari'      # str   tekst
alder = 19         # int   heltall
hoyde = 1.72       # float desimaltall, PUNKTUM ikke komma
elev = True        # bool  True eller False

print(type(alder))
```

`=` betyr «legg inn i», ikke «er lik». Derfor gir `alder = alder + 1` mening — og kortformen er `alder += 1`.

Navn skrives med små bokstaver og understrek: `antall_elever`. Python skiller mellom `navn` og `Navn`.

**Konvertering:** `int('42')` · `float('3.14')` · `str(42)`

### Oppgave

Lag variabler for navn, alder og høyde i meter. Skriv ut en setning som bruker alle tre, og skriv så ut datatypen til hver av dem.

<details><summary>Løsning</summary>

```python
navn = 'Kari'
alder = 19
hoyde = 1.72

print(f'{navn} er {alder} år og {hoyde} m høy.')
print(type(navn), type(alder), type(hoyde))
```

</details>

---

## 2. Utskrift og formatering

```python
print('Hei', 42)
print('2026', '01', '15', sep='-')
print('samme linje', end=' ')
```

**f-strenger** er standardverktøyet:

```python
print(f'{navn} er {alder} år, og blir {alder + 10}.')
print(f'{3.14159:.2f}')        # 3.14
print(f'[{"Vare":<12}]')       # venstre
print(f'[{"Vare":>12}]')       # høyre
print(f'[{"Vare":^12}]')       # midtstilt
print(f'[{3.14159:>10.2f}]')   # begge deler
```

Bredden kan være en variabel: `f'{navn:^{bredde}}'`

`round(x, 2)` endrer **verdien**. `f'{x:.2f}'` endrer bare **visningen**. Du vil nesten alltid ha den siste.

**Spesialtegn:** `\n` linjeskift · `\t` tabulator

### Oppgave

Skriv ut denne kvitteringen. Varenavnene skal være venstrejustert i 12 tegn, beløpene høyrejustert med to desimaler.

```
Melk               21.90
Brød               34.50
Kaffe              89.00
```

<details><summary>Løsning</summary>

```python
print(f'{"Melk":<12}{21.90:>12.2f}')
print(f'{"Brød":<12}{34.50:>12.2f}')
print(f'{"Kaffe":<12}{89.00:>12.2f}')
```

</details>

---

## 3. Operatorer

| Operator | Gjør                         | Eksempel      |
| -------- | ---------------------------- | ------------- |
| `+ - *`  | vanlig regning               | `7 * 2` → 14  |
| `/`      | divisjon, alltid desimaltall | `7 / 2` → 3.5 |
| `//`     | heltallsdivisjon             | `7 // 2` → 3  |
| `%`      | rest                         | `7 % 2` → 1   |
| `**`     | potens                       | `7 ** 2` → 49 |

På tekst gjør `+` og `*` noe helt annet: `'ha' * 3` → `hahaha`

**Sammenligning** gir `True` eller `False`: `== != < > <= >=`

**Logikk:** `and` (begge) · `or` (minst én) · `not` (snur)

### Oppgave

Et antall sekunder skal gjøres om til timer, minutter og sekunder. Med 78125 sekunder skal det bli `21:42:05`. Alle tre feltene skal ha to siffer.

<details><summary>Løsning</summary>

```python
sekunder = 78125

timer = sekunder // 3600
minutter = sekunder % 3600 // 60
sek = sekunder % 60

print(f'{timer:02d}:{minutter:02d}:{sek:02d}')
```

`//` plukker ut hele enheter, `%` gir det som er igjen.

</details>

---

## 4. Tekst og indeksering

```
  d   a   t   a   m   a   s   k   i   n
  0   1   2   3   4   5   6   7   8   9
-10  -9  -8  -7  -6  -5  -4  -3  -2  -1
```

```python
tekst[0]      # d      første
tekst[-1]     # n      siste
tekst[0:4]    # data   til, men IKKE med, 4
tekst[4:]     # maskin
tekst[::-1]   # baklengs

len(tekst)
'maskin' in tekst
tekst.upper()
tekst.lower()
tekst.strip()
tekst.replace('data', 'vaske')
tekst.split()
```

Tekst kan **ikke** endres tegn for tegn. Lister kan.

### Oppgave

Lag et brukernavn av de tre første bokstavene i fornavnet og de tre første i etternavnet, med små bokstaver. `Kari Nordmann` skal gi `karnor`.

Skriv så ut om et ord er et palindrom — altså likt baklengs. Dette skal gjøres uten `if`.

<details><summary>Løsning</summary>

```python
fornavn = 'Kari'
etternavn = 'Nordmann'

print((fornavn[0:3] + etternavn[0:3]).lower())

ord_test = 'regninger'
print(ord_test[::-1])
print(ord_test == ord_test[::-1])
```

En sammenligning gir `True` eller `False` helt av seg selv. Derfor trengs ingen `if`.

</details>

---

## 5. Input fra bruker

```python
navn = input('Hva heter du? ')
alder = int(input('Alder? '))        # int() er nødvendig
hoyde = float(input('Høyde? '))
```

`input()` gir **alltid** tekst. Skal du regne, må du konvertere.

### Oppgave

Spør brukeren om alder. Godta bare hele tall — spør på nytt til svaret duger. Skriv så ut hvor gammel brukeren er om ti år.

<details><summary>Løsning</summary>

```python
alder = input('Alder? ')

while not alder.isdigit():
    print('Skriv et helt tall.')
    alder = input('Alder? ')

alder = int(alder)
print(f'Om ti år er du {alder + 10} år.')
```

Legg merke til at `input()` står både før løkka og inni den. Uten den første har `while` ingenting å sjekke.

</details>

---

## 6. Valg og betingelser

```python
if poeng >= 90:
    karakter = 6
elif poeng >= 75:
    karakter = 5
else:
    karakter = 4
```

Kolon på slutten. Innrykket avgjør hva som hører til — fire mellomrom.

Python sjekker ovenfra og ned og stopper ved første sanne gren. **Rekkefølgen er logikken.**

```python
if alder >= 18 and har_billett:
    print('Velkommen')

print(0 < alder < 18)    # doble sammenligninger er lov
```

### Oppgave

Gjør om poeng til karakter: 90 eller mer gir 6, fra 75 gir 5, fra 60 gir 4, ellers 3. Test med 78.

<details><summary>Løsning</summary>

```python
poeng = 78

if poeng >= 90:
    karakter = 6
elif poeng >= 75:
    karakter = 5
elif poeng >= 60:
    karakter = 4
else:
    karakter = 3

print(f'{poeng} poeng gir karakteren {karakter}.')
```

Snur du rekkefølgen, treffer den første grenen nesten alltid, og resten sjekkes aldri.

</details>

---

## 7. Løkker

```python
for i in range(5):         # 0, 1, 2, 3, 4 — stopper FØR 5
for i in range(1, 6):      # 1 til 5
for i in range(0, 21, 5):  # 0, 5, 10, 15, 20
for i in range(10, 0, -1): # baklengs

for bokstav in 'datamaskin':
for vare in frukt:
for i in range(len(frukt)):
```

`while` når du ikke vet hvor mange runder:

```python
while tall <= 5:
    print(tall)
    tall += 1          # uten denne stopper den ALDRI
```

`break` hopper ut av løkka. `continue` hopper til neste runde. **Begge ser bare den nærmeste løkka rundt seg.**

**Akkumulatormønsteret** — regn ut selv:

```python
sum_tall = 0
for verdi in tall:
    sum_tall += verdi          # lag FØR løkka, oppdater INNI

storst = tall[0]
for verdi in tall:
    if verdi > storst:
        storst = verdi         # beste hittil
```

### Oppgave

Summer alle partall fra 1 til 100, og tell hvor mange de er. Svaret er 2550 og 50.

<details><summary>Løsning</summary>

```python
sum_partall = 0
antall = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_partall += i
        antall += 1

print(f'Summen er {sum_partall}, fordelt på {antall} tall.')
```

Begge variablene lages før løkka og oppdateres inni. Det er det samme mønsteret hver gang.

</details>

---

## 8. Lister

```python
frukt = ['eple', 'pære', 'banan']

frukt[0] = 'plomme'       # lister KAN endres
frukt.append('kiwi')      # bakerst
frukt.insert(1, 'melon')  # på plass 1
frukt.remove('banan')     # en bestemt verdi
sist = frukt.pop()        # ta ut den siste
del frukt[0]

len(frukt)
'eple' in frukt
frukt.count('eple')
frukt.index('pære')
frukt.sort()      # sorterer lista selv
sorted(frukt)     # lager en NY sortert liste

'a b c'.split()   # tekst  -> liste
', '.join(frukt)  # liste  -> tekst
```

**Kopieringsfella:** `b = a` lager ikke en kopi, bare et nytt navn på samme liste. Bruk `b = a.copy()`.

### Oppgave

Du har prisene `[21.90, 34.50, 89.00, 12.50]`. Legg til 45.00, fjern 12.50, og regn så ut totalsum, snitt og dyreste vare — med løkke, ikke med ferdige funksjoner.

<details><summary>Løsning</summary>

```python
priser = [21.90, 34.50, 89.00, 12.50]

priser.append(45.00)
priser.remove(12.50)

sum_priser = 0
for pris in priser:
    sum_priser += pris

dyrest = priser[0]
for pris in priser:
    if pris > dyrest:
        dyrest = pris

print(f'Sum:     {sum_priser:>8.2f}')
print(f'Snitt:   {sum_priser / len(priser):>8.2f}')
print(f'Dyreste: {dyrest:>8.2f}')
```

</details>

---

## 9. 2D-lister

```python
brett = [
    [1, 2, 3],
    [4, 5, 6],
]

brett[1]        # hele rad 1
brett[1][2]     # rad 1, kolonne 2 — RAD FØRST

len(brett)      # antall rader
len(brett[0])   # antall kolonner
```

```python
for rad in brett:
    for verdi in rad:
        print(f'{verdi:>4}', end='')
    print()
```

Bygge et brett — `rad = []` må stå **inne** i den ytre løkka:

```python
rutenett = []
for r in range(3):
    rad = []
    for k in range(4):
        rad.append(0)
    rutenett.append(rad)
```

### Oppgave

Bygg en 2D-liste på 3 rader og 4 kolonner der hvert felt er raden ganget med kolonnen. Skriv den ut som et rutenett med tallene rett under hverandre.

<details><summary>Løsning</summary>

```python
brett = []

for r in range(1, 4):
    rad = []
    for k in range(1, 5):
        rad.append(r * k)
    brett.append(rad)

for rad in brett:
    for verdi in rad:
        print(f'{verdi:>4}', end='')
    print()
```

```
   1   2   3   4
   2   4   6   8
   3   6   9  12
```

`end=''` holder raden på én linje. Den tomme `print()` avslutter den.

</details>

---

## 10. Ordbøker

```python
karakterer = {'Kari': 5, 'Ola': 4}

karakterer['Kari']              # slå opp
karakterer['Mia'] = 3           # legg til
del karakterer['Ola']           # slett
'Kari' in karakterer            # sjekker NØKLER
karakterer.get('Finnes ikke', 0)

for navn, tall in karakterer.items():
    print(f'{navn:<8}{tall}')
```

Verdien kan være en liste: `{'Kari': [5, 4, 6]}`

**Liste eller ordbok?** Liste når rekkefølgen betyr noe. Ordbok når du slår opp på et navn.

### Oppgave

Tell hvor mange ganger hver bokstav forekommer i `informasjonsteknologi`, og finn den hyppigste. Du får ikke bruke ferdige funksjoner.

<details><summary>Løsning</summary>

```python
tekst = 'informasjonsteknologi'
antall = {}

for bokstav in tekst:
    if bokstav in antall:
        antall[bokstav] += 1
    else:
        antall[bokstav] = 1

hyppigst = ''
flest = 0

for bokstav, tall in antall.items():
    if tall > flest:
        hyppigst = bokstav
        flest = tall

print(f'Hyppigst: {hyppigst} ({flest} ganger)')
```

Du vet ikke på forhånd hvilke nøkler du trenger — de lages underveis. Det er ordbokas beste triks.

</details>

---

## 11. Biblioteker

```python
import numpy as np
import random

np.sqrt(2)
np.pi
np.sin(np.radians(30))
random.randint(1, 6)
random.choice(['stein', 'saks', 'papir'])
```

`import` skal stå øverst i fila.

### Oppgave

Kast en terning 1000 ganger, lagre kastene i en liste, og regn ut snittet. Ligger det nær 3,5?

<details><summary>Løsning</summary>

```python
import random

kast = []

for i in range(1000):
    kast.append(random.randint(1, 6))

sum_kast = 0
for verdi in kast:
    sum_kast += verdi

print(f'Snitt: {sum_kast / len(kast):.2f}')
```

Snittet av 1 til 6 er 3,5. Med 1000 kast lander du nær, men sjelden nøyaktig.

</details>

---

## 12. Feil og feilmeldinger

| Type          | Når                        | Melding                                              |
| ------------- | -------------------------- | ---------------------------------------------------- |
| Syntaksfeil   | starter ikke               | `SyntaxError`                                        |
| Kjøretidsfeil | stopper underveis          | `TypeError`, `ValueError`, `NameError`, `IndexError` |
| Logisk feil   | kjører, men svaret er feil | ingen melding                                        |

1. Les **nederste** linje først. Der står feiltypen.
2. Se på linjenummeret — og på linja over.
3. `print()` ut verdien og typen når du er usikker.

### Oppgave

Fire feil i fem linjer. Finn dem alle.

```python
import numpy as np

Radius = input('Oppgi radius: ')
areal = np.pi * radius ** 2
print('Arealet er ' + areal + ' kvadratmeter)
```

<details><summary>Løsning</summary>

1. `Radius` med stor R defineres, `radius` med liten brukes → `NameError`
2. `input()` gir tekst og kan ikke opphøyes i andre → `TypeError`, mangler `float()`
3. `'...' + areal` limer tekst og tall → `TypeError`
4. Manglende anførselstegn på slutten → `SyntaxError`

```python
import numpy as np

radius = float(input('Oppgi radius: '))
areal = np.pi * radius**2
print(f'Arealet er {areal:.2f} kvadratmeter')
```

</details>

---

## 13. Fellene som tar flest

| Felle                  | Hva som skjer                         |
| ---------------------- | ------------------------------------- |
| `=` mot `==`           | tilordning i stedet for sammenligning |
| `input()` uten `int()` | `'19' + 1` → TypeError                |
| `range(5)`             | gir 0–4, ikke 1–5                     |
| `tekst[0:4]`           | tar ikke med 4                        |
| Rekkefølge i `elif`    | en gren nås aldri                     |
| `while` uten `+= 1`    | evig løkke — Ctrl + C                 |
| `b = a` på lister      | ingen kopi                            |
| `0.1 + 0.2 == 0.3`     | `False` — bruk `np.isclose`           |
| `'Kari' == 'kari'`     | `False` — bruk `.lower()`             |
| `brett[-1]` på kanten  | ingen feilmelding, bare feil svar     |
