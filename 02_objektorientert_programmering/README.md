# 2 Objektorientert programmering — oppsummering

Klasser og objekter (2A, uke 44–45), UML (2B, uke 46), flytskjema (uke 47) og systemutvikling (2B, uke 48). Heldagsprøve før jul: del 1 onsdag 02.12 og del 2 fredag 11.12. Den dekker alt fram til da, og er bygd som eksamen.

Alle ordene fra kapittelet står forklart i [`ordliste.md`](ordliste.md). Den er lov å bruke på prøver.

Hvert tema har en typisk oppgave nederst. Prøv selv før du åpner løsningen. **På eksamen** viser hvilke eksamensoppgaver som tester temaet.

Filene fra timene står nederst, under [Filene i kapittelet](#filene-i-kapittelet).

[Klasser](#1-klasser-og-objekter) ·
[Metoder](#2-metoder-__str__-og-standardverdier) ·
[Innkapsling](#3-innkapsling-feil-og-testprogram) ·
[Klassevariabler](#4-klassevariabler) ·
[Samlinger](#5-samlinger-av-objekter) ·
[Pseudokode](#6-pseudokode) ·
[Arv](#7-arv) ·
[Fire ord](#8-fire-ord-fra-eksamen) ·
[Feller](#9-fellene-som-tar-flest)

---

## 1. Klasser og objekter

```python
class Bil:
    def __init__(self, merke, kilometer):
        self.merke = merke
        self.kilometer = kilometer


bil1 = Bil('Volvo', 120000)    # ett objekt
bil2 = Bil('Tesla', 45000)     # et annet objekt

bil1.kilometer = 130000
print(bil1.kilometer, bil2.kilometer)    # bare bil1 endret seg
```

En **klasse** er oppskriften. Et **objekt** er én ting laget fra oppskriften.

`__init__` er **konstruktøren**. Den kjører av seg selv når objektet lages, og gir det **attributtene** sine.

`self` betyr «dette objektet». Det står først i hver metode, men sendes ikke med når du kaller den. Hvert objekt har sine egne verdier.

### Oppgave

Lag klassen `Elev` med fornavn, etternavn og trinn. Lag tre elever, endre trinnet på den første, og skriv ut trinnet til alle tre.

<details><summary>Løsning</summary>

```python
class Elev:
    def __init__(self, fornavn, etternavn, trinn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.trinn = trinn


elever = [Elev('Kari', 'Nordmann', 2), Elev('Ola', 'Hansen', 2), Elev('Ali', 'Khan', 3)]
elever[0].trinn = 3

for elev in elever:
    print(elev.fornavn, elev.trinn)
```

Bare Kari fikk nytt trinn. De andre objektene er urørt.

</details>

---

## 2. Metoder, `__str__` og standardverdier

```python
class Bil:
    """Representerer en bil med merke og kilometerstand."""

    def __init__(self, merke, kilometer=0):      # standardverdi
        self.merke = merke
        self.kilometer = kilometer

    def kjor(self, distanse):                    # metode som endrer objektet
        self.kilometer += distanse

    def trenger_service(self):                   # metode som returnerer
        return self.kilometer > 150000

    def __str__(self):                           # det print viser
        return f'{self.merke} med {self.kilometer} km'


bil = Bil('Tesla')
bil.kjor(2000)
print(bil)                    # Tesla med 2000 km
print(bil.trenger_service())  # False
```

En **metode** er en funksjon som hører til klassen. Den kan bruke og endre attributtene gjennom `self`.

Uten `__str__` skriver `print(bil)` noe slikt som `<__main__.Bil object at 0x7f8b…>`. `__str__` skal **returnere** teksten, ikke skrive den ut.

### Oppgave

Lag klassen `Terning` med et antall sider, som standard 6. Metoden `kast()` skal returnere et tilfeldig tall og huske hvor mange ganger terningen er kastet. Lag en `__str__` som viser antall sider og antall kast.

<details><summary>Løsning</summary>

```python
import random


class Terning:
    def __init__(self, sider=6):
        self.sider = sider
        self.antall_kast = 0

    def kast(self):
        self.antall_kast += 1
        return random.randint(1, self.sider)

    def __str__(self):
        return f'Terning med {self.sider} sider, kastet {self.antall_kast} ganger'


vanlig = Terning()
d20 = Terning(20)
print(vanlig.kast(), d20.kast(), d20.kast())
print(vanlig)
print(d20)
```

</details>

---

## 3. Innkapsling, feil og testprogram

```python
class Batteri:
    """Et batteri med en kapasitet og et energinivå."""

    def __init__(self, batteri_id, energikapasitet):
        self._batteri_id = batteri_id
        self._energikapasitet = energikapasitet
        self._energiniva = 0.0

    def lad_opp(self, energi):
        if energi < 0:
            raise ValueError('Energimengden kan ikke være negativ.')
        self._energiniva += energi
        if self._energiniva > self._energikapasitet:
            self._energiniva = self._energikapasitet

    def vis_energiniva(self):
        return self._energiniva


batteri = Batteri('BAT001', 100.0)
batteri.lad_opp(50.0)

try:
    batteri.lad_opp(-10.0)
except ValueError as feil:
    print('Feil fanget:', feil)
```

**Understrek** foran et attributt betyr «ikke rør denne utenfra». Python hindrer deg ikke, men det er en avtale. Alle endringer går gjennom metodene, som sjekker verdien. Det heter **innkapsling**.

`raise ValueError('…')` stopper programmet med din egen feilmelding. `try`/`except` fanger feilen, så programmet kan fortsette.

Et **testprogram** lager objekter, kaller metodene og viser at både vanlige verdier og feil blir håndtert riktig.

**På eksamen:** klasseoppgaven er nesten alltid lik denne. H2024 oppgave 6 er nettopp `Batteri`, V2024 oppgave 6 er en kalkulator, V2025 oppgave 6 er et bibliotek og H2025 oppgave 5 er en digitalklokke. Alle ber om testprogram og håndtering av feil og unntak.

### Oppgave

Lag klassen `Konto` med eier og `_saldo`. `sett_inn` og `ta_ut` skal kaste `ValueError` ved negativt beløp, og `ta_ut` også når det ikke er dekning. Skriv et testprogram som viser at alle tre feilene fanges.

<details><summary>Løsning</summary>

```python
class Konto:
    def __init__(self, eier, saldo=0):
        self.eier = eier
        self._saldo = saldo

    def sett_inn(self, belop):
        if belop < 0:
            raise ValueError('Beløpet kan ikke være negativt.')
        self._saldo += belop

    def ta_ut(self, belop):
        if belop < 0:
            raise ValueError('Beløpet kan ikke være negativt.')
        if belop > self._saldo:
            raise ValueError('Ikke dekning.')
        self._saldo -= belop

    def vis_saldo(self):
        return self._saldo


konto = Konto('Kari', 500)
konto.sett_inn(250)
konto.ta_ut(100)
print(konto.vis_saldo())  # 650

for handling, belop in [('inn', -5), ('ut', -5), ('ut', 10000)]:
    try:
        if handling == 'inn':
            konto.sett_inn(belop)
        else:
            konto.ta_ut(belop)
    except ValueError as feil:
        print(f'{handling} {belop}: {feil}')
```

</details>

---

## 4. Klassevariabler

```python
class Medlem:
    medlemsnummer = 1                                  # felles for ALLE objekter

    def __init__(self, navn):
        self.navn = navn
        self.medlemsnummer = Medlem.medlemsnummer      # dette objektet får nummeret
        Medlem.medlemsnummer += 1                      # så teller vi opp


a = Medlem('Kari')
b = Medlem('Ola')
print(a.medlemsnummer, b.medlemsnummer)   # 1 2
print(Medlem.medlemsnummer)               # 3, neste ledige
```

`Medlem.medlemsnummer` er felles for klassen og teller oppover. `self.medlemsnummer` tilhører ett objekt og står fast.

### Oppgave

Gi `Elev` fra oppgave 1 et elevnummer som telles opp med en klassevariabel. Lag fem elever og skriv ut nummeret til hver. Hva er `Elev.elevnummer` etterpå, og hvorfor?

<details><summary>Løsning</summary>

```python
class Elev:
    elevnummer = 1

    def __init__(self, fornavn):
        self.fornavn = fornavn
        self.elevnummer = Elev.elevnummer
        Elev.elevnummer += 1


elever = []
for navn in ['Kari', 'Ola', 'Ali', 'Nora', 'Per']:
    elever.append(Elev(navn))

for elev in elever:
    print(elev.elevnummer, elev.fornavn)

print(Elev.elevnummer)  # 6
```

Fem elever har fått 1 til 5. Klassevariabelen står på nummeret neste elev skal få.

</details>

---

## 5. Samlinger av objekter

```python
def finn_medlem(nummer, liste):
    """Returnerer medlemmet med dette nummeret, eller None."""
    for medlem in liste:
        if medlem.medlemsnummer == nummer:
            return medlem
    return None              # ETTER løkka, ellers sjekkes bare den første
```

En liste med objekter oppfører seg som alle andre lister. Det nye er at du skriver `medlem.navn` i stedet for `rad[0]`.

`print(liste)` viser objektadresser, fordi `print` på en liste ikke bruker `__str__`. Bruk en løkke.

**Beste hittil med objekter:** ta vare på hele objektet, ikke bare tallet. Da har du både navn og verdi etterpå.

```python
kaldest = maalinger[0]
for m in maalinger:
    if m.temperatur < kaldest.temperatur:
        kaldest = m
print(kaldest)
```

**Fra fil til objekter:** lag ett objekt per rad når du leser fila.

```python
turer = []
with open('data/sykkelturer.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)
    for rad in innhold:
        turer.append(Sykkeltur(rad[0], rad[1], rad[2], rad[3], float(rad[4])))
```

`tur.varighet` er lesbart. `rad[4]` er det ikke. Det er hele gevinsten.

### Oppgave

Lag klassen `Maaling` med sted og temperatur. Lag fem målinger i en liste, og finn snittemperaturen og den kaldeste målingen med én løkke.

<details><summary>Løsning</summary>

```python
class Maaling:
    def __init__(self, sted, temperatur):
        self.sted = sted
        self.temperatur = temperatur

    def __str__(self):
        return f'{self.sted}: {self.temperatur} grader'


maalinger = [
    Maaling('Oslo', -3.2),
    Maaling('Bergen', 1.4),
    Maaling('Tromsø', -8.7),
    Maaling('Kristiansand', 2.1),
    Maaling('Bodø', -4.4),
]

sum_temp = 0
kaldest = maalinger[0]
for m in maalinger:
    sum_temp += m.temperatur
    if m.temperatur < kaldest.temperatur:
        kaldest = m

print(f'Snitt: {sum_temp / len(maalinger):.1f}')
print(f'Kaldest: {kaldest}')
```

</details>

---

## 6. Pseudokode

Eksamen skriver ofte algoritmer som pseudokode. Det er ikke Python, men en avtale om hvordan man beskriver en algoritme med ord.

```
FUNCTION finnMedlem(nummer, liste)
    FOR hvert medlem i liste
        IF medlem.medlemsnummer EQUAL TO nummer
            RETURN medlem
        ENDIF
    ENDFOR
    RETURN ingenting
ENDFUNCTION
```

| Pseudokode | Python |
|---|---|
| `SET x TO 5` | `x = 5` |
| `DISPLAY x` | `print(x)` |
| `READ x` | `x = input()` |
| `IF … ELSE IF … ELSE … ENDIF` | `if … elif … else` |
| `FOR hvert … ENDFOR` | `for` |
| `WHILE … ENDWHILE` | `while` |
| `REPEAT … UNTIL betingelse` | `while True` med `break` |
| `FUNCTION … ENDFUNCTION` | `def` |
| `RETURN` | `return` |
| `CALL x.metode()` | `x.metode()` |
| `EQUAL TO`, `NOT EQUAL TO` | `==`, `!=` |
| `GREATER THAN`, `LESSER THAN` | `>`, `<` |
| `INCREMENT i`, `DECREMENT i` | `i += 1`, `i -= 1` |

Innrykket viser hva som hører til hva. `END`-ordene sier hvor en blokk slutter.

**På eksamen:** står pseudokode på alle eksamenene fra V2023 til H2025. De spør hva den viser, ber deg forklare algoritmen, sortere linjer i riktig rekkefølge, fullføre den, eller lage et program fra den.

### Oppgave

Eksamen H2024, oppgave 3. Hva vil vises som resultat? Svar uten å kjøre koden, og lag så programmet i Python for å sjekke.

```
FUNCTION beregn(n):
   SET s TO 0
   FOR hvert tall i fra og med 1 til og med n
      IF i % 2 EQUAL TO 0
         SET s TO s + i
      ELSE
         SET s TO s - i
      ENDIF
   ENDFOR
   RETURN s
ENDFUNCTION

DISPLAY beregn(7)
```

<details><summary>Løsning</summary>

Svaret er −4: −1 + 2 − 3 + 4 − 5 + 6 − 7.

```python
def beregn(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s += i
        else:
            s -= i
    return s


print(beregn(7))
```

«Fra og med 1 til og med n» blir `range(1, n + 1)`, fordi `range` stopper før sluttverdien.

</details>

---

## 7. Arv

```python
class Dyr:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def spis(self):
        print(f'{self.navn} spiser.')


class Hund(Dyr):                              # Hund arver fra Dyr
    def __init__(self, navn, alder, rase):
        super().__init__(navn, alder)         # la Dyr gjøre sin del
        self.rase = rase

    def bjeff(self):
        print(f'{self.navn} sier voff.')


class Fisk(Dyr):
    def spis(self):                           # overstyrer spis fra Dyr
        print(f'{self.navn} spiser under vann.')


for d in [Hund('Rex', 4, 'collie'), Fisk('Nemo', 1)]:
    d.spis()
```

`Dyr` er **superklassen**, `Hund` og `Fisk` er **subklasser**. Subklassen får alt superklassen har, og legger til eller overstyrer.

`super().__init__(…)` kjører superklassens konstruktør. Glemmer du den, mangler attributtene, og feilen kommer først når de brukes.

Arv passer når du kan si «en X **er** en Y». En hund er et dyr. En sirkel er ikke et rektangel.

### Oppgave

Lag `Kjoretoy` med merke, kilometer og `kjor(distanse)`. Lag `Elbil` som arver, har batterikapasitet, og har en egen `kjor` som også trekker 0,2 kWh per km fra batteriet. Kjør begge 100 km i én løkke.

<details><summary>Løsning</summary>

```python
class Kjoretoy:
    def __init__(self, merke, kilometer=0):
        self.merke = merke
        self.kilometer = kilometer

    def kjor(self, distanse):
        self.kilometer += distanse

    def __str__(self):
        return f'{self.merke}: {self.kilometer} km'


class Elbil(Kjoretoy):
    def __init__(self, merke, batteri, kilometer=0):
        super().__init__(merke, kilometer)
        self.batteri = batteri

    def kjor(self, distanse):
        super().kjor(distanse)
        self.batteri -= distanse * 0.2

    def __str__(self):
        return f'{self.merke}: {self.kilometer} km, {self.batteri:.1f} kWh igjen'


for bil in [Kjoretoy('Volvo', 120000), Elbil('Tesla', 75)]:
    bil.kjor(100)
    print(bil)
```

`super().kjor(distanse)` gjenbruker kilometertellingen fra `Kjoretoy`. Elbilen legger bare til det nye.

</details>

---

## 8. Fire ord fra eksamen

| Ord | Betyr | Hos oss |
|---|---|---|
| **Arv** | en klasse bygger på en annen og gjenbruker koden | `class Hund(Dyr)` |
| **Polymorfisme** | samme metodekall gjør forskjellige ting avhengig av objektet | `d.spis()` i løkka over dyr |
| **Innkapsling** | dataene er pakket inn i objektet og endres bare gjennom metodene | `self._saldo` og `sett_inn` |
| **Abstraksjon** | du bruker hva et objekt kan, uten å tenke på hvordan | `kvadrat.areal()` |

Innkapsling og abstraksjon ligner. Innkapsling handler om å **beskytte dataene**. Abstraksjon handler om å **skjule detaljene** i hvordan noe gjøres.

Om to klasser i et arvetre: subklassen er en **spesialisering** av superklassen, og superklassen er en **generalisering** av subklassene.

**På eksamen:** flervalg om disse ordene på fem av seks eksamener: H2023 oppgave 3, V2024 oppgave 1–2, H2024 oppgave 1, V2025 oppgave 3–4 og H2025 oppgave 1.

### Oppgave

Eksamen V2025, oppgave 3. En utvikler samler felles metoder i en superklasse, men beholder spesialiserte varianter av metodene i subklassene. Hvilket prinsipp gjør at metodene kan ha samme navn i superklassen og subklassene, og likevel kalles riktig på objektene? Abstraksjon, polymorfisme, innkapsling eller arv?

<details><summary>Løsning</summary>

**Polymorfisme.** Arv er det som gjør at subklassene får metodene, men det at riktig variant kalles på hvert objekt, er polymorfisme. Tenk på `Fisk` som overstyrer `spis`: `d.spis()` gjør forskjellige ting for en hund og en fisk.

</details>

---

## 9. Fellene som tar flest

| Felle | Hva som skjer |
|---|---|
| glemt `self` som første parameter | `takes 1 positional argument but 2 were given` |
| `self` i kallet: `bil.kjor(self, 100)` | `NameError` |
| `merke = merke` uten `self.` | attributtet finnes ikke etterpå |
| `_init_` med én understrek | konstruktøren kjører aldri |
| `print` i `__str__` | `TypeError: __str__ returned non-string` |
| `print(liste)` med objekter | objektadresser — bruk løkke |
| `return None` inne i løkka | bare det første elementet sjekkes |
| `self.nummer += 1` i stedet for `Klasse.nummer += 1` | klassevariabelen telles aldri opp |
| glemt `super().__init__` | attributtene fra superklassen mangler |
| `super().__init__(self, navn)` | `self` sendes to ganger, `TypeError` |

---

## Filene i kapittelet

| Mappe | Uke | Innhold |
|---|---|---|
| [`2A_klasser_og_objekter`](2A_klasser_og_objekter) | 44–45 | klasser, metoder, innkapsling, klassevariabler, samlinger, pseudokode, arv |

### 2A Klasser og objekter

| Fil | Hva det er |
|---|---|
| `2A_okt1_gjennomgang.py` | klasser og objekter, fra to variabler til en hel `Batteri`-klasse |
| `2A_okt2_gjennomgang.py` | klassevariabler og samlinger av objekter, med bysykkelturene, og pseudokode |
| `2A_okt3_gjennomgang.py` | arv, og de fire ordene arv, polymorfisme, innkapsling og abstraksjon |
| `2A_oppgaver.py` | oppgavene, med hvilke som hører til hvilken økt. Oppgavene merket EKSAMEN er fra tidligere eksamener |
| `data/` | `sykkelturer.csv` |
