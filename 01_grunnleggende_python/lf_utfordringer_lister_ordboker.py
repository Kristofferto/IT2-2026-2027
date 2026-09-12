"""
IT2 fagdag - UTFORDRINGER, LØSNINGSFORSLAG

Testverdiene er skrevet rett inn så fila kan kjøres i sin helhet.
"""

import random

"""
1. BOKSTAVTELLING
"""

tekst = 'informasjonsteknologi'
antall = {}

for bokstav in tekst.lower():
    if bokstav == ' ':
        continue
    if bokstav in antall:
        antall[bokstav] += 1
    else:
        antall[bokstav] = 1

hyppigst = ''
flest = 0

for bokstav, tall in antall.items():
    if tall > flest:
        hyppigst = bokstav
        flest = tall

print(f'Hyppigst: {hyppigst} ({flest} ganger)')

for bokstav in sorted(antall):
    print(f'{bokstav}: {antall[bokstav]}')


"""
2. FRA TO LISTER TIL ÉN ORDBOK
"""

navn = ['Kari', 'Ola', 'Ali', 'Mia']
poeng = [88, 72, 95, 64]

resultat = {}

for i in range(len(navn)):
    resultat[navn[i]] = poeng[i]

print(resultat)

for elev, p in resultat.items():
    if p > 70:
        print(f'{elev:<8}{p:>5}')

beste = ''
best_poeng = 0

for elev, p in resultat.items():
    if p > best_poeng:
        beste = elev
        best_poeng = p

print(f'Best: {beste} med {best_poeng} poeng')

# d) To like navn kolliderer - den siste overskriver den første.
#    Lister har ikke det problemet, men der må du holde styr på
#    indeksene selv. Begge løsningene har en pris.


"""
3. TRANSPONERING
"""

matrise = [
    [1, 2, 3],
    [4, 5, 6],
]

transponert = []

for k in range(len(matrise[0])):
    ny_rad = []
    for r in range(len(matrise)):
        ny_rad.append(matrise[r][k])
    transponert.append(ny_rad)

print('Original:')
for rad in matrise:
    for verdi in rad:
        print(f'{verdi:>4}', end='')
    print()

print('Transponert:')
for rad in transponert:
    for verdi in rad:
        print(f'{verdi:>4}', end='')
    print()

# d) To transponeringer gir originalen tilbake.


"""
4. TRE PÅ RAD
"""

brett = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X'],
]

vinner = ''

for rad in brett:
    if rad[0] == rad[1] == rad[2] != ' ':
        vinner = rad[0]

for k in range(3):
    if brett[0][k] == brett[1][k] == brett[2][k] != ' ':
        vinner = brett[0][k]

if brett[0][0] == brett[1][1] == brett[2][2] != ' ':
    vinner = brett[0][0]

if brett[0][2] == brett[1][1] == brett[2][0] != ' ':
    vinner = brett[0][2]

if vinner == '':
    print('Ingen har vunnet ennå.')
else:
    print(f'{vinner} har vunnet.')


"""
5. HANDLELISTA
"""

handleliste = {
    'melk': [2, 21.90],
    'brød': [1, 34.50],
    'kaffe': [3, 89.00],
}

handleliste['bananer'] = [6, 4.50]
del handleliste['brød']

bredde = 0
for vare in handleliste:
    if len(vare) > bredde:
        bredde = len(vare)
bredde += 2

total = 0

print(f'{"Vare":<{bredde}}{"Ant":>5}{"Pris":>9}{"Sum":>9}')
print(f'{"-" * (bredde + 23)}')

for vare, verdier in handleliste.items():
    ant = verdier[0]
    pris = verdier[1]
    total += ant * pris
    print(f'{vare:<{bredde}}{ant:>5}{pris:>9.2f}{ant * pris:>9.2f}')

print(f'{"-" * (bredde + 23)}')
print(f'{"Totalt":<{bredde}}{"":>5}{"":>9}{total:>9.2f}')


"""
6. TERNINGSTATISTIKK
"""

random.seed(2026)

kast = 100000
tellinger = {}

for i in range(kast):
    sum_terning = random.randint(1, 6) + random.randint(1, 6)
    if sum_terning in tellinger:
        tellinger[sum_terning] += 1
    else:
        tellinger[sum_terning] = 1

for sum_terning in sorted(tellinger):
    andel = tellinger[sum_terning] / kast
    stjerner = '*' * int(andel * 100)
    print(f'{sum_terning:>3}   {stjerner:<20}{andel:>7.1%}')

# c) Sum 7 kan lages på seks måter av 36, altså 16,7 prosent.
# d) Med 100 kast er tilfeldig variasjon like stor som mønsteret.
#    Feilen synker som 1 / sqrt(antall kast).


"""
7. ORDFREKVENS
"""

setning = 'det var en gang en katt og en hund og en mus'
ord_antall = {}

for ordet in setning.split():
    if ordet in ord_antall:
        ord_antall[ordet] += 1
    else:
        ord_antall[ordet] = 1

for ordet in sorted(ord_antall, key=ord_antall.get, reverse=True):
    print(f'{ordet:<8}{ord_antall[ordet]}')

print('Bare én gang:')
for ordet, tall in ord_antall.items():
    if tall == 1:
        print(f'  {ordet}')

print(f'Antall forskjellige ord: {len(ord_antall)}')

sum_forekomster = 0
for tall in ord_antall.values():
    sum_forekomster += tall

print(f'Gjennomsnitt per ord: {sum_forekomster / len(ord_antall):.2f}')
