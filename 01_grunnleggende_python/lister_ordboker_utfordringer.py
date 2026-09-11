"""
IT2 fagdag - UTFORDRINGER

For deg som er ferdig med de vanlige oppgavene.

Du har alt fra 1A til 1C, pluss lister, 2D-lister og ordbøker.
Ingen funksjoner - de kommer senere.

Kan noe regnes ut med en løkke, skal det gjøres med en løkke.
Ikke bruk sum(), max(), min() eller np.mean().
"""

"""
1. BOKSTAVTELLING

Bruk en ordbok til å telle hvor mange ganger hver bokstav
forekommer i en tekst.

  a) Tell bokstavene i 'informasjonsteknologi'
  b) Hopp over mellomrom, og la store og små bokstaver telle likt
  c) Finn den hyppigste bokstaven med en løkke
  d) Skriv ut resultatet sortert alfabetisk
"""


"""
2. FRA TO LISTER TIL ÉN ORDBOK

    navn = ['Kari', 'Ola', 'Ali', 'Mia']
    poeng = [88, 72, 95, 64]

  a) Bygg en ordbok med navn som nøkkel og poeng som verdi
  b) Skriv ut alle som har over 70 poeng
  c) Finn navnet på den med flest poeng
  d) Hva skjer hvis to elever heter det samme? Prøv det.
     Er det et problem med lister også?
"""


"""
3. TRANSPONERING

Å transponere en 2D-liste betyr å bytte om rader og kolonner.

    [[1, 2, 3],          [[1, 4],
     [4, 5, 6]]    ->     [2, 5],
                          [3, 6]]

  a) Skriv koden som transponerer en 2D-liste
  b) Den skal virke for alle størrelser, ikke bare 2x3
  c) Skriv ut både den opprinnelige og den transponerte, pent
  d) Hva skjer hvis du transponerer to ganger?
"""


"""
4. TRE PÅ RAD

    brett = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'X'],
    ]

  a) Sjekk om noen har tre like på en rad
  b) Sjekk kolonnene også
  c) Sjekk de to diagonalene
  d) Skriv ut hvem som har vunnet, eller at ingen har det ennå
"""


"""
5. HANDLELISTA

    handleliste = {
        'melk': [2, 21.90],
        'brød': [1, 34.50],
        'kaffe': [3, 89.00],
    }

Verdien er en liste med antall og pris.

  a) Skriv ut en kvittering med varenavn, antall, pris og sum
  b) Regn ut totalsummen
  c) Kolonnebredden skal tilpasse seg det lengste varenavnet
  d) Legg til en vare underveis, og fjern en annen
"""


"""
6. TERNINGSTATISTIKK

Kast to terninger 100 000 ganger og tell hvor ofte hver sum
fra 2 til 12 forekommer.

  a) Bruk en ordbok til tellingen
  b) Skriv ut resultatet som et stolpediagram av stjerner:

        7   ****************  16.6 %

  c) Sammenlign med det du ville regnet ut for hånd.
     Hvor mange av de 36 kombinasjonene gir sum 7?
  d) Prøv med 100 kast i stedet. Hvorfor blir det så mye styggere?
"""


"""
7. ORDFREKVENS

    setning = 'det var en gang en katt og en hund og en mus'

  a) Del opp setningen i ord og tell hvor ofte hvert ord forekommer
  b) Skriv ut ordene sortert etter hyppighet, det vanligste først
  c) Finn ordene som bare forekommer én gang
  d) Hvor mange forskjellige ord er det totalt?

Hint til b: sorted(ordbok, key=ordbok.get, reverse=True)
"""


"""
8. HAR DU KOMMET GJENNOM ALT?

Sudoku-sjekk
    Gitt et 9x9-brett som en 2D-liste. Sjekk om hver rad og hver
    kolonne inneholder tallene 1 til 9 nøyaktig én gang.
    Klarer du de ni 3x3-boksene også?

Vokalregister
    Bygg en ordbok der nøkkelen er en vokal og verdien er en liste
    med alle ordene i en setning som inneholder den vokalen.
    Et ord kan havne i flere lister.

Din egen
    Finn på en oppgave som er vanskelig med disse verktøyene,
    og lever den til læreren med fasit.
"""
