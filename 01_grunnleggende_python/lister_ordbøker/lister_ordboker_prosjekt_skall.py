# IT2 fagdag - prosjekt
# Velg A eller B. Begge bruker lister, 2D-lister og ordbøker.
# Fyll ut TODO-ene i rekkefølge, og kjør etter hver.


import random

# ============================================================
# PROSJEKT A - KARAKTERBOKA
# ============================================================

karakterer = {
    'Kari': [5, 4, 6, 5],
    'Ola': [3, 4, 4, 2],
    'Ali': [6, 6, 5, 6],
    'Mia': [4, 3, 4, 4],
    'Jonas': [2, 3, 3, 4],
}

# TODO A1: skriv ut alle elevene med karakterene sine

# TODO A2: regn ut snittet for hver elev og skriv det ut med én desimal
#          Summer med en løkke og del på len(). Ikke bruk ferdige
#          funksjoner - poenget er at du ser hva som skjer.

# TODO A3: finn eleven med det beste snittet, og den med det svakeste

# TODO A4: skriv ut en pen tabell med navn, karakterer og snitt,
#          i kolonner som står rett under hverandre

# TODO A5: legg til en ny elev, og legg til en karakter for en
#          som allerede finnes

# UTVIDELSER
#   - regn ut klassens snitt
#   - tell hvor mange som har hver karakter (ordbok igjen)
#   - sorter tabellen etter snitt
#   - la brukeren skrive inn navn og få opp karakterene


# ============================================================
# PROSJEKT B - MINESVEIPER
# ============================================================

RADER = 8
KOLONNER = 8
BOMBER = 10

# TODO B1: lag et tomt brett, altså en 2D-liste med RADER rader
#          og KOLONNER kolonner, fylt med 0

# TODO B2: plasser BOMBER bomber på tilfeldige plasser.
#          Bruk -1 for bombe. Pass på at du ikke legger to på
#          samme rute.
#          Hint: random.randint(0, RADER - 1)

# TODO B3: for hver rute som IKKE er bombe, tell hvor mange bomber
#          som ligger i de åtte naborutene.
#          Pass på kantene - rad -1 og rad RADER finnes ikke.

# TODO B4: skriv ut brettet pent. Bruk * for bombe og mellomrom
#          der tallet er 0, så det blir lettere å lese.

# UTVIDELSER
#   - la brukeren skrive inn rad og kolonne for å åpne en rute
#   - lag et eget brett som holder styr på hva som er åpnet
#   - avslutt spillet når brukeren treffer en bombe
