"""
IT2 mandag - LØSNINGSFORSLAG

Testverdiene er skrevet rett inn så fila kan kjøres i sin helhet.
"""

import random

"""
1. TERNINGSYMBOLER
"""

random.seed(2026)

symbol = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}

kast = random.randint(1, 6)
print(f'{kast} {symbol[kast]}')

telling = {}
linje = ''

for i in range(10):
    kast = random.randint(1, 6)
    linje += symbol[kast] + ' '
    if kast in telling:
        telling[kast] += 1
    else:
        telling[kast] = 1

print(linje)

for verdi in sorted(telling):
    print(f'{symbol[verdi]}  {telling[verdi]}')


"""
2. KARAKTERBESKRIVELSE
"""

beskrivelse = {
    1: 'svært lav',
    2: 'lav',
    3: 'nokså god',
    4: 'god',
    5: 'meget god',
    6: 'fremragende',
}

for karakter in sorted(beskrivelse):
    print(f'{karakter}  {beskrivelse[karakter]}')

print(beskrivelse.get(7, 'finnes ikke'))


"""
3. MÅNEDER
"""

navn = {
    1: 'januar',
    2: 'februar',
    3: 'mars',
    4: 'april',
    5: 'mai',
    6: 'juni',
    7: 'juli',
    8: 'august',
    9: 'september',
    10: 'oktober',
    11: 'november',
    12: 'desember',
}

dager = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

aar = 2024

if aar % 4 == 0 and (aar % 100 != 0 or aar % 400 == 0):
    dager[2] = 29

sum_dager = 0

for nummer in sorted(navn):
    print(f'{nummer:>3}  {navn[nummer]:<12}{dager[nummer]:>4}')
    sum_dager += dager[nummer]

print(f'{aar} har {sum_dager} dager.')


"""
4. FRA ELIF-KJEDE TIL ORDBOK
"""

retninger = {
    0: 'nord',
    1: 'nordøst',
    2: 'øst',
    3: 'sørøst',
    4: 'sør',
    5: 'sørvest',
    6: 'vest',
    7: 'nordvest',
}

retning = 2
print(retninger[retning])
print(retninger.get(11, 'ukjent retning'))

# b) Sytten linjer ble til én. Ordboka er også lettere å rette
#    hvis noe er feil.

# d) motsatt vei
tall_fra_navn = {}

for tall, navn_retning in retninger.items():
    tall_fra_navn[navn_retning] = tall

print(tall_fra_navn['vest'])


"""
5. VALUTA
"""

kurser = {'USD': 10.85, 'EUR': 11.70, 'GBP': 13.40, 'SEK': 1.02}

belop = 1500  # input('Beløp i kroner: ')

for valuta in sorted(kurser):
    print(f'{valuta}  {belop / kurser[valuta]:>10.2f}')

print()

for valuta in sorted(kurser):
    print(f'100 {valuta} = {100 * kurser[valuta]:>8.2f} kr')

print(kurser.get('JPY', 'ukjent valuta'))


"""
6. MORSEKODE
"""

morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'i': '..',
    'k': '-.-',
    'n': '-.',
    'o': '---',
    'r': '.-.',
    's': '...',
    't': '-',
}

ordet = 'kode'
kodet = ''

for bokstav in ordet.lower():
    kodet += morse.get(bokstav, '?') + ' '

print(f'{ordet} -> {kodet.strip()}')


"""
7. TALLORD
"""

tallord = {
    'en': 1,
    'to': 2,
    'tre': 3,
    'fire': 4,
    'fem': 5,
    'seks': 6,
    'sju': 7,
    'åtte': 8,
    'ni': 9,
    'ti': 10,
}

setning = 'tre fem ni to'
sum_tall = 0
storst = 0

for ordet in setning.split():
    verdi = tallord[ordet]
    sum_tall += verdi
    if verdi > storst:
        storst = verdi

print(f'Sum: {sum_tall}, størst: {storst}')

# c) snu ordboka
snudd = {}

for ordet, verdi in tallord.items():
    snudd[verdi] = ordet

print(snudd[7])


"""
8. ROMERTALL
"""

verdier = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

romertall = 'MCMXCIV'
sum_tall = 0

for i in range(len(romertall)):
    verdi = verdier[romertall[i]]
    # Står et mindre tegn foran et større, skal det trekkes fra
    if i + 1 < len(romertall) and verdi < verdier[romertall[i + 1]]:
        sum_tall -= verdi
    else:
        sum_tall += verdi

print(f'{romertall} = {sum_tall}')
