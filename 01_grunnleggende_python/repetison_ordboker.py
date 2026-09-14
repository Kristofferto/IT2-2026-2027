# IT2 mandag - ordbok som oppslagstabell


# 1. Fra elif-kjede til ordbok

h = 4

# Slik gjorde dere det på fagdagen:
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

print(ukedag)

# Samme sak med en ordbok:
ukedager = {
    0: 'lørdag',
    1: 'søndag',
    2: 'mandag',
    3: 'tirsdag',
    4: 'onsdag',
    5: 'torsdag',
    6: 'fredag',
}

print(ukedager[h])

# Sju grener ble til ett oppslag.
# Dette er ordbokas viktigste bruk: en tabell du slår opp i.


# 2. Nøkkelen kan være hva som helst

priser = {'melk': 21.90, 'brød': 34.50, 'kaffe': 89.00}

print(priser['kaffe'])

# \u2680...
symbol = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}

print(symbol[3])


# 3. get() når nøkkelen kanskje ikke finnes

print(priser['melk'])
# print(priser['te'])     -> KeyError, programmet stopper

print(priser.get('te'))  # None, ingen krasj
print(priser.get('te', 0))  # 0 som standardverdi

# Bruk get() når du er usikker på om nøkkelen finnes.
# Bruk vanlig oppslag når den ALLTID skal finnes - da vil du
# faktisk at det smeller hvis noe er galt.


# 4. Slå opp flere ganger etter hverandre

bestilling = ['melk', 'kaffe', 'melk']
total = 0

for vare in bestilling:
    total += priser[vare]

print(f'{total:.2f}')
