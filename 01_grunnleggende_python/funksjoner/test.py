# vi lager oss noen funksjoner

import minmatte
import numpy as np


def hilse():
    print('Hei')


hilse()


def areal(lengde, bredde):
    return lengde * bredde


bredde = 5
lengde = 4
print(
    f'Arealet til en firkant med bredde {bredde} og lengde {lengde} er {areal(bredde, lengde)}'
)

print(areal(4, 7))
areal(19, 200)


def beregn_mva(pris, sats=0.25):
    return pris * sats, pris


print(beregn_mva(100))
print(beregn_mva(1000, 0.10))
print(beregn_mva(sats=0.10, pris=100))


def min_maks(liste):
    minst = liste[0]
    storst = liste[0]

    for verdi in liste:
        if verdi < minst:
            minst = verdi
        if verdi > storst:
            storst = verdi

    return minst, storst


print(min_maks([2, 5, 78, 2, 5, 1]))

minste, storste = min_maks([2, 5, 78, 2, 5, 1])

print(f'Minste: {minste}')
print(f'Største: {storste}')

antall = 5


def les_antall():
    return antall


def ok(tall):
    tall += 1
    return tall


ok(antall)
print(les_antall())


nytt = antall * 2
