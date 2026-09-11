# IT2 fagdag - lister, 2D-lister og ordbøker
# Marker en seksjon og kjør med Shift+Enter.


# 1. Lage og bruke lister

frukt = ['eple', 'pære', 'banan', 'appelsin']

print(frukt)
print(len(frukt))
print(frukt[0])  # første
print(frukt[-1])  # siste
print(frukt[1:3])  # utsnitt, som i tekst
print('banan' in frukt)

# Indeksering og utsnitt er helt likt som i tekst.
# Det eneste nye er hva som ligger inni.


# 2. Lister kan endres

frukt[0] = 'plomme'  # dette virker
print(frukt)

# tekst[0] = 'P'  -> TypeError. Tekst kan IKKE endres.
# Det er den store forskjellen.

frukt.append('kiwi')  # legg til bakerst
frukt.insert(1, 'melon')  # legg til på plass 1
frukt.remove('banan')  # fjern en bestemt verdi
sist = frukt.pop()  # ta ut den siste og få den tilbake

print(frukt)
print(f'Tok ut: {sist}')

del frukt[0]
print(frukt)


# 3. Løkke gjennom en liste

tall = [4, 8, 15, 16, 23, 42]

for verdi in tall:
    print(verdi)

# Trenger du nummeret også:
for i in range(len(tall)):
    print(f'{i}: {tall[i]}')

# Bygge en ny liste med en løkke:
doble = []

for verdi in tall:
    doble.append(verdi * 2)

print(doble)


# 4. Regn ut selv med løkke

tall = [4, 8, 15, 16, 23, 42]

# Summen
sum_tall = 0
for verdi in tall:
    sum_tall += verdi

print(sum_tall)

# Snittet
print(f'{sum_tall / len(tall):.2f}')

# Største verdi: hold styr på den beste hittil
storst = tall[0]
for verdi in tall:
    if verdi > storst:
        storst = verdi

print(storst)

# Python har ferdige funksjoner for dette, men de skjuler hva som
# faktisk skjer. Vi regner selv. Mønsteret er alltid det samme:
# lag en variabel FØR løkka, oppdater den INNI.

print(tall.count(15))
print(tall.index(16))  # på hvilken plass ligger 16?

navn = ['Ola', 'Kari', 'Ali', 'Mia']

print(sorted(navn))  # lager en NY sortert liste
print(navn)  # originalen er urørt

navn.sort()  # sorterer lista selv
print(navn)

navn.reverse()
print(navn)


# 5. split og join

setning = 'eple pære banan'

deler = setning.split(' ')  # tekst -> liste
print(deler)

samlet = ', '.join(deler)  # liste -> tekst
print(samlet)

# split() uten argument deler på alle mellomrom
print('Kari  Ola   Ali'.split())


# 6. Kopieringsfella

a = [1, 2, 3]
b = a  # dette er IKKE en kopi

b.append(4)
print(a)  # a ble også endret!

# b = a lager bare et nytt navn på den samme lista.
# Tegn to piler til samme boks.

a = [1, 2, 3]
b = a.copy()  # dette er en ekte kopi

b.append(4)
print(a, b)


# 7. 2D-lister

brett = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(brett[1])  # hele rad nummer 1
print(brett[1][2])  # rad 1, kolonne 2

# RAD FØRST, SÅ KOLONNE.

brett[0][0] = 99
print(brett[0])

print(len(brett))  # antall rader
print(len(brett[0]))  # antall kolonner


# 8. Løkke gjennom 2D

for rad in brett:
    print(rad)

for rad in brett:
    for verdi in rad:
        print(f'{verdi:>4}', end='')
    print()

# Med indekser, når du trenger å vite hvor du er:
for r in range(len(brett)):
    for k in range(len(brett[r])):
        print(f'({r},{k}) = {brett[r][k]}')


# 9. Bygge et 2D-brett

rutenett = []

for r in range(3):
    rad = []
    for k in range(4):
        rad.append(0)
    rutenett.append(rad)

print(rutenett)


# 10. Ordbøker

# Problemet ordboka løser: to lister som må holdes i takt.
navn = ['Kari', 'Ola', 'Ali']
karakter = [5, 4, 6]
print(karakter[navn.index('Kari')])  # tungvint og skjørt

# Ordbok: slå opp på navn i stedet for nummer.
karakterer = {'Kari': 5, 'Ola': 4, 'Ali': 6}

print(karakterer['Kari'])
print(len(karakterer))

karakterer['Mia'] = 3  # legg til
karakterer['Ola'] = 5  # endre
del karakterer['Ali']  # slett

print(karakterer)

print('Kari' in karakterer)  # in sjekker NØKLER, ikke verdier
print(karakterer.get('Finnes ikke', 0))  # trygg oppslag med standardverdi


# 11. Løkke gjennom en ordbok

karakterer = {'Kari': 5, 'Ola': 4, 'Ali': 6}

for navn in karakterer:
    print(navn)

for navn in karakterer.keys():
    print(navn)

for tall in karakterer.values():
    print(tall)

for navn, tall in karakterer.items():
    print(f'{navn:<8}{tall}')


# 12. Verdien kan være en liste

resultater = {
    'Kari': [5, 4, 6],
    'Ola': [3, 4, 4],
    'Ali': [6, 6, 5],
}

print(resultater['Kari'])
print(resultater['Kari'][0])

for navn, karakterer in resultater.items():
    sum_karakterer = 0
    for k in karakterer:
        sum_karakterer += k
    print(f'{navn:<8}{sum_karakterer / len(karakterer):>6.2f}')


# 13. Telling med ordbok

tekst = 'programmering'
antall = {}

for bokstav in tekst:
    if bokstav in antall:
        antall[bokstav] = antall[bokstav] + 1
    else:
        antall[bokstav] = 1

print(antall)

# Dette er ordbokas beste triks. Du vet ikke på forhånd hvilke
# nøkler du trenger - de lages underveis.


# 14. Når liste, når ordbok?

# LISTE   når rekkefølgen betyr noe, eller når tingene er like
#         karakterer i en prøve, plasser i et brett, ord i en setning
#
# ORDBOK  når du slår opp på et navn
#         karakter per elev, pris per vare, antall per bokstav
