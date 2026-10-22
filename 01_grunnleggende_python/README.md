# 1 Grunnleggende Python — oppsummering

Alt fra kapittel 1A til 1F, uke 36–41: tall og tekst, valg, løkker, lister, ordbøker og funksjoner.

Hvert tema har en typisk oppgave nederst. Prøv selv før du åpner løsningen. **På eksamen** viser hvilke eksamensoppgaver som tester temaet.

Filene fra timene står nederst, under [Filene i kapittelet](#filene-i-kapittelet).

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
[Funksjoner](#11-funksjoner) ·
[Testing](#12-teste-med-assert) ·
[Bibliotek](#13-biblioteker) ·
[Feil](#14-feil-og-feilmeldinger) ·
[Feller](#15-fellene-som-tar-flest)

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

**På eksamen:** `%` og `//` til å plukke ut sifre. H2024 oppgave 5 snur sifrene i et tall og sjekker om det er et palindromtall.

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

**På eksamen:** V2025 oppgave 5 forskyver hver bokstav i en tekst n plasser i alfabetet.

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

**På eksamen:** V2023 oppgave 5 (største av tre tall) og H2024 oppgave 4 (temperaturmeldinger) ber deg sortere linjer med pseudokode. V2023 oppgave 6 er karakter fra poengsum, med en testplan som avslører feil grenser.

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

**På eksamen:** nesten hver eksamen spør hva en løkke skriver ut: V2023 oppgave 2, V2024 oppgave 3, H2024 oppgave 3 og H2025 oppgave 3.

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

**På eksamen:** H2023 oppgave 6 finner det nest største tallet, H2023 oppgave 7 sorterer en liste, og V2024 oppgave 5 lager Fibonacci-tallene i en liste.

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

**Nøstede ordbøker** — en ordbok inni en ordbok:

```python
skole = {
    'Kari': {'matte': 5, 'norsk': 4},
    'Ola': {'matte': 3, 'norsk': 4},
}

skole['Kari']['matte']          # ytterste nøkkel FØRST, som brett[rad][kolonne]
skole['Kari']['it2'] = 6        # nytt fag for Kari
skole['Mia'] = {}               # ny elev må lages før du legger noe inn
skole['Mia']['matte'] = 5

for navn, fag in skole.items():
    for fagnavn, karakter in fag.items():
        print(f'{navn:<8}{fagnavn:<8}{karakter}')
```

Trenger du to opplysninger for å finne fram — både navn og fag — trenger du to nivåer.

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

### Oppgave 2

Lag en nøstet ordbok med tre elever og karakterene deres i matte og norsk. Regn ut snittet for hver elev, og snittet i matte for hele klassen.

<details><summary>Løsning</summary>

```python
skole = {
    'Kari': {'matte': 5, 'norsk': 4},
    'Ola': {'matte': 3, 'norsk': 4},
    'Ali': {'matte': 6, 'norsk': 5},
}

for navn, fag in skole.items():
    sum_karakterer = 0
    antall = 0
    for karakter in fag.values():
        sum_karakterer += karakter
        antall += 1
    print(f'{navn:<6}{sum_karakterer / antall:.1f}')

sum_matte = 0
for fag in skole.values():
    sum_matte += fag['matte']

print(f'Matte: {sum_matte / len(skole):.2f}')
```

Den ytre løkka går gjennom elevene, den indre gjennom fagene til én elev.

</details>

---

## 11. Funksjoner

```python
def areal(bredde, hoyde):
    """Returnerer arealet av et rektangel."""
    return bredde * hoyde


print(areal(3, 4))                   # 12
print(areal(hoyde=4, bredde=3))      # navngitte argumenter, fri rekkefølge
```

`def` lager funksjonen. Ingenting skjer før du **kaller** den. Docstringen med tre anførselstegn sier hva funksjonen gjør, og vises når du holder musa over navnet i VS Code.

**Standardverdier** står sist: `def pris_med_mva(pris, sats=0.25):`

**`return` mot `print`:** `return` sender svaret ut så du kan regne videre med det. En funksjon uten `return` gir `None`. `return` avslutter funksjonen med én gang.

```python
def min_og_maks(liste):
    minst = liste[0]
    storst = liste[0]
    for verdi in liste:
        if verdi < minst:
            minst = verdi
        if verdi > storst:
            storst = verdi
    return minst, storst          # to verdier ut


lav, hoy = min_og_maks([12, 4, 19, 7])
```

**Rekkevidde:** en variabel laget inne i en funksjon finnes bare der. Vil du ha verdien ut, må du returnere den. Tall sendes inn som kopi, men en liste sendes inn som seg selv — `liste.append()` inne i funksjonen endrer originalen.

**Egne biblioteker:** en vanlig `.py`-fil med funksjoner kan importeres fra en annen fil i samme mappe:

```python
import minmatte                  # minmatte.py i samme mappe
print(minmatte.snitt([4, 8, 6]))

from minmatte import minste      # da slipper du å skrive minmatte foran
```

Testkode i biblioteket legges under `if __name__ == '__main__':`, så den ikke kjører når fila importeres.

**På eksamen:** heter det `FUNCTION`, `RETURN` og `ENDFUNCTION` i pseudokoden. V2023 oppgave 3 bruker en funksjon for trekanttall, H2025 oppgave 4 og V2025 oppgave 5 ber deg skrive en funksjon fra en algoritme.

### Oppgave

Skriv `snitt_uten_laveste(tall)` som fjerner den laveste verdien og returnerer snittet av resten. Finn den laveste med løkke. `[4, 2, 8, 6]` skal gi 6.0.

<details><summary>Løsning</summary>

```python
def snitt_uten_laveste(tall):
    """Returnerer snittet når den laveste verdien er fjernet."""
    laveste = tall[0]
    for t in tall:
        if t < laveste:
            laveste = t

    resten = tall.copy()
    resten.remove(laveste)

    sum_tall = 0
    for t in resten:
        sum_tall += t
    return sum_tall / len(resten)


print(snitt_uten_laveste([4, 2, 8, 6]))
```

`tall.copy()` gjør at lista som ble sendt inn, ikke endres.

</details>

---

## 12. Teste med assert

```python
def tell_giftige(giftige, plukket):
    teller = 0
    for sopp in plukket:
        if sopp in giftige:
            teller += 1
    return teller


assert tell_giftige(['fluesopp'], ['kantarell', 'fluesopp']) == 1
assert tell_giftige([], ['fluesopp']) == 0      # kanttilfelle
print('Alle testene gikk gjennom')
```

`assert` sier: dette **må** være sant. Er det ikke det, stopper programmet med `AssertionError`.

Feilene bor i **kanttilfellene**: tom liste, ett element, to som er like store, det største tallet som er lov. En funksjon som består eksempelet i oppgaven, kan fortsatt være feil.

**På eksamen:** heter det et **testprogram**. Klasseoppgaven ber nesten hvert år om et testprogram som viser at koden virker, og som finner feil og unntak.

### Oppgave

Skriv `er_primtall(n)` som returnerer `True` eller `False`. Skriv fem `assert`-linjer som tester den, og ta med minst to kanttilfeller.

<details><summary>Løsning</summary>

```python
def er_primtall(n):
    """Returnerer True hvis n er et primtall."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


assert er_primtall(7)
assert not er_primtall(9)
assert er_primtall(2)          # det minste primtallet
assert not er_primtall(1)      # kanttilfelle
assert not er_primtall(0)      # kanttilfelle
print('Alle testene gikk gjennom')
```

`return False` inne i løkka avslutter så fort en divisor er funnet. `return True` står etter løkka, fordi vi må ha sjekket alle før vi vet svaret.

</details>

---

## 13. Biblioteker

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

## 14. Feil og feilmeldinger

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

## 15. Fellene som tar flest

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
| `print` i stedet for `return` | funksjonen gir `None`          |
| `return` inne i løkka  | funksjonen stopper etter første runde |
| `skole['Mia']['matte'] = 5` | `KeyError` — lag `skole['Mia'] = {}` først |

---

## Filene i kapittelet

Løsningsforslagene i dette kapittelet heter `lf_…py`.

| Mappe | Uke | Filer |
|---|---|---|
| [`1A_tall_og_tekster`](1A_tall_og_tekster) | 36 | `grunnleggende_python_okt1.py` og `_okt2.py` fra timene, `ekstra_oppgaver_uke36.py` |
| [`1B_valg_og_betingelser`](1B_valg_og_betingelser) | 37 | `valg_betingelser.py` fra timen, `utfordringer_valg_betingelser.py` |
| [`1C_lokker`](1C_lokker) | 37 | `lokker.py` fra timen, `utfordringer_lokker.py` |
| [`1D_1E_lister_og_ordboker`](1D_1E_lister_og_ordboker) | 38 | `lister_ordboker.py`, `lister_ordboker_2.py` og `ordboker_nostede.py` fra timene, oppgaver, utfordringer, konkurranse og prosjekt |
| [`1F_funksjoner`](1F_funksjoner) | 41 | `funksjoner.py` fra timen, `minmatte.py` (eget bibliotek), `funksjoner_oppgaver.py`, `repetisjon_oppgaver.py` med `repetisjon_tester.py` |

Testing med `assert` og MiniOlympiaden ligger i [`07_repetisjon_og_eksamen/miniolympiaden`](../07_repetisjon_og_eksamen/miniolympiaden).
