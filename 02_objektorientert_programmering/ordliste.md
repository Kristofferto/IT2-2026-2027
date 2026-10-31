# Ordliste for kapittel 2

Objektorientert programmering har mange nye ord, og eksamen bruker dem i flervalg hvert år. Her står de med en kort forklaring og et eksempel. Ordlista er lov å bruke på prøver.

Engelsk står i parentes når feilmeldinger eller nettsider bruker det engelske ordet.

[Klasser](#1-klasser-og-objekter) ·
[Innkapsling](#2-innkapsling-og-feil) ·
[Samlinger](#3-klassevariabler-og-samlinger) ·
[Arv](#4-arv-og-de-fire-ordene) ·
[Pseudokode](#5-pseudokode) ·
[Ord som ligner](#ord-som-ligner)

---

## 1. Klasser og objekter

| Ord | Betyr | Eksempel |
|---|---|---|
| **klasse** (class) | oppskriften på en type ting: hva den vet, og hva den kan | `class Bil:` |
| **objekt** | én ting laget fra en klasse. Hvert objekt har sine egne verdier | `bil1 = Bil('Volvo', 0)` |
| **instans** | et annet ord for objekt. «bil1 er en instans av Bil» | |
| **attributt** | en verdi objektet husker. Kalles også egenskap eller felt | `self.merke` |
| **metode** | en funksjon som hører til klassen, og som kan bruke attributtene | `def kjor(self, km):` |
| **konstruktør** | metoden som kjører når objektet lages, og gir det attributtene | `def __init__(self, merke):` |
| **`self`** | «dette objektet». Står først i hver metode, men sendes ikke med i kallet | `self.kilometer += km` |
| **`__str__`** | metoden `print` bruker for å vise objektet. Skal returnere tekst | `return f'{self.merke}'` |
| **standardverdi** | verdien en parameter får hvis du ikke sender noe | `def __init__(self, km=0):` |
| **docstring** | teksten under `class` eller `def` som sier hva den gjør | `"""En bil med merke."""` |
| **punktum** | brukes for å nå attributter og metoder i et objekt | `bil1.kjor(100)` |

---

## 2. Innkapsling og feil

| Ord | Betyr | Eksempel |
|---|---|---|
| **innkapsling** | dataene er pakket inn i objektet og endres bare gjennom metodene, som sjekker verdiene | `konto.sett_inn(100)`, ikke `konto._saldo = 100` |
| **privat** | skal ikke brukes utenfor klassen. Understrek i Python, minus i UML | `self._saldo` |
| **offentlig** | laget for å brukes utenfra. Pluss i UML | `def sett_inn(self, belop):` |
| **grensesnitt** | metodene andre bruker for å snakke med objektet | `sett_inn`, `ta_ut`, `vis_saldo` |
| **unntak** (exception) | en feil som stopper programmet hvis ingen fanger den | `ValueError`, `TypeError` |
| **kaste et unntak** | å stoppe med en egen feilmelding når noe er galt | `raise ValueError('Negativt beløp')` |
| **fange et unntak** | å ta imot feilen så programmet kan fortsette | `try:` … `except ValueError as feil:` |
| **testprogram** | kode som lager objekter, kaller metodene og viser at både vanlige verdier og feil håndteres riktig | |

---

## 3. Klassevariabler og samlinger

| Ord | Betyr | Eksempel |
|---|---|---|
| **klassevariabel** | én verdi som er felles for alle objektene av klassen | `Medlem.antall` |
| **objektvariabel** | en verdi som hører til ett objekt. Det samme som attributt | `self.navn` |
| **samling av objekter** | en liste med objekter. Du løper gjennom den som alle andre lister | `for m in medlemmer:` |

---

## 4. Arv og de fire ordene

| Ord | Betyr | Eksempel |
|---|---|---|
| **arv** (inheritance) | en klasse bygger på en annen og får alt den har | `class Hund(Dyr):` |
| **superklasse** | klassen det arves fra. Kalles også foreldreklasse | `Dyr` |
| **subklasse** | klassen som arver. Kalles også barneklasse | `Hund` |
| **`super()`** | brukes i subklassen for å kjøre metoden i superklassen | `super().__init__(navn)` |
| **overstyre** (override) | subklassen lager sin egen versjon av en metode den har arvet | `def spis(self):` i `Fisk` |
| **polymorfisme** | samme metodekall gjør forskjellige ting avhengig av objektet | `d.spis()` i en løkke over dyr |
| **abstraksjon** | å bruke hva et objekt kan, uten å tenke på hvordan det gjøres | `kvadrat.areal()` |
| **abstrakt klasse** | en superklasse det aldri lages objekter av, bare subklasser | `SpillObjekt` i Manic Mansion |
| **spesialisering** | subklassen er en spesialisering av superklassen | en hund er et spesielt dyr |
| **generalisering** | superklassen er en generalisering av subklassene | dyr er det hunder og fisker har felles |
| **gjenbruk** | koden skrives én gang og brukes flere steder. Arv er én måte | |

**De fire prinsippene i objektorientert programmering** er arv, polymorfisme, innkapsling og abstraksjon. Eksamen spør om dem nesten hvert år.

---

## 5. Pseudokode

| Ord | Betyr | Eksempel |
|---|---|---|
| **algoritme** | en oppskrift i trinn som løser et problem | finn det største tallet i en liste |
| **pseudokode** | en algoritme skrevet med ord og faste nøkkelord. Kan ikke kjøres | `SET x TO 5`, `DISPLAY x` |

---

## Ord som ligner

| Disse | Forskjellen |
|---|---|
| klasse og objekt | klassen er oppskriften, objektet er kaka. Én klasse, mange objekter |
| attributt og metode | attributtet er noe objektet **vet**, metoden er noe det **kan** |
| funksjon og metode | en metode er en funksjon inne i en klasse, og har `self` |
| parameter og argument | parameteren er navnet i `def`, argumentet er verdien du sender i kallet |
| `return` og `print` | `return` gir verdien tilbake så den kan brukes videre. `print` bare viser den |
| klassevariabel og objektvariabel | `Medlem.antall` er felles for alle, `self.navn` hører til ett objekt |
| arv og polymorfisme | arv gjør at subklassen **får** metoden. Polymorfisme gjør at riktig versjon **kjøres** |
| innkapsling og abstraksjon | innkapsling **beskytter dataene**. Abstraksjon **skjuler hvordan** det gjøres |
| spesialisering og generalisering | samme forhold sett fra hver sin ende. Subklassen er spesialiseringen |
