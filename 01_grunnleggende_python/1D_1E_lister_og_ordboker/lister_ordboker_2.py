"""
IT2 mandag - OPPGAVER

Ordbok som oppslagstabell.

REGELEN: regn ut selv med løkke der du kan.
Ikke bruk sum(), max() eller min().
"""

"""
1. TERNINGSYMBOLER

    symbol = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}

  a) Kast en terning med random og skriv ut symbolet
  b) Kast ti ganger og skriv alle symbolene på én linje
  c) Tell hvor mange ganger hvert symbol kom, og skriv ut en tabell
"""


"""
2. KARAKTERBESKRIVELSE

Lag en ordbok som gir en beskrivelse til hver karakter:
1 er svært lav, 2 er lav, 3 er nokså god, 4 er god,
5 er meget god, 6 er fremragende.

  a) Slå opp én karakter og skriv ut beskrivelsen
  b) Skriv ut hele skalaen som en pen tabell
  c) Hva skjer hvis noen slår opp karakteren 7? Fiks det med get()
"""


"""
3. MÅNEDER

Lag to ordbøker: én som gir månedsnavn fra nummer, og én som gir
antall dager i måneden.

  a) Skriv ut navnet og antall dager for en måned brukeren oppgir
  b) Skriv ut hele året som en tabell
  c) Regn ut hvor mange dager det er i året til sammen
  d) Legg inn skuddår. Februar skal ha 29 dager når året er skuddår.
"""


"""
4. FRA ELIF-KJEDE TIL ORDBOK

Her er et program som gjør om et tall til en himmelretning:

    retning = 2

    if retning == 0:
        navn = 'nord'
    elif retning == 1:
        navn = 'nordøst'
    elif retning == 2:
        navn = 'øst'
    elif retning == 3:
        navn = 'sørøst'
    elif retning == 4:
        navn = 'sør'
    elif retning == 5:
        navn = 'sørvest'
    elif retning == 6:
        navn = 'vest'
    else:
        navn = 'nordvest'

    print(navn)

  a) Skriv om hele elif-kjeden til ett oppslag i en ordbok
  b) Hvor mange linjer kortere ble programmet?
  c) Be brukeren om et tall og skriv ut retningen.
     Bruk get() så det ikke krasjer på et tall utenfor 0-7.
  d) Gå motsatt vei: lag en ordbok som gir tallet når du oppgir navnet
"""


"""
5. VALUTA

    kurser = {'USD': 10.85, 'EUR': 11.70, 'GBP': 13.40, 'SEK': 1.02}

  a) Be brukeren om et beløp i kroner og en valuta.
     Skriv ut hvor mye det blir.
  b) Skriv ut beløpet i alle valutaene som en tabell med to desimaler
  c) Gå motsatt vei: hvor mange kroner er 100 av hver valuta?
  d) Bruk get() så programmet ikke krasjer på en valuta som ikke finnes
"""


"""
6. MORSEKODE

    morse = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'i': '..', 'k': '-.-', 'n': '-.', 'o': '---', 'r': '.-.',
        's': '...', 't': '-',
    }

  a) Oversett ordet 'kode' til morse. Skill tegnene med mellomrom.
  b) Be brukeren om et ord og oversett det
  c) Hva skjer med en bokstav som ikke står i ordboka? Fiks det.
  d) Utvid ordboka med resten av alfabetet
"""


"""
7. TALLORD

    tallord = {'en': 1, 'to': 2, 'tre': 3, 'fire': 4, 'fem': 5,
               'seks': 6, 'sju': 7, 'åtte': 8, 'ni': 9, 'ti': 10}

  a) Regn ut summen av tallordene i setningen 'tre fem ni to'.
     Svaret er 19.
  b) Finn det største tallordet i setningen
  c) Snu ordboka: lag en ny der tallet er nøkkel og ordet er verdi.
     Skriv ut 7 som 'sju'.
"""


"""
8. ROMERTALL

    verdier = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
               'D': 500, 'M': 1000}

Vanligvis legges tegnene sammen: XVI er 16. Men står et lite tegn
FORAN et større, skal det trekkes fra: IV er 4, ikke 6.

  a) Regn ut verdien av XVI
  b) Få med fratrekksregelen. MCMXCIV skal gi 1994.
  c) Test med noen årstall du kjenner
"""


"""
9. HAR DU KOMMET GJENNOM ALT?

Kortstokk
    Lag en ordbok som gir verdien til hvert kort: to til ti er seg selv,
    knekt er 11, dame 12, konge 13 og ess 14. Trekk fem tilfeldige kort
    og regn ut summen.

Bokstavpoeng
    I Scrabble er noen bokstaver verdt mer enn andre. Lag en ordbok med
    poeng per bokstav og regn ut hva et ord er verdt.

Din egen
    Finn på en oppgave og lever den til læreren med fasit.
"""
