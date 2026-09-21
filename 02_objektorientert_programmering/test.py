# noestede_ordboker.py

resultater = {'Kari': [5, 4, 6]}


skole = {
    'Kari': {'matte': 5, 'norsk': 4, 'it2': 6},
    'Ola': {'matte': 6, 'norsk': 3, 'it2': 5},
}

print(skole['Kari'])
print(skole['Kari']['it2'])

# endre, slette, lage ny osv osv...
skole['Kari']['norsk'] = 5
skole['Kari']['engelsk'] = 3
skole['Gunnar'] = {'matte': 6, 'gym': 4}
# skole['Mari']['religion'] = 4
print(skole)

for elev, fag in skole.items():
    print(f'{elev} har følgende fag og karakterer:')
    for fagnavn, karakter in fag.items():
        print(f'{fagnavn}: {karakter}')

# snitt per elev
for navn, fag in skole.items():
    sum_karakterer = 0
    antall_fag = 0
    for fag_navn, karakter in fag.items():
        sum_karakterer += karakter
        antall_fag += 1
    print(f'{navn} har snittet {sum_karakterer / antall_fag}')
