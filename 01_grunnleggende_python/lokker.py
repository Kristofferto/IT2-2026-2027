# IT2 1C - Løkker
# Oppgaver: se boka
# Marker en seksjon og kjør med Shift+Enter.

# 1. for med range

for i in range(5):
    print(i)

# range(5) gir 0, 1, 2, 3, 4. Fem tall, men den stopper FØR 5.
# i er en helt vanlig variabel som får en ny verdi for hver runde.

for i in range(5):
    print(f'Runde {i + 1} av 5')


# 2. range med start, slutt og steg

for i in range(1, 6):  # 1 til 5
    print(i)

for i in range(0, 21, 5):  # 0, 5, 10, 15, 20
    print(i)

for i in range(10, 0, -1):  # baklengs
    print(i)

print('Ferdig!')


# 3. Løkke gjennom en tekst

ord_tekst = 'datamaskin'

for bokstav in ord_tekst:
    print(bokstav)

# Her trenger vi ikke indeks i det hele tatt.
# Løkka henter ett tegn av gangen, fra første til siste.


# 4. Løkke gjennom en liste

# En liste er flere verdier i én variabel. Mer om dette på fagdagen.
frukt = ['eple', 'pære', 'banan', 'appelsin']

for vare in frukt:
    print(vare)

print(len(frukt))
print(frukt[0])

# Trenger du nummeret på hvert element, kan du løkke over indeksene:
for i in range(len(frukt)):
    print(f'{i + 1}. {frukt[i]}')


# 5. Summere og telle

sum_tall = 0

for i in range(1, 101):
    sum_tall = sum_tall + i

print(f'Summen av 1 til 100 er {sum_tall}')

# Mønsteret: lag en variabel FØR løkka, oppdater den INNI.
# Glemmer du å lage den først, får du NameError.

antall_a = 0

for bokstav in 'datamaskin':
    if bokstav == 'a':
        antall_a = antall_a + 1

print(f'Ordet har {antall_a} a-er')


# 6. while

tall = 1

while tall <= 5:
    print(tall)
    tall = tall + 1  # uten denne stopper løkka ALDRI

# for brukes når du vet hvor mange runder.
# while brukes når du ikke vet det.

sparing = 1000

while sparing < 2000:
    sparing = sparing * 1.05

print(f'Beløpet er nå {sparing:.2f}')

# Går en løkke i evig loop: trykk Ctrl + C i terminalen.


# 7. break og continue

for i in range(10):
    if i == 5:
        break  # hopp helt ut av løkka
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue  # hopp over resten av denne runden
    print(i)


# 8. Validering av brukerinput
# Vi spør på nytt til brukeren skriver noe som duger.

alder = input('Hvor gammel er du? ')

while not alder.isdigit():
    print('Skriv et helt tall.')
    alder = input('Hvor gammel er du? ')

alder = int(alder)
print(f'Du er {alder} år.')

# isdigit() sjekker at teksten bare inneholder siffer.
# Uten den krasjer int() på alt annet enn tall.


# 9. Feller

# range(5) stopper på 4, ikke 5
for i in range(3):
    print(i)  # 0, 1, 2

# Variabelen lever videre etter løkka
print(f'Etter løkka er i lik {i}')

# En while som aldri endrer betingelsen kjører for alltid:
#   tall = 1
#   while tall <= 5:
#       print(tall)          <- tall endres aldri
