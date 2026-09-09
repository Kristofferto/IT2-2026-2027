# Løkker i python

# for og while løkker

# enkel for løkked med range

for i in range(5):
    print(f'Runde {i + 1} av 5')


for i in range(50, 1, -1):
    print(i)


ord = 'datamaskin'

for bokstav in ord:
    print(bokstav)

handleliste = [
    'eple',
    'vaniljekrem',
    'sukker',
    'mel',
    'kanel',
    'smør',
    'vaniljesukker',
    'bakepulver',
]

for vare in handleliste:
    print(vare)

for vare in handleliste:
    for bokstav in vare:
        print(bokstav)

# jeg vil ha antall varer i lista OG antall bokstaver totalt i handleisten

antall_varer = 0
antall_bokstaver = 0
for vare in handleliste:
    antall_varer += 1
    for bokstav in vare:
        antall_bokstaver += 1

print(f'Antall varer i handlelisten er {antall_varer}.')
print(f'Antall bokstaver totalt i handlelisten er {antall_bokstaver}.')

# while løkker

tall = 1

while tall <= 100:
    print('jadda')
    tall += 1

# avslutte løkker når vi vil
for i in range(10):
    if i == 5:
        break

    print(i)


while True:
    tall += 10

    if tall == 10000:
        break
