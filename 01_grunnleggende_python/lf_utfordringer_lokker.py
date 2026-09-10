"""
IT2 1C - UTFORDRINGER, LØSNINGSFORSLAG

Testverdiene er skrevet rett inn så fila kan kjøres i sin helhet.
input()-linja står som kommentar der den hører hjemme.
"""

import random

import numpy as np

"""
1. GANGETABELLEN
"""

print(f'{"":>5}', end='')
for kolonne in range(1, 11):
    print(f'{kolonne:>5}', end='')
print()

for rad in range(1, 11):
    print(f'{rad:>5}', end='')
    for kolonne in range(1, 11):
        print(f'{rad * kolonne:>5}', end='')
    print()  # tom print avslutter raden

# c) nedre halvdel: legg inn if kolonne <= rad
# d) Gangetabellen er symmetrisk. 3 * 7 og 7 * 3 er samme tall.


"""
2. PRIMTALL
"""

tall = 97  # input('Tall: ')
er_primtall = tall > 1

for deler in range(2, int(np.sqrt(tall)) + 1):
    if tall % deler == 0:
        er_primtall = False
        break  # d) ingen grunn til å lete videre

print(f'{tall} er primtall: {er_primtall}')

antall = 0
for kandidat in range(2, 100):
    primtall = True
    for deler in range(2, int(np.sqrt(kandidat)) + 1):
        if kandidat % deler == 0:
            primtall = False
            break
    if primtall:
        antall += 1

print(f'Primtall under 100: {antall}')

# c) Det holder å gå til kvadratroten. Har tallet en deler større
#    enn roten, må det også ha en mindre - de kommer alltid i par.


"""
3. FIBONACCI OG DET GYLNE SNITT
"""

a, b = 1, 1

for i in range(20):
    print(f'{a:>8}{b / a:>16.10f}')
    a, b = b, a + b  # begge oppdateres samtidig

print(f'Det gylne snitt: {(1 + np.sqrt(5)) / 2:.10f}')

# d) Rundt 15-16 ledd før seks desimaler stemmer.


"""
4. COLLATZ
"""

tall = 27
steg = 0

while tall != 1:
    if tall % 2 == 0:
        tall = tall // 2
    else:
        tall = 3 * tall + 1
    steg += 1

print(f'27 bruker {steg} steg.')

beste_start = 0
beste_lengde = 0

for start in range(2, 1000):
    tall = start
    steg = 0
    while tall != 1:
        if tall % 2 == 0:
            tall = tall // 2
        else:
            tall = 3 * tall + 1
        steg += 1
    if steg > beste_lengde:
        beste_start = start
        beste_lengde = steg

print(f'Lengst rekke: {beste_start} med {beste_lengde} steg')

# d) Vi vet ikke på forhånd hvor mange steg det tar. Det er nettopp
#    det som er uløst i matematikken.


"""
5. KVADRATROT UTEN np.sqrt
"""

n = 2
x = 1.0
runde = 0

while not np.isclose(x * x, n, rtol=1e-15):
    x = 0.5 * (x + n / x)
    runde += 1
    print(f'Runde {runde}: {x:.15f}')

print(f'np.sqrt: {np.sqrt(2):.15f}')

# b) Fem runder holder fra x = 1.
# d) Fra x = 1000 trengs rundt et titalls runder ekstra. Metoden
#    halverer avstanden raskt, så et dårlig startgjett koster lite.


"""
6. PI MED TILFELDIGE TALL
"""

random.seed(2026)

kast = 100000
innenfor = 0

for i in range(kast):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        innenfor += 1

print(f'Estimat for pi: {4 * innenfor / kast:.5f}')
print(f'Fasit:          {np.pi:.5f}')

# c) Feilen synker som 1 / sqrt(antall kast). Hundre ganger så mange
#    kast gir ti ganger så godt svar.
# d) Med seed blir tallene like hver gang. Det gjør at du kan
#    reprodusere en kjøring, og det avslører at tallene ikke er
#    tilfeldige i det hele tatt - de er bare vanskelige å forutsi.


"""
7. KVITTERING FRA TO LISTER
"""

varer = ['Melk', 'Kaffefilter', 'Brød']
priser = [21.90, 34.50, 89.00]

bredde = 0
for vare in varer:
    if len(vare) > bredde:
        bredde = len(vare)
bredde += 2

total = 0
dyrest = 0

for i in range(len(varer)):
    print(f'{varer[i]:<{bredde}}{priser[i]:>8.2f}')
    total += priser[i]
    if priser[i] > priser[dyrest]:
        dyrest = i

print(f'{"-" * (bredde + 8)}')
print(f'{"Totalt":<{bredde}}{total:>8.2f}')
print(f'Dyreste vare: {varer[dyrest]}')


"""
8. BINÆRSØK
"""

hemmelig = 738
lav = 1
hoy = 1000
antall_gjett = 0

while True:
    gjett = (lav + hoy) // 2
    antall_gjett += 1
    print(f'Gjett {antall_gjett}: {gjett}')
    if gjett == hemmelig:
        break
    elif gjett < hemmelig:
        lav = gjett + 1
    else:
        hoy = gjett - 1

print(f'Funnet på {antall_gjett} gjett.')
print(f'log2(1000) = {np.log2(1000):.2f}')

# b) Verste tilfelle er 10 gjett for 1000 tall.
# c) Hver gjetning halverer området. Antall gjett er derfor log2 av
#    antall muligheter, rundet opp.
# d) En million: 20 gjett. En milliard: 30.
