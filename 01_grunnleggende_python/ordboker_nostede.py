# IT2 onsdag - nøstede ordbøker


# 1. En ordbok inni en ordbok

# På fagdagen hadde dere en liste som verdi:
resultater = {'Kari': [5, 4, 6]}

# Men hva om karakterene hører til ulike fag?
skole = {
    'Kari': {'matte': 5, 'norsk': 4, 'it2': 6},
    'Ola': {'matte': 3, 'norsk': 4, 'it2': 4},
}

print(skole['Kari'])  # hele den indre ordboka
print(skole['Kari']['matte'])  # ett tall

# YTTERSTE NØKKEL FØRST, så den indre.
# Nøyaktig samme mønster som brett[rad][kolonne].


# 2. Endre og legge til

skole['Kari']['norsk'] = 5  # endre
skole['Kari']['engelsk'] = 4  # nytt fag for Kari
skole['Ali'] = {'matte': 6}  # ny elev

print(skole['Kari'])
print(skole['Ali'])

# Dette går IKKE:
#   skole['Mia']['matte'] = 5   -> KeyError
# Mia finnes ikke ennå, så det er ingenting å legge noe inn i.
# Den ytre nøkkelen må lages først:

skole['Mia'] = {}
skole['Mia']['matte'] = 5

print(skole['Mia'])


# 3. Løkke gjennom to nivåer

for navn, fag in skole.items():
    print(navn)
    for fagnavn, karakter in fag.items():
        print(f'   {fagnavn:<10}{karakter}')


# 4. Regne ut på tvers

# Snitt per elev
for navn, fag in skole.items():
    sum_karakterer = 0
    antall = 0
    for karakter in fag.values():
        sum_karakterer += karakter
        antall += 1
    print(f'{navn:<8}{sum_karakterer / antall:>5.1f}')

# Snitt i matte for hele klassen
sum_matte = 0
antall = 0

for fag in skole.values():
    if 'matte' in fag:  # ikke alle har alle fag
        sum_matte += fag['matte']
        antall += 1

print(f'Matte: {sum_matte / antall:.2f}')


# 5. Når trenger du to nivåer?

# ETT nivå   navn -> karakter
# TO nivåer  navn -> fag -> karakter
#
# Spør deg selv: trenger jeg to opplysninger for å finne fram?
# Trenger du både navn OG fag, er svaret to nivåer.
