"""
IT2 onsdag - OPPGAVER

Nøstede ordbøker.

REGELEN: regn ut selv med løkke der du kan.
Ikke bruk sum(), max() eller min().
"""

"""
1. KARAKTERBOKA MED FAG

    skole = {
        'Kari': {'matte': 5, 'norsk': 4, 'it2': 6},
        'Ola': {'matte': 3, 'norsk': 4, 'it2': 4},
        'Ali': {'matte': 6, 'norsk': 5, 'it2': 6},
        'Mia': {'matte': 4, 'norsk': 3, 'it2': 4},
    }

  a) Skriv ut alle elevene med fagene og karakterene sine
  b) Regn ut snittet for hver elev
  c) Regn ut snittet i hvert fag for hele klassen
  d) Finn eleven med best snitt, og finn faget klassen er svakest i
  e) Legg til en ny elev og et nytt fag for én av de gamle
"""


"""
2. KONTAKTLISTA

Bygg en ordbok der navnet er nøkkel og verdien er en ordbok med
telefon, e-post og klasse.

  a) Legg inn tre personer
  b) Skriv ut alle som en pen tabell
  c) La brukeren søke på et navn og få opp opplysningene.
     Bruk get() så det ikke krasjer på et navn som ikke finnes.
  d) Skriv ut alle som går i samme klasse
"""


"""
3. LAGERBEHOLDNING

    lager = {
        'Oslo': {'melk': 12, 'brød': 30, 'kaffe': 8},
        'Bergen': {'melk': 5, 'brød': 22},
        'Tromsø': {'melk': 0, 'kaffe': 15, 'te': 9},
    }

Legg merke til at butikkene ikke fører de samme varene.

  a) Skriv ut beholdningen per butikk
  b) Hvor mange liter melk finnes til sammen?
  c) Hvilke varer er utsolgt et sted?
  d) Lag en ny ordbok som viser totalen per vare på tvers av butikkene
  e) Hvilken butikk har flest varer på lager til sammen?

Hint til c og d: bruk in for å sjekke om en vare finnes i en butikk.
"""


"""
4. KANTINEKASSA

Dagens hovedoppgave. Den bruker alt fra 1A til nå.

    meny = {
        'kaffe': {'pris': 25.00, 'antall': 40},
        'bolle': {'pris': 32.00, 'antall': 15},
        'baguett': {'pris': 59.00, 'antall': 8},
        'juice': {'pris': 28.00, 'antall': 20},
    }

  a) Skriv ut menyen som en pen tabell med pris og hvor mange
     som er igjen
  b) La brukeren bestille en vare og et antall. Sjekk at varen finnes
     og at det er nok igjen.
  c) Trekk fra på lageret, og legg varen i bestillingen
  d) La brukeren bestille flere ting. Skriv 'ferdig' for å avslutte.
  e) Skriv ut en kvittering med varelinjer og totalsum
  f) Skriv ut dagens omsetning og hva som er utsolgt

  Utvidelser:
    - kolonnebredden tilpasses det lengste varenavnet
    - studentrabatt på 10 prosent
    - hold styr på hvor mange av hver vare som ble solgt
    - la brukeren angre siste vare
"""


"""
5. HAR DU KOMMET GJENNOM ALT?

Tre nivåer
    Utvid karakterboka til skole -> klasse -> elev -> fag.
    Regn ut snittet per klasse.

Reiseregister
    Nøkkel er et land, verdien er en ordbok med hovedstad,
    folketall og valuta. Skriv ut de tre folkerikeste.

Din egen
    Finn på en oppgave og lever den til læreren med fasit.
"""
