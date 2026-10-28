# IT2 - repetisjon før prøven
# En typisk oppgave av hver type. Samme rekkefølge som prøven.

import csv
import json

import matplotlib.pyplot as plt
import pandas as pd


# 1. Funksjon med parameter og returverdi


def snitt(tall):
    """Returnerer gjennomsnittet av tallene i lista."""
    sum_tall = 0
    for t in tall:
        sum_tall += t
    return sum_tall / len(tall)


print(snitt([4, 8, 6]))

# Tre ting sensor ser etter: parameter, return, docstring.
# En funksjon som skriver ut i stedet for å returnere, kan
# ikke brukes videre. print er ikke return.


# 2. Fil inn, tall ut


def les_vaerdata(filnavn):
    """Returnerer to lister: månedsnavn og temperaturer."""
    maneder = []
    temperaturer = []
    with open(filnavn, encoding='utf-8-sig') as fil:
        innhold = csv.reader(fil, delimiter=';')
        next(innhold)  # hopp over overskriftene
        for rad in innhold:
            maneder.append(rad[0])
            temperaturer.append(float(rad[1]))
    return maneder, temperaturer


maneder, temperaturer = les_vaerdata('data/vaer_oslo.csv')

varmest = temperaturer[0]
varmest_navn = maneder[0]
for i in range(len(temperaturer)):
    if temperaturer[i] > varmest:
        varmest = temperaturer[i]
        varmest_navn = maneder[i]

print(f'Snitt: {snitt(temperaturer):.2f}')
print(f'Varmest: {varmest_navn} med {varmest} grader')

# Oppgave 6 på prøven er dette mønsteret: les, regn med løkke, skriv ut.
# Tekst fra fil er ALLTID tekst. float() må til.
# Spør: hva skjer uten next()? Uten utf-8-sig?


# 3. Pandas på en stygg fil

with open('data/ssbmedier.csv', encoding='latin-1') as fil:
    for i in range(3):
        print(fil.readline().strip()[:80])

medier = pd.read_csv(
    'data/ssbmedier.csv',
    skiprows=1,
    sep=';',
    index_col=0,
    na_values='..',
    encoding='latin-1',
)
medier.columns = range(2013, 2026)

print(medier.loc['Radio'].mean())
print(medier[medier[2025] > 50].index)

# Se på fila først. Hver innstilling svarer til noe du ser:
#   tittellinje            skiprows=1
#   semikolon              sep=';'
#   navn først på raden    index_col=0
#   .. der tall mangler    na_values='..'
#   rare tegn i VS Code    encoding='latin-1'
# I pandas er mean() lov. På vanlige lister gjelder løkka.


# 4. JSON

with open('data/skole.json', encoding='utf-8') as fil:
    skole = json.load(fil)

print(skole['klasser'][1]['navn'])
print(skole['klasser'][0]['fag'][2])

# Les én klamme om gangen, fra venstre:
# skole -> 'klasser' gir en liste -> [0] gir første ordbok -> 'fag' gir en liste.


# 5. Graftegning: to figurer i ett vindu

plt.subplot(2, 1, 1)
plt.plot(maneder, temperaturer, marker='o', label='Oslo')
plt.axhline(0, color='grey', linestyle='--')
plt.title('Temperatur')
plt.xlabel('Måned')
plt.ylabel('Grader')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(range(2013, 2026), medier.loc['TV'], marker='o', label='TV')
plt.title('Tid brukt på TV')
plt.xlabel('År')
plt.ylabel('Minutter per dag')
plt.legend()

plt.tight_layout()
plt.savefig('repetisjon.png')  # FØR show
plt.show()

# Tittel og aksetitler er gratis poeng. En figur uten dem er ikke ferdig.
# TV mangler tall for 2020 og 2022. NaN blir hull i linja.
# Spør: hvorfor står 2021 som et punkt alene?


# 6. Les en klasse og forklar hva den gjør


class Konto:
    """En bankkonto med en eier og en saldo."""

    def __init__(self, eier, saldo=0):
        self.eier = eier
        self._saldo = saldo

    def sett_inn(self, belop):
        if belop < 0:
            raise ValueError('Beløpet kan ikke være negativt.')
        self._saldo += belop

    def vis_saldo(self):
        return self._saldo

    def __str__(self):
        return f'{self.eier}: {self._saldo:.2f} kr'


konto = Konto('Kari Nordmann', 500)
konto.sett_inn(250)
print(konto)

# Spørsmål å stille høyt:
#   Hva kjører når vi skriver Konto('Kari Nordmann', 500)?
#   Hva er self?
#   Hvorfor står saldo med understrek?
#   Hva skjer med konto.sett_inn(-100)? Kjører linjene etter?
#   Hva skjer uten __str__?


# 7. Skriv en klasse selv


class Maaling:
    """En temperaturmåling fra ett sted."""

    def __init__(self, sted, temperatur):
        if temperatur < -90:
            raise ValueError('Så kaldt blir det ikke.')
        self.sted = sted
        self.temperatur = temperatur

    def er_frost(self):
        return self.temperatur < 0

    def __str__(self):
        return f'{self.sted}: {self.temperatur} grader'


maalinger = [Maaling('Oslo', -3.2), Maaling('Bergen', 1.4), Maaling('Tromsø', -8.7)]

for m in maalinger:
    if m.er_frost():
        print(m)

try:
    Maaling('Mars', -120)
except ValueError as feil:
    print('Feil fanget:', feil)

# Konstruktør, attributter, en metode, __str__, raise og en liste med objekter.
# Det er nøyaktig nivået som kreves i oppgave 9.
