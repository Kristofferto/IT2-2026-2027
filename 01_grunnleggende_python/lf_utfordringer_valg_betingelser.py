"""
IT2 1B - UTFORDRINGER, LØSNINGSFORSLAG

Testverdiene er skrevet rett inn så fila kan kjøres i sin helhet.
input()-linja står som kommentar der den hører hjemme.
"""

import numpy as np

"""
1. SKUDDÅR
"""

aar = 1900  # input('Årstall: ')

if aar % 4 == 0 and (aar % 100 != 0 or aar % 400 == 0):
    print(f'{aar} er skuddår.')
else:
    print(f'{aar} er ikke skuddår.')

# c) Parentesen er hele poenget. Uten den blir and/or feil gruppert.
# d) Året er 365,2422 dager. Ett skuddår hvert fjerde år overkorrigerer,
#    så hvert hundrede år hoppes over - og det underkorrigerer igjen,
#    derfor unntaket for 400.


"""
2. ANNENGRADSLIGNING
"""

a, b, c = 1, -3, 2  # input(...)

if a == 0:
    print('Dette er ikke en annengradsligning.')
else:
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + np.sqrt(d)) / (2 * a)
        x2 = (-b - np.sqrt(d)) / (2 * a)
        print(f'To løsninger: x = {x1:.3f} og x = {x2:.3f}')
    elif d == 0:
        print(f'Én løsning: x = {-b / (2 * a):.3f}')
    else:
        print('Ingen reelle løsninger.')


"""
3. TREKANTEN
"""

s1, s2, s3 = 3.0, 4.0, 5.0

if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
    print('Dette er ikke en trekant.')
else:
    if s1 == s2 == s3:
        print('Likesidet trekant.')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('Likebeint trekant.')
    else:
        print('Ulikesidet trekant.')

    # c) rettvinklet, med lengste side som hypotenus
    lang = max(s1, s2, s3)
    kort_kvadrat = s1**2 + s2**2 + s3**2 - lang**2
    if np.isclose(kort_kvadrat, lang**2):
        print('Trekanten er rettvinklet.')

# d) Med 0.3, 0.4 og 0.5 feiler == fordi desimaltall lagres unøyaktig.
#    np.isclose spør om tallene er nær nok, og løser det.


"""
4. TRINNSKATT
"""

inntekt = 350000  # input('Inntekt: ')

if inntekt <= 200000:
    skatt = 0
elif inntekt <= 400000:
    skatt = (inntekt - 200000) * 0.05
elif inntekt <= 800000:
    skatt = 200000 * 0.05 + (inntekt - 400000) * 0.15
else:
    skatt = 200000 * 0.05 + 400000 * 0.15 + (inntekt - 800000) * 0.25

print(f'Inntekt {inntekt:>10,.0f}'.replace(',', ' '))
print(f'Skatt   {skatt:>10,.0f}'.replace(',', ' '))
print(f'Andel   {skatt / inntekt:>10.1%}')

# d) Snur du rekkefølgen, treffer den første grenen nesten alltid,
#    og resten blir aldri sjekket. Rekkefølgen ER logikken.


"""
5. STEIN, SAKS, PAPIR
"""

# stein = 0, saks = 1, papir = 2
spiller1 = 0
spiller2 = 1

resultat = (spiller1 - spiller2) % 3

if resultat == 0:
    print('Uavgjort.')
elif resultat == 2:
    print('Spiller 1 vinner.')
else:
    print('Spiller 2 vinner.')

# a) Med ren if/elif trengs ni grener, eller tre nøstede nivåer.
# c) Modulo-varianten. Med fem valg slår hvert valg de to neste,
#    og da holder det å sjekke om resultatet er 1 eller 2.


"""
6. DE MORGAN
"""

print(f'{"a":<7}{"b":<7}{"not(a and b)":<15}{"(not a) or (not b)":<20}')

a, b = True, True
print(f'{a!s:<7}{b!s:<7}{not (a and b)!s:<15}{(not a) or (not b)!s:<20}')
a, b = True, False
print(f'{a!s:<7}{b!s:<7}{not (a and b)!s:<15}{(not a) or (not b)!s:<20}')
a, b = False, True
print(f'{a!s:<7}{b!s:<7}{not (a and b)!s:<15}{(not a) or (not b)!s:<20}')
a, b = False, False
print(f'{a!s:<7}{b!s:<7}{not (a and b)!s:<15}{(not a) or (not b)!s:<20}')

# Kolonnene er like i alle fire radene. Uttrykkene er logisk like.
# d) Det motsatte av (alder >= 18 and har_billett)
#    er (alder < 18 or ikke_billett).


"""
7. PASSORDSJEKK
"""

passord = 'Sykkel24'  # input('Passord: ')

lang_nok = len(passord) >= 8
har_stor = passord != passord.lower()  # noe endret seg ved lower()
har_liten = passord != passord.upper()
har_siffer = not passord.isalpha()  # ikke bare bokstaver

if lang_nok and har_stor and har_liten and har_siffer:
    print('Passordet er godkjent.')
else:
    print('Passordet er ikke godkjent.')

if not lang_nok:
    print('- må være minst åtte tegn')
if not har_stor:
    print('- mangler stor bokstav')
if not har_liten:
    print('- mangler liten bokstav')
if not har_siffer:
    print('- mangler siffer')

# d) 'Sykkel!!' slipper gjennom. isalpha() er False også når passordet
#    inneholder et tegn som ikke er en bokstav, uansett om det er et
#    siffer eller ikke.


"""
8. UKEDAG
"""

dag = 2
maaned = 9
aar = 2026

if maaned < 3:  # b) januar og februar hører til året før
    maaned = maaned + 12
    aar = aar - 1

K = aar % 100
J = aar // 100

h = (dag + 13 * (maaned + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

if h == 0:
    ukedag = 'lørdag'
elif h == 1:
    ukedag = 'søndag'
elif h == 2:
    ukedag = 'mandag'
elif h == 3:
    ukedag = 'tirsdag'
elif h == 4:
    ukedag = 'onsdag'
elif h == 5:
    ukedag = 'torsdag'
else:
    ukedag = 'fredag'

print(f'Datoen var en {ukedag}.')

# d) Med vanlig divisjon blir mellomregningene desimaltall,
#    og % 7 gir et desimaltall som aldri treffer noen av grenene.
