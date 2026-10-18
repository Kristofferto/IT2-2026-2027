# IT2 3B - reelle datasett, økt 1
# Filer, CSV og JSON
# Datafilene ligger i mappa data/

import csv
import json

import matplotlib.pyplot as plt

# 1. Lese en hel fil

with open('data/temperaturer.txt', encoding='utf-8') as fil:
    innhold = fil.read()

print(innhold)

# with sørger for at fila lukkes, også hvis noe krasjer.
# encoding forteller hvordan tegnene er lagret. Mer om det i del 6.


# 2. Lese linje for linje

with open('data/temperaturer.txt', encoding='utf-8') as fil:
    for linje in fil:
        print(linje.strip())

# strip() fjerner linjeskiftet på slutten.
# Uten den får du en blank linje mellom hver.


# 3. Dele opp hver linje

måneder = []
temperaturer = []

with open('data/temperaturer.txt', encoding='utf-8') as fil:
    for linje in fil:
        deler = linje.strip().split(' ')
        måneder.append(deler[0])
        temperaturer.append(float(deler[1]))

print(måneder[0], temperaturer[0])

# Teksten fra fila er alltid tekst. float() eller int() må til.


# 4. Skrive til fil

with open('resultat.txt', 'w', encoding='utf-8') as fil:
    fil.write('Varme måneder\n')
    for i in range(len(måneder)):
        if temperaturer[i] > 10:
            fil.write(f'{måneder[i]}\t{temperaturer[i]}\n')

with open('resultat.txt', 'a', encoding='utf-8') as fil:
    fil.write('Ferdig\n')

# 'w' starter fila på nytt. 'a' legger til på slutten.
# \n er linjeskift, \t er tabulator.


# 5. CSV

with open('data/vaer_oslo.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    overskrifter = next(innhold)
    print(overskrifter)
    for rad in innhold:
        print(rad)

# csv.reader deler hver linje ved skilletegnet og gir oss en liste.
# next() henter én linje, her overskriftene. For-løkka tar resten.


# 6. Encoding

# Encoding er oppskriften tegnene ble lagret med. Vi må lese med samme oppskrift.

with open('data/vaer_oslo.csv', encoding='utf-8') as fil:
    innhold = csv.reader(fil, delimiter=';')
    print(next(innhold))

# '\ufeffManed': Excel legger et usynlig tegn først i fila. utf-8-sig fjerner det.

with open('frukt.txt', 'w', encoding='utf-8') as fil:
    fil.write('Blåbær og grønnsaker\n')

with open('frukt.txt', encoding='latin-1') as fil:
    print(fil.read())

# Feil oppskrift gir BlÃ¥bÃ¦r. Ingen feilmelding, bare rare tegn. Det er det verste.
# Leser vi en latin-1-fil med utf-8, krasjer det i stedet. Fjern # og kjør:
#
# with open('data/ssbmedier.csv', encoding='utf-8') as fil:
#     print(fil.read())
#
# Start med utf-8. Krasjer det, prøv latin-1.
# Står det \ufeff foran første kolonnenavn, bruk utf-8-sig.


# 7. Fra CSV til lister vi kan plotte

måneder = []
temperatur = []
nedbør = []

with open('data/vaer_oslo.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)  # hopp over overskriftene
    for rad in innhold:
        måneder.append(rad[0])
        temperatur.append(float(rad[1]))
        nedbør.append(int(rad[2]))

print(måneder)
print(nedbør)


# 8. Regne på det vi leste inn

sum_nedbør = 0
våtest = måneder[0]
mest = nedbør[0]

for i in range(len(måneder)):
    sum_nedbør += nedbør[i]
    if nedbør[i] > mest:
        mest = nedbør[i]
        våtest = måneder[i]

print(f'Totalt {sum_nedbør} mm. Våtest: {våtest} med {mest} mm.')


# 9. Og så tegner vi

plt.bar(måneder, nedbør)
plt.title('Nedbør i Oslo')
plt.xlabel('Måned')
plt.ylabel('Nedbør')
plt.xticks(rotation=45)  # skrå månedsnavn, så de ikke overlapper
plt.tight_layout()
plt.show()

# Dette er hele kjeden: fil inn, tall ut, figur til slutt.
# Det er den dere skal kunne på fagdagen.


# 10. JSON

with open('data/skole.json', encoding='utf-8') as fil:
    skole = json.load(fil)

print(skole)
print(json.dumps(skole, indent=2, ensure_ascii=False))

# json.load() gir ordbøker og lister. Det kan dere fra før.
# json.dumps() med indent gjør utskriften lesbar.


# 11. Grave seg nedover

print(skole['skole'])
print(skole['klasser'][0]['navn'])
print(skole['klasser'][0]['fag'][2])

for klasse in skole['klasser']:
    print(f'{klasse["navn"]:<8}{klasse["antall"]:>4} elever')

# Ordbok inni liste inni ordbok. Les én klamme om gangen, fra venstre.


# 12. Se på fila før du leser den

with open('data/ssbmedier.csv', encoding='latin-1') as fil:
    for i in range(4):
        print(fil.readline().strip())

# Fra SSB: minutter vi bruker på ulike medier en gjennomsnittsdag.
# Fire spørsmål før vi skriver kode:
#   Hva skiller verdiene?              semikolon
#   Hva står over overskriftene?       én tittellinje
#   Hvordan ser et manglende tall ut?  ..
#   Hvilken encoding?                  ikke utf-8: VS Code viser � der det skal stå å


# 13. En stygg fil for hånd

årstall = []
tv = []

with open('data/ssbmedier.csv', encoding='latin-1') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)  # tittellinja
    overskrifter = next(innhold)
    for rad in innhold:
        if rad[0] == 'TV':
            for i in range(1, len(rad)):
                if rad[i] != '..':
                    årstall.append(int(overskrifter[i][-4:]))
                    tv.append(int(rad[i]))

print(årstall)
print(tv)

plt.plot(årstall, tv, marker='o')
plt.title('Tid brukt på TV')
plt.xlabel('Årstall')
plt.ylabel('Minutter per dag')
plt.grid()
plt.show()

# rad[0] er medietypen. De fire siste tegnene i hver overskrift er årstallet.
# if-testen hopper over .. der SSB mangler tall.
# Tittellinje, semikolon, latin-1 og hull: alt for hånd.
# På onsdag gjør pandas det samme i én kommando.
