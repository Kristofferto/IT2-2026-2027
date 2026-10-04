# IT2 fagdag - prosjekt, løsningsforslag


import random

# ============================================================
# PROSJEKT A - KARAKTERBOKA
# ============================================================

karakterer = {
    'Kari': [5, 4, 6, 5],
    'Ola': [3, 4, 4, 2],
    'Ali': [6, 6, 5, 6],
    'Mia': [4, 3, 4, 4],
    'Jonas': [2, 3, 3, 4],
}

# A5: legg til og utvid
karakterer['Nora'] = [5, 5, 4]
karakterer['Ola'].append(5)

# A1 til A4: tabellen
bredde = 0
for navn in karakterer:
    if len(navn) > bredde:
        bredde = len(navn)
bredde += 2

print(f'{"Navn":<{bredde}}{"Karakterer":<20}{"Snitt":>7}')
print(f'{"-" * (bredde + 27)}')

beste_navn = ''
beste_snitt = 0
svakeste_navn = ''
svakeste_snitt = 6

for navn, tall in karakterer.items():
    sum_karakterer = 0
    for k in tall:
        sum_karakterer += k
    snitt = sum_karakterer / len(tall)
    som_tekst = ', '.join(str(k) for k in tall)
    print(f'{navn:<{bredde}}{som_tekst:<20}{snitt:>7.1f}')

    if snitt > beste_snitt:
        beste_navn = navn
        beste_snitt = snitt
    if snitt < svakeste_snitt:
        svakeste_navn = navn
        svakeste_snitt = snitt

print(f'{"-" * (bredde + 27)}')
print(f'Best:    {beste_navn} ({beste_snitt:.1f})')
print(f'Svakest: {svakeste_navn} ({svakeste_snitt:.1f})')

# Utvidelse: klassens snitt og fordeling
alle = []
fordeling = {}

for tall in karakterer.values():
    for k in tall:
        alle.append(k)
        if k in fordeling:
            fordeling[k] += 1
        else:
            fordeling[k] = 1

sum_alle = 0
for k in alle:
    sum_alle += k

print(f'Klassens snitt: {sum_alle / len(alle):.2f}')

for k in sorted(fordeling):
    print(f'  {k}: {"*" * fordeling[k]}')


# ============================================================
# PROSJEKT B - MINESVEIPER
# ============================================================

random.seed(2026)

RADER = 8
KOLONNER = 8
BOMBER = 10

# B1: tomt brett
brett = []

for r in range(RADER):
    rad = []
    for k in range(KOLONNER):
        rad.append(0)
    brett.append(rad)

# B2: plasser bomber
lagt_ut = 0

while lagt_ut < BOMBER:
    r = random.randint(0, RADER - 1)
    k = random.randint(0, KOLONNER - 1)
    if brett[r][k] != -1:
        brett[r][k] = -1
        lagt_ut += 1

# B3: tell naboer
for r in range(RADER):
    for k in range(KOLONNER):
        if brett[r][k] == -1:
            continue
        naboer = 0
        for dr in range(-1, 2):
            for dk in range(-1, 2):
                nr = r + dr
                nk = k + dk
                if nr < 0 or nr >= RADER or nk < 0 or nk >= KOLONNER:
                    continue  # utenfor brettet
                if brett[nr][nk] == -1:
                    naboer += 1
        brett[r][k] = naboer

# B4: skriv ut
print()
print(f'{"":>3}', end='')
for k in range(KOLONNER):
    print(f'{k:>3}', end='')
print()

for r in range(RADER):
    print(f'{r:>3}', end='')
    for k in range(KOLONNER):
        if brett[r][k] == -1:
            print(f'{"*":>3}', end='')
        elif brett[r][k] == 0:
            print(f'{".":>3}', end='')
        else:
            print(f'{brett[r][k]:>3}', end='')
    print()
