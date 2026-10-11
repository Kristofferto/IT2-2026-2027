"""
IT2 - REPETISJON, LØSNINGSFORSLAG

Oppgave 12 og 13 bruker input(). Sett INPUT_PA = True for å vise dem.
"""

INPUT_PA = False

"""
1. BADMINTON
"""


def badminton(per_vil, palle_vil, espen_vil):
    antall = 0
    for vil in [per_vil, palle_vil, espen_vil]:
        if vil:
            antall += 1
    return antall == 2


print(badminton(True, True, False), badminton(True, True, True))


"""
2. POENG
"""


def poeng(kort):
    if kort == 'lyn':
        return 0
    return len(kort)


print(poeng('hjerte'), poeng('lyn'), poeng('firkløver'))


"""
3. JAGES
"""


def jages(dyreliste):
    for jeger in dyreliste:
        for bytte in dyreliste:
            if jeger == 'hund' and bytte == 'katt':
                return True
            if jeger == 'katt' and bytte == 'mus':
                return True
    return False


print(jages(['mus', 'katt']), jages(['mus', 'mus', 'hund']))


"""
4. POENGSUM
"""


def poengsum(kort_liste):
    sum_poeng = 0
    for kort in kort_liste:
        sum_poeng += poeng(kort)
    return sum_poeng


print(poengsum(['hjerte', 'lyspære']))


"""
5. BORDSETTING
"""


def bordsetting(introverte, ekstroverte):
    rekke = []
    for i in range(len(introverte)):
        rekke.append(introverte[i])
        rekke.append(ekstroverte[i])
    return rekke


print(bordsetting(['Per', 'Palle'], ['Kari', 'Mia']))


"""
6. FELLES
"""


def felles(tall_lister):
    telling = {}
    for liste in tall_lister:
        for verdi in liste:
            if verdi in telling:
                telling[verdi] += 1
            else:
                telling[verdi] = 1

    svar = []
    for verdi, antall in telling.items():
        if antall >= 2:
            svar.append(verdi)
    return svar


print(felles([[1, 5, 1], [3, 4], [2, 3]]))


"""
7. ADSKILT
"""


def minste(liste):
    beste = liste[0]
    for verdi in liste:
        if verdi < beste:
            beste = verdi
    return beste


def storste(liste):
    beste = liste[0]
    for verdi in liste:
        if verdi > beste:
            beste = verdi
    return beste


def adskilt(tall_lister):
    for i in range(len(tall_lister)):
        for j in range(len(tall_lister)):
            if i == j:
                continue
            if minste(tall_lister[i]) > storste(tall_lister[j]):
                return True
    return False


print(adskilt([[1, 10], [6, 8], [2, 3]]))
print(adskilt([[1, 10], [6, 8], [2, 3, 7]]))


"""
8. HEIE
"""


def heie(tabell):
    if tabell['Brann'] <= 3:
        return 'Brann'
    for lag, plass in tabell.items():
        if plass == 1:
            return lag


print(heie({'Rosenborg': 4, 'Odd': 1, 'Molde': 3, 'Brann': 2}))
print(heie({'Rosenborg': 2, 'Odd': 1, 'Molde': 3, 'Brann': 4}))


"""
9. FLERTALL
"""


def flertall(dyreliste):
    telling = {}
    for dyr in dyreliste:
        if dyr in telling:
            telling[dyr] += 1
        else:
            telling[dyr] = 1

    beste = ''
    flest = 0
    uavgjort = False

    for dyr, antall in telling.items():
        if antall > flest:
            beste = dyr
            flest = antall
            uavgjort = False
        elif antall == flest:
            uavgjort = True

    if uavgjort:
        return 'uavgjort'
    return beste


print(flertall(['ulv', 'sau', 'ulv']), flertall(['ulv', 'sau', 'sau', 'ulv']))


"""
10. UTVIDET JAGES
"""


def utvidet_jages(dyreliste, jaging):
    for jeger in dyreliste:
        if jeger in jaging and jaging[jeger] in dyreliste:
            return True
    return False


print(utvidet_jages(['ulv', 'mus', 'sau'], {'ulv': 'sau'}))
print(utvidet_jages(['ulv', 'mus', 'hund'], {'ulv': 'sau', 'katt': 'mus'}))


"""
11. INTERESSEGRUPPER
"""


def lag_interessegrupper(personers_interesse):
    grupper = {}
    for person, interesse in personers_interesse.items():
        if interesse not in grupper:
            grupper[interesse] = []
        grupper[interesse].append(person)
    return grupper


print(lag_interessegrupper({'Per': 'Mat', 'Palle': 'Film', 'Espen': 'Mat'}))


"""
12. FORENKLE MED EN FUNKSJON
"""


def les_tekst(sporsmal):
    """Leser inn en ikke-tom tekst fra bruker."""
    svar = input(sporsmal)
    while len(svar) == 0:
        print('Ugyldig verdi!')
        svar = input(sporsmal)
    return svar


"""
13. VELG
"""


def velg(liste):
    """Lar brukeren velge et element ved å oppgi en gyldig indeks."""
    indeks = int(input('Velg indeks: '))
    while indeks < 0 or indeks >= len(liste):
        indeks = int(input('Velg indeks: '))
    return liste[indeks]


if INPUT_PA:
    navn = les_tekst('Skriv inn navn: ')
    print(f'Velkommen, {navn}!')

    reisemal = les_tekst('Skriv inn hvor du skal: ')
    print(f'God tur til {reisemal}!')

    print(velg(['eple', 'pære', 'banan']))
else:
    print('(INPUT_PA er False - sett den til True for oppgave 12 og 13.)')


"""
14. STIGESPILLET
"""


def stigespill(terningkast, stiger):
    posisjon = 0
    for kast in terningkast:
        posisjon += kast
        if posisjon in stiger:
            posisjon = stiger[posisjon]
    return posisjon


print(stigespill([5, 4, 2, 2], {5: 12, 18: 7}))


"""
15. HVILKE TRE KAST?
"""


def hvilke_tre_kast(slutt_rute, stiger):
    muligheter = []
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                if stigespill([a, b, c], stiger) == slutt_rute:
                    muligheter.append([a, b, c])
    return muligheter


print(hvilke_tre_kast(5, {3: 15, 17: 4}))


"""
16. TELLEFUNKSJON
"""


def tell_og_skriv_ut(elementer):
    """Teller forekomster i en liste og skriver ut antallet av hver."""
    telling = {}
    for element in elementer:
        if element not in telling:
            telling[element] = 0
        telling[element] += 1
    for element in telling:
        print('Antall', element, ':', telling[element])


tell_og_skriv_ut(['F', 'E', 'R', 'S', 'K', 'E', 'N'])
tell_og_skriv_ut(['flodhest', 'er', 'best', 'ingen', 'protest'])
