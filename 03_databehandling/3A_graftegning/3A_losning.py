"""
IT2 3A - LØSNINGSFORSLAG

Hver oppgave åpner ett eller flere vinduer. Lukk vinduet for å gå videre.
"""

import random

import matplotlib.pyplot as plt
import numpy as np

"""
3A OPPGAVE 1 - første graf
"""

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# a) og b)
plt.plot(x, y)
plt.title('y = x i andre')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# c)
plt.scatter(x, y)
plt.title('y = x i andre, som punkter')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# d) Begge i samme figur: kall plot og scatter før show.
plt.plot(x, y)
plt.scatter(x, y)
plt.title('Linje og punkter')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


"""
3A OPPGAVE 2 - fra løkke til graf
"""

x = []
kvadrat = []
kube = []

for i in range(21):
    x.append(i)
    kvadrat.append(i**2)
    kube.append(i**3)

plt.plot(x, kvadrat, label='x^2')
plt.plot(x, kube, label='x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('To potensfunksjoner')
plt.legend()
plt.ylim(0, 400)
plt.show()

# e) x^3 forsvinner ut av bildet etter x = 7. Dataene er der,
#    men utsnittet skjuler dem.


"""
3A OPPGAVE 3 - karakterer
"""

karakterer = [4, 5, 3, 6, 4, 4, 2, 5, 6, 3, 4, 5, 4, 3, 5, 6, 2, 4]

plt.hist(karakterer, bins=[1, 2, 3, 4, 5, 6, 7])
plt.xlabel('Karakter')
plt.ylabel('Antall')
plt.title('Fordeling av karakterer, histogram')
plt.show()

fordeling = {}
for k in karakterer:
    if k in fordeling:
        fordeling[k] += 1
    else:
        fordeling[k] = 1

verdier = sorted(fordeling)
antall = []
for k in verdier:
    antall.append(fordeling[k])

plt.bar(verdier, antall)
plt.xlabel('Karakter')
plt.ylabel('Antall')
plt.title('Fordeling av karakterer, søylediagram')
plt.show()

# d) Histogram teller selv. Søylediagram tegner tall du allerede har.
#    Har du rådata, bruk histogram. Har du en oppsummering, bruk bar.


"""
3A OPPGAVE 4 - valgresultat
"""

partier = ['A', 'H', 'SV', 'FrP', 'Sp', 'V', 'MDG']
stemmer = [26.3, 20.4, 7.6, 11.6, 13.5, 4.6, 3.9]

# a)
plt.pie(stemmer, labels=partier)
plt.title('Valgresultat i prosent')
plt.show()

# b)
plt.barh(partier, stemmer)
plt.title('Valgresultat i prosent')
plt.xlabel('Prosent av stemmene')
plt.ylabel('Parti')
plt.show()

# c) Søylediagrammet er lettest å lese nøyaktig. Øyet er flinkt til å
#    sammenligne lengder, men dårlig til å sammenligne vinkler og arealer.
#    I sektordiagrammet er det vanskelig å se at Sp er større enn FrP.

# d) Sorter med løkke: finn den største som er igjen, flytt den over i
#    de nye listene, og gjenta til de gamle listene er tomme.
igjen_partier = partier.copy()
igjen_stemmer = stemmer.copy()
sorterte_partier = []
sorterte_stemmer = []

while len(igjen_stemmer) > 0:
    storst = 0
    for i in range(len(igjen_stemmer)):
        if igjen_stemmer[i] > igjen_stemmer[storst]:
            storst = i
    sorterte_partier.append(igjen_partier.pop(storst))
    sorterte_stemmer.append(igjen_stemmer.pop(storst))

plt.barh(sorterte_partier, sorterte_stemmer)
plt.gca().invert_yaxis()  # barh tegner nedenfra, så den største havner øverst
plt.title('Valgresultat i prosent, sortert')
plt.xlabel('Prosent av stemmene')
plt.ylabel('Parti')
plt.show()


"""
3A OPPGAVE 5 - to byer
"""

maaneder = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'des']
oslo = [-3.2, -2.1, 1.8, 6.4, 12.1, 16.3, 18.0, 16.8, 12.4, 6.9, 1.5, -1.8]
bergen = [1.4, 1.9, 3.6, 6.1, 10.2, 13.0, 14.1, 14.2, 11.5, 8.4, 4.3, 2.1]

plt.plot(maaneder, oslo, linestyle='--', marker='o', label='Oslo')
plt.plot(maaneder, bergen, marker='s', label='Bergen')
plt.axhline(0)
plt.xlabel('Måned')
plt.ylabel('Grader celsius')
plt.title('Middeltemperatur')
plt.legend()
plt.show()

# d) største forskjell
storst = 0
maaned_storst = ''
forskjell = []

for i in range(len(maaneder)):
    diff = oslo[i] - bergen[i]
    forskjell.append(diff)
    if abs(diff) > storst:
        storst = abs(diff)
        maaned_storst = maaneder[i]

print(f'Størst forskjell i {maaned_storst}: {storst:.1f} grader')

# e)
plt.plot(maaneder, forskjell, marker='o')
plt.axhline(0)
plt.title('Forskjellen mellom Oslo og Bergen')
plt.xlabel('Måned')
plt.ylabel('Oslo minus Bergen (grader)')
plt.show()


"""
3A OPPGAVE 6 - subplot
"""

# a) til c)
plt.subplot(1, 2, 1)
plt.plot(maaneder, oslo)
plt.title('Oslo')
plt.xlabel('Måned')
plt.ylabel('Grader celsius')
plt.ylim(-5, 20)

plt.subplot(1, 2, 2)
plt.plot(maaneder, bergen)
plt.title('Bergen')
plt.xlabel('Måned')
plt.ylim(-5, 20)

plt.show()

# c) Lik y-akse er det som gjør figurene sammenlignbare.
#    Uten den ser Bergen ut til å svinge like mye som Oslo.

# d) Fire grafer i et 2x2-rutenett. Nummeret går radvis: 1 2 / 3 4.
plt.subplot(2, 2, 1)
plt.plot(maaneder, oslo)
plt.title('Oslo')

plt.subplot(2, 2, 2)
plt.plot(maaneder, bergen)
plt.title('Bergen')

plt.subplot(2, 2, 3)
plt.bar(maaneder, oslo)
plt.title('Oslo, søyler')

plt.subplot(2, 2, 4)
plt.plot(maaneder, forskjell)
plt.title('Oslo minus Bergen')

plt.tight_layout()  # hindrer at titlene overlapper
plt.show()


"""
3A OPPGAVE 7 - lagre figuren
"""

# a)
plt.plot(maaneder, oslo, label='Oslo')
plt.plot(maaneder, bergen, label='Bergen')
plt.title('Middeltemperatur')
plt.xlabel('Måned')
plt.ylabel('Grader celsius')
plt.legend()
plt.savefig('temperatur.png')
plt.show()

# b) temperatur.png ligger i mappa fila kjører fra.

# c) Står savefig etter show, blir bildet tomt. show() viser figuren,
#    og når vinduet lukkes, er figuren borte. Da er det ingenting igjen
#    å lagre. savefig må alltid stå før show.


"""
3A OPPGAVE 8 - har du kommet gjennom alt?
"""

# Terningstatistikk
summer = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
antall_kast = [0] * 11

for i in range(10000):
    summen = random.randint(1, 6) + random.randint(1, 6)
    antall_kast[summen - 2] += 1

plt.bar(summer, antall_kast)
plt.title('Summen av to terninger, 10 000 kast')
plt.xlabel('Sum')
plt.ylabel('Antall')
plt.show()

# Fordelingen er en trekant med topp på 7. Det er seks måter å få 7 på,
# men bare én måte å få 2 eller 12.


# Funksjonsplotter
def tegn_graf(f, start, slutt):
    """Tegner funksjonen f fra start til slutt, med 200 punkter."""
    steg = (slutt - start) / 199
    x = []
    y = []
    for i in range(200):
        verdi = start + i * steg
        x.append(verdi)
        y.append(f(verdi))
    plt.plot(x, y)
    plt.title('Grafen til funksjonen')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()


tegn_graf(np.sin, 0, 2 * np.pi)

# Din egen: ingen fasit. En god figur har tittel, aksetitler med enhet,
# og en diagramtype som passer til dataene.
