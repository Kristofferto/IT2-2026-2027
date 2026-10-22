"""
IT2 - funksjoner
LØSNINGSFORSLAG

Oppgave 9 bruker input(). Sett SPILL = True når du skal vise den.
"""

import random

import minmatte

SPILL = False

"""
1. OPPVARMING
"""


def areal(bredde, hoyde):
    return bredde * hoyde


def omkrets(bredde, hoyde):
    return 2 * bredde + 2 * hoyde


def beskriv(bredde, hoyde):
    print(
        f'{bredde} x {hoyde}: areal {areal(bredde, hoyde)}, omkrets {omkrets(bredde, hoyde)}'
    )


beskriv(4, 7)

# d) Med print i stedet for return returnerer funksjonen None,
#    og f-strengen skriver ut None.


"""
2. STANDARDVERDIER OG NAVNGITTE ARGUMENTER
"""


def rente(belop, sats=0.05, aar=1):
    return belop * (1 + sats) ** aar


print(f'{rente(1000):.2f}')
print(f'{rente(1000, 0.03):.2f}')
print(f'{rente(1000, 0.03, 10):.2f}')
print(f'{rente(aar=10, sats=0.03, belop=1000):.2f}')

# d) SyntaxError: non-default argument follows default argument.
#    Parametre med standardverdi må stå sist.


"""
3. RETURNERE FLERE VERDIER
"""


def min_maks_snitt(liste):
    minst = liste[0]
    storst = liste[0]
    sum_tall = 0
    for verdi in liste:
        sum_tall += verdi
        if verdi < minst:
            minst = verdi
        if verdi > storst:
            storst = verdi
    return minst, storst, sum_tall / len(liste)


tall = [12.4, 8.1, 15.7, 3.2, 11.0]
lav, hoy, gjennomsnitt = min_maks_snitt(tall)
print(f'{lav} {hoy} {gjennomsnitt:.2f}')

samlet = min_maks_snitt(tall)
print(samlet)
print(samlet[1])  # d) hent ut den andre verdien


"""
4. TIDLIG RETURN
"""


def finnes(liste, verdi):
    for element in liste:
        if element == verdi:
            return True  # stopper med én gang
    return False


def forste_negative(liste):
    for i in range(len(liste)):
        if liste[i] < 0:
            return i
    return -1


def er_primtall(tall):
    if tall < 2:
        return False
    for deler in range(2, int(tall**0.5) + 1):
        if tall % deler == 0:
            return False
    return True


print(finnes(tall, 15.7))
print(forste_negative([4, 9, -2, 7]))
print(er_primtall(97), er_primtall(91))


"""
5. REKKEVIDDE
"""

antall = 5


def les_antall():
    return antall  # globale variabler kan leses


def endre_antall():
    antall = 99  # lager en NY lokal variabel


def legg_til(liste):
    liste.append(0)


def legg_til_trygt(liste):
    ny = liste.copy()
    ny.append(0)
    return ny


print(les_antall())
endre_antall()
print(antall)

original = [1, 2, 3]
legg_til(original)
print(original)

original = [1, 2, 3]
print(legg_til_trygt(original), original)

# d) Tall sendes som kopi, lister sendes som seg selv. Derfor kan
#    funksjonen endre lista, men ikke tallet.


"""
6. EGET BIBLIOTEK
"""

# Se minmatte.py. Her brukes den:

print(minmatte.summer(tall))
print(f'{minmatte.snitt(tall):.2f}')
print(minmatte.storste(tall), minmatte.minste(tall))


"""
7. FUNKSJONER SOM BYGGER PÅ HVERANDRE
"""


def er_vokal(bokstav):
    return bokstav in 'aeiouyæøå'


def tell_vokaler(ordet):
    antall_vokaler = 0
    for bokstav in ordet:
        if er_vokal(bokstav):
            antall_vokaler += 1
    return antall_vokaler


def vokalandel(setning):
    return tell_vokaler(setning) / len(setning)


print(tell_vokaler('informasjonsteknologi'))
print(f'{vokalandel("informasjonsteknologi"):.1%}')


"""
8. ORDBOK INN OG UT
"""

lager = {'melk': 12, 'brød': 0, 'kaffe': 8}


def totalt_antall(beholdning):
    sum_tall = 0
    for antall_vare in beholdning.values():
        sum_tall += antall_vare
    return sum_tall


def flest_av(beholdning):
    beste = ''
    flest = 0
    for vare, antall_vare in beholdning.items():
        if antall_vare > flest:
            beste = vare
            flest = antall_vare
    return beste


def utsolgt(beholdning):
    tomme = []
    for vare, antall_vare in beholdning.items():
        if antall_vare == 0:
            tomme.append(vare)
    return tomme


def selg(beholdning, vare):
    if vare in beholdning and beholdning[vare] > 0:
        beholdning[vare] -= 1
        return True
    return False


print(totalt_antall(lager), flest_av(lager), utsolgt(lager))
selg(lager, 'melk')
selg(lager, 'melk')
print(lager)

# e) Ordbøker sendes som seg selv, akkurat som lister.


"""
9. TALLSPILL
"""


def trekk_tall():
    return random.randint(1, 100)


def les_gyldig_tall(tekst, lav, hoy):
    svar = input(tekst)
    while not svar.isdigit() or int(svar) < lav or int(svar) > hoy:
        print(f'Skriv et helt tall mellom {lav} og {hoy}.')
        svar = input(tekst)
    return int(svar)


def sjekk(gjett, fasit):
    if gjett < fasit:
        return 'for lavt'
    if gjett > fasit:
        return 'for høyt'
    return 'riktig'


if SPILL:
    fasit = trekk_tall()
    antall_gjett = 0

    while True:
        gjett = les_gyldig_tall('Gjett: ', 1, 100)
        antall_gjett += 1
        svar = sjekk(gjett, fasit)
        print(svar)
        if svar == 'riktig':
            break

    print(f'Du klarte det på {antall_gjett} gjett.')
else:
    print('(SPILL er False - sett den til True øverst i fila.)')

# e) les_gyldig_tall kan brukes i et hvilket som helst program
#    som leser inn tall fra bruker.
