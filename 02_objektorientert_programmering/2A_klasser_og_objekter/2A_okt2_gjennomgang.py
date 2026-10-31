# IT2 2A - klassevariabler og samling av objekter, økt 2


# 1. Klassevariabel


class Medlem:
    medlemsnummer = 1  # felles for ALLE objekter

    def __init__(self, fornavn, etternavn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.medlemsnummer = Medlem.medlemsnummer  # dette objektet får nummeret
        Medlem.medlemsnummer += 1  # så teller vi opp for neste

    def __str__(self):
        return f'{self.fornavn} {self.etternavn}, nr {self.medlemsnummer}'


a = Medlem('Kari', 'Nordmann')
b = Medlem('Ola', 'Hansen')
c = Medlem('Ali', 'Khan')

print(a)
print(b)
print(c)
print(Medlem.medlemsnummer)

# Medlem.medlemsnummer er felles og teller oppover.
# self.medlemsnummer tilhører ett objekt og står fast.
# Samme ord, to helt ulike ting. Pek på det.


# 2. Mange objekter i en liste

klasse = []

for i in range(5):
    elev = Medlem(f'Elev{i}', 'Hansen')
    klasse.append(elev)

for elev in klasse:
    print(elev)

# Lista inneholder objekter, ikke tall eller tekst.
# Ellers oppfører den seg helt som lister pleier.


# 3. Lete i samlingen


def finn_medlem(nummer, liste):
    """Returnerer medlemmet med dette nummeret, eller None."""
    for medlem in liste:
        if medlem.medlemsnummer == nummer:
            return medlem
    return None


def finn_ved_fornavn(fornavn, liste):
    """Returnerer en liste med alle som har dette fornavnet."""
    funn = []
    for medlem in liste:
        if medlem.fornavn == fornavn:
            funn.append(medlem)
    return funn


print(finn_medlem(5, klasse))
print(finn_medlem(999, klasse))

for funn in finn_ved_fornavn('Elev2', klasse):
    print(funn)

# Skriver du ut hele lista med én print, får du objektadresser.
# print() på en liste bruker ikke __str__ på elementene.

# Dette er løkka som leter, fra kap 1. Det eneste nye er at
# elementene er objekter, så vi skriver medlem.fornavn
# i stedet for rad[0].


# 4. Regne på en samling av objekter


class Maaling:
    def __init__(self, sted, temperatur):
        self.sted = sted
        self.temperatur = temperatur

    def __str__(self):
        return f'{self.sted}: {self.temperatur} grader'


maalinger = [
    Maaling('Oslo', -3.2),
    Maaling('Bergen', 1.4),
    Maaling('Tromso', -8.7),
    Maaling('Kristiansand', 2.1),
]

sum_temp = 0
kaldest = maalinger[0]

for m in maalinger:
    sum_temp += m.temperatur
    if m.temperatur < kaldest.temperatur:
        kaldest = m

print(f'Snitt: {sum_temp / len(maalinger):.1f}')
print(f'Kaldest: {kaldest}')

# Beste hittil-mønsteret igjen, nå med objekter.
# kaldest er et helt objekt, ikke bare et tall.


# 5. Objekter inn i en figur

import matplotlib.pyplot as plt

steder = []
temperaturer = []

for m in maalinger:
    steder.append(m.sted)
    temperaturer.append(m.temperatur)

plt.bar(steder, temperaturer)
plt.axhline(0)
plt.ylabel('grader celsius')
plt.title('Temperatur')
plt.show()

# matplotlib forstår ikke objekter. Du må plukke ut listene selv.


# 6. Fra fil til objekter


class Sykkeltur:
    def __init__(self, dato, starttid, start, slutt, varighet):
        self.dato = dato
        self.starttid = starttid
        self.start = start
        self.slutt = slutt
        self.varighet = varighet

    def er_lang(self):
        return self.varighet > 30

    def __str__(self):
        return f'{self.dato} {self.starttid}  {self.start} til {self.slutt}  {self.varighet} min'


import csv

turer = []

with open('data/sykkelturer.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)
    for rad in innhold:
        tur = Sykkeltur(rad[0], rad[1], rad[2], rad[3], float(rad[4]))
        turer.append(tur)

print(f'{len(turer)} turer lest inn')
print(turer[0])

antall_lange = 0
for tur in turer:
    if tur.er_lang():
        antall_lange += 1

print(f'{antall_lange} turer varte over 30 minutter')

# tur.varighet er lesbart. rad[4] er det ikke.
# Det er hele gevinsten.


# 7. Samme algoritme i pseudokode

# På eksamen står algoritmer ofte som pseudokode. Det er ikke Python,
# men en avtale om hvordan man skriver en algoritme med ord.
# Slik ser finn_medlem fra seksjon 3 ut:
#
#   FUNCTION finnMedlem(nummer, liste)
#       FOR hvert medlem i liste
#           IF medlem.medlemsnummer EQUAL TO nummer
#               RETURN medlem
#           ENDIF
#       ENDFOR
#       RETURN ingenting
#   ENDFUNCTION
#
# Ordene eksamen bruker:
#
#   SET x TO 5               x = 5
#   DISPLAY x                print(x)
#   READ x                   x = input()
#   IF ... ENDIF             if
#   ELSE IF                  elif
#   FOR hvert ... ENDFOR     for
#   WHILE ... ENDWHILE       while
#   FUNCTION ... ENDFUNCTION def
#   RETURN                   return
#   EQUAL TO, GREATER THAN   ==, >
#   INCREMENT i              i += 1
#
# Innrykket viser hva som hører til hva, akkurat som i Python.
# END-ordene sier hvor en blokk slutter. Python bruker bare innrykket.
