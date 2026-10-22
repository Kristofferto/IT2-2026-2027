# 2 Objektorientert programmering — oppsummering

Klasser og objekter (2A, uke 44–45), UML (2B, uke 46) og systemutvikling (2B, uke 47–48).

Hvert tema har en typisk oppgave nederst. Prøv selv før du åpner løsningen. **På eksamen** viser hvilke eksamensoppgaver som tester temaet.

Filene fra timene står nederst, under [Filene i kapittelet](#filene-i-kapittelet).

[Klasser](#1-klasser-og-objekter) ·
[Metoder](#2-metoder-__str__-og-standardverdier) ·
[Innkapsling](#3-innkapsling-feil-og-testprogram) ·
[Feller](#4-fellene-som-tar-flest)

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

## 4. Fellene som tar flest

| Felle | Hva som skjer |
|---|---|
| glemt `self` som første parameter | `takes 1 positional argument but 2 were given` |
| `self` i kallet: `bil.kjor(self, 100)` | `NameError` |
| `merke = merke` uten `self.` | attributtet finnes ikke etterpå |
| `_init_` med én understrek | konstruktøren kjører aldri |
| `print` i `__str__` | `TypeError: __str__ returned non-string` |

---

## Filene i kapittelet

| Mappe | Uke | Innhold |
|---|---|---|
| [`2A_klasser_og_objekter`](2A_klasser_og_objekter) | 44–45 | klasser, metoder, innkapsling, klassevariabler, samlinger, pseudokode, arv |

### 2A Klasser og objekter

| Fil | Hva det er |
|---|---|
| `2A_okt1_gjennomgang.py` | klasser og objekter, fra to variabler til en hel `Batteri`-klasse |
| `2A_oppgaver.py` | oppgavene, med hvilke som hører til hvilken økt. Oppgavene merket EKSAMEN er fra tidligere eksamener |
