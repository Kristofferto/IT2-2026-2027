"""
IT2 onsdag - LØSNINGSFORSLAG

Kantinekassa (oppgave 4) bruker input(). Sett KJOR_KASSA = True
når du skal vise den.
"""

KJOR_KASSA = False

"""
1. KARAKTERBOKA MED FAG
"""

skole = {
    'Kari': {'matte': 5, 'norsk': 4, 'it2': 6},
    'Ola': {'matte': 3, 'norsk': 4, 'it2': 4},
    'Ali': {'matte': 6, 'norsk': 5, 'it2': 6},
    'Mia': {'matte': 4, 'norsk': 3, 'it2': 4},
}

skole['Jonas'] = {'matte': 3, 'norsk': 4, 'it2': 3}
skole['Kari']['engelsk'] = 5

# a og b
beste_navn = ''
beste_snitt = 0

for navn, fag in skole.items():
    sum_karakterer = 0
    antall = 0
    linje = ''
    for fagnavn, karakter in fag.items():
        sum_karakterer += karakter
        antall += 1
        linje += f'{fagnavn} {karakter}   '
    snitt = sum_karakterer / antall
    print(f'{navn:<8}{linje:<40}{snitt:>5.1f}')
    if snitt > beste_snitt:
        beste_navn = navn
        beste_snitt = snitt

print(f'Best: {beste_navn} ({beste_snitt:.1f})')

# c og d: snitt per fag
fagsum = {}
fagantall = {}

for fag in skole.values():
    for fagnavn, karakter in fag.items():
        if fagnavn in fagsum:
            fagsum[fagnavn] += karakter
            fagantall[fagnavn] += 1
        else:
            fagsum[fagnavn] = karakter
            fagantall[fagnavn] = 1

svakest = ''
lavest = 7

for fagnavn in sorted(fagsum):
    snitt = fagsum[fagnavn] / fagantall[fagnavn]
    print(f'{fagnavn:<10}{snitt:>5.2f}')
    if snitt < lavest:
        svakest = fagnavn
        lavest = snitt

print(f'Svakest: {svakest} ({lavest:.2f})')


"""
2. KONTAKTLISTA
"""

kontakter = {
    'Kari': {'telefon': '99887766', 'epost': 'kari@skole.no', 'klasse': '2A'},
    'Ola': {'telefon': '91234567', 'epost': 'ola@skole.no', 'klasse': '2B'},
    'Ali': {'telefon': '48001122', 'epost': 'ali@skole.no', 'klasse': '2A'},
}

print(f'{"Navn":<8}{"Telefon":<12}{"E-post":<20}{"Klasse":<8}')
print('-' * 48)

for navn, info in kontakter.items():
    print(f'{navn:<8}{info["telefon"]:<12}{info["epost"]:<20}{info["klasse"]:<8}')

sok = 'Ola'
funnet = kontakter.get(sok)

if funnet == None:
    print(f'Fant ingen som heter {sok}.')
else:
    print(f'{sok}: {funnet["telefon"]}')

print('Elever i 2A:')
for navn, info in kontakter.items():
    if info['klasse'] == '2A':
        print(f'  {navn}')


"""
3. LAGERBEHOLDNING
"""

lager = {
    'Oslo': {'melk': 12, 'brød': 30, 'kaffe': 8},
    'Bergen': {'melk': 5, 'brød': 22},
    'Tromsø': {'melk': 0, 'kaffe': 15, 'te': 9},
}

for butikk, varer in lager.items():
    print(butikk)
    for vare, antall in varer.items():
        print(f'   {vare:<10}{antall:>4}')

# b) melk til sammen
sum_melk = 0
for varer in lager.values():
    if 'melk' in varer:
        sum_melk += varer['melk']

print(f'Melk totalt: {sum_melk}')

# c) utsolgt
print('Utsolgt:')
for butikk, varer in lager.items():
    for vare, antall in varer.items():
        if antall == 0:
            print(f'   {vare} i {butikk}')

# d) total per vare
totalt = {}

for varer in lager.values():
    for vare, antall in varer.items():
        if vare in totalt:
            totalt[vare] += antall
        else:
            totalt[vare] = antall

for vare in sorted(totalt):
    print(f'{vare:<10}{totalt[vare]:>4}')

# e) størst butikk
storst = ''
flest = 0

for butikk, varer in lager.items():
    sum_butikk = 0
    for antall in varer.values():
        sum_butikk += antall
    if sum_butikk > flest:
        storst = butikk
        flest = sum_butikk

print(f'Flest varer: {storst} ({flest})')


"""
4. KANTINEKASSA
"""

meny = {
    'kaffe': {'pris': 25.00, 'antall': 40},
    'bolle': {'pris': 32.00, 'antall': 15},
    'baguett': {'pris': 59.00, 'antall': 8},
    'juice': {'pris': 28.00, 'antall': 20},
}

bredde = 0
for vare in meny:
    if len(vare) > bredde:
        bredde = len(vare)
bredde += 2

print(f'{"Vare":<{bredde}}{"Pris":>8}{"Igjen":>8}')
print('-' * (bredde + 16))

for vare, info in meny.items():
    print(f'{vare:<{bredde}}{info["pris"]:>8.2f}{info["antall"]:>8}')

if KJOR_KASSA:
    bestilling = {}

    while True:
        vare = input('Vare (eller ferdig): ').lower()

        if vare == 'ferdig':
            break

        if vare not in meny:
            print('Den varen finnes ikke.')
            continue

        antall = input('Antall: ')

        if not antall.isdigit():
            print('Skriv et helt tall.')
            continue

        antall = int(antall)

        if antall > meny[vare]['antall']:
            print(f'Bare {meny[vare]["antall"]} igjen.')
            continue

        meny[vare]['antall'] -= antall

        if vare in bestilling:
            bestilling[vare] += antall
        else:
            bestilling[vare] = antall

    # Kvittering
    print()
    print(f'{"Vare":<{bredde}}{"Ant":>5}{"Pris":>9}{"Sum":>9}')
    print('-' * (bredde + 23))

    total = 0

    for vare, antall in bestilling.items():
        pris = meny[vare]['pris']
        linjesum = antall * pris
        total += linjesum
        print(f'{vare:<{bredde}}{antall:>5}{pris:>9.2f}{linjesum:>9.2f}')

    print('-' * (bredde + 23))
    print(f'{"Totalt":<{bredde}}{"":>5}{"":>9}{total:>9.2f}')

    print('Utsolgt:')
    for vare, info in meny.items():
        if info['antall'] == 0:
            print(f'   {vare}')
else:
    print('(KJOR_KASSA er False - sett den til True øverst i fila.)')
