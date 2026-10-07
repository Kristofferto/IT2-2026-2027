# IT2 - å teste funksjoner med assert


# 1. Hva assert gjør

assert 2 + 2 == 4  # sant, ingenting skjer
# assert 2 + 2 == 5   -> AssertionError, programmet stopper

# assert sier: dette MÅ være sant. Er det ikke det, stopper alt.


# 2. Teste en funksjon


def tell_giftige(giftige, plukket):
    teller = 0
    for sopp in plukket:
        if sopp in giftige:
            teller += 1
    return teller


assert tell_giftige(['fluesopp'], ['kantarell', 'fluesopp']) == 1
assert tell_giftige(['fluesopp'], ['fluesopp', 'fluesopp']) == 2

print('tell_giftige: OK')

# Kjører fila uten feilmelding, virker funksjonen på disse tilfellene.


# 3. Kanttilfeller er der feilene bor

assert tell_giftige([], ['fluesopp']) == 0  # ingen er giftige
assert tell_giftige(['fluesopp'], []) == 0  # ingenting plukket

print('kanttilfeller: OK')


# 4. En funksjon som ser riktig ut


def flertall(dyreliste):
    telling = {}
    for dyr in dyreliste:
        if dyr in telling:
            telling[dyr] += 1
        else:
            telling[dyr] = 1

    beste = ''
    flest = 0
    for dyr, antall in telling.items():
        if antall > flest:
            beste = dyr
            flest = antall
    return beste


assert flertall(['ulv', 'sau', 'ulv']) == 'ulv'

print('flertall, eksempelet fra oppgaven: OK')

# Eksempelet går gjennom. Men oppgaven sa også at den skal gi
# 'uavgjort' når to er like vanlige:

# assert flertall(['ulv', 'sau', 'sau', 'ulv']) == 'uavgjort'
#   -> AssertionError

# Funksjonen er altså feil, selv om den besto den første testen.
# Det er dette tester er til for.


# 5. Rettet versjon


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


assert flertall(['ulv', 'sau', 'ulv']) == 'ulv'
assert flertall(['ulv', 'sau', 'sau', 'ulv']) == 'uavgjort'
assert flertall(['sau']) == 'sau'
assert flertall(['a', 'a', 'b', 'c']) == 'a'

print('flertall: OK')


# 6. Melding når testen feiler

assert flertall(['sau']) == 'sau', 'én art alene må vinne'

# Teksten etter komma vises i feilmeldingen. Nyttig når du har mange.


# 7. Fortsette selv om en test feiler

try:
    assert flertall([]) == 'uavgjort'
    print('tom liste: OK')
except AssertionError:
    print('tom liste: FEIL')

# try/except fanger feilen så resten av testene får kjøre.
# Det er slik testfila i dagens konkurranse er bygget.
