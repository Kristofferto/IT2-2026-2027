# IT2 - løsningsforslag til utfordringene

import random

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap


# OPPGAVE 1 - TALLSPILL (eksamen H2025, oppgave 4)

# a) Algoritmen sorterer sifrene i tallet, lager det største og det minste
#    tallet sifrene kan gi, og trekker det minste fra det største.
#    Svaret blir nytt tall, og slik fortsetter den til svaret blir det samme
#    som tallet den startet runden med. For firesifrede tall er det 6174,
#    fordi 7641 - 1467 = 6174.


# b) og c) Sifrene lages med f'{tall:04d}', som fyller på med nuller foran.
def ett_steg(tall):
    sifre = sorted(f'{tall:04d}')
    stigende = int(''.join(sifre))
    synkende = int(''.join(sifre[::-1]))
    return synkende, stigende, synkende - stigende


def tallspill(tall, vis=True):
    """Returnerer tallet algoritmen ender på og hvor mange runder den trengte."""
    # d) Fire like sifre gir 0 - 0 = 0, og da kommer vi aldri til 6174.
    tekst = f'{tall:04d}'
    if tekst == tekst[0] * 4:
        if vis:
            print(f'{tall} har fire like sifre. Da blir svaret 0 hver gang.')
        return 0, 0
    runder = 0
    while True:
        synkende, stigende, nytt_tall = ett_steg(tall)
        runder += 1
        if vis:
            print(f'{tall:04d} -> {synkende:04d} - {stigende:04d} = {nytt_tall:04d}')
        if nytt_tall == tall:
            return tall, runder
        tall = nytt_tall


# tall = int(input('Skriv et firesifret tall: '))
for tall in [3142, 2111, 1000, 5555]:
    tallspill(tall)
    print()

# e) Alle tall ender på 6174. Siste runde er den som gir 6174 en gang til,
#    så her telles rundene til tallet ikke endrer seg.
antall_med_runder = {}
for tall in range(1000, 10000):
    if str(tall) == str(tall)[0] * 4:
        continue
    slutt, runder = tallspill(tall, vis=False)
    if slutt != 6174:
        print(f'{tall} ender ikke på 6174')
    if runder not in antall_med_runder:
        antall_med_runder[runder] = 0
    antall_med_runder[runder] += 1

flest_runder = 0
for runder in antall_med_runder:
    if runder > flest_runder:
        flest_runder = runder
print(f'Flest runder: {flest_runder}, og {antall_med_runder[flest_runder]} tall trenger så mange')

runder_liste = sorted(antall_med_runder)
antall_liste = [antall_med_runder[r] for r in runder_liste]
plt.bar(runder_liste, antall_liste)
plt.title('Tallspillet: hvor mange runder trenger tallene fra 1000 til 9999?')
plt.xlabel('Antall runder til tallet ikke endrer seg')
plt.ylabel('Antall tall')
plt.show()


# OPPGAVE 2 - YOUTUBE-STATISTIKK (eksamen H2023, oppgave 11)
"""
Valg for å vaske og forberede datasettet:
- Fila er lagret med latin-1, ikke utf-8, så den leses med encoding='latin-1'.
- nan i fila blir NaN av seg selv i pandas. Kanaler uten land er ikke med i a)
  og b), fordi value_counts() hopper over NaN.
- c) Åtte kanaler har 0 videovisninger. Det er kanaler som YouTube Movies, som
  samler andres videoer. Tallet er ikke ekte, så de er ikke med i snittet av
  videovisninger. De er med i snittet av abonnenter, fordi det tallet er ekte.
"""

youtube = pd.read_csv('data/global_youtube_statistics.csv', encoding='latin-1')

# a)
kanaler_per_land = youtube['Country'].value_counts()
topp10 = kanaler_per_land.head(10)
print('De ti landene med flest kanaler:')
print(topp10)

plt.barh(topp10.index[::-1], topp10.values[::-1])
plt.title('De ti landene med flest av de største YouTube-kanalene')
plt.xlabel('Antall kanaler')
plt.ylabel('Land')
plt.tight_layout()
plt.show()

# c)
null_visninger = youtube[youtube['video views'] == 0]
print(null_visninger[['Youtuber', 'Country', 'video views']])

# b)
med_visninger = youtube[youtube['video views'] > 0]
print(f'{"Land":<16}{"Abonnenter":>14}{"Visninger":>18}')
for land in topp10.index:
    abonnenter = youtube[youtube['Country'] == land]['subscribers'].mean()
    visninger = med_visninger[med_visninger['Country'] == land]['video views'].mean()
    print(f'{land:<16}{abonnenter:>14,.0f}{visninger:>18,.0f}')

# d) Brukervalg. Her kommer kategorien fra en liste, så fila ikke venter på input.
kategorier = list(youtube['category'].value_counts().index)
for svar in ['musikk', 'Gaming']:  # svar = input('Kategori: ')
    if svar not in kategorier:
        print(f'{svar} finnes ikke. Velg en av disse:')
        print(', '.join(sorted(kategorier)))
        continue
    utvalg = youtube[youtube['category'] == svar]
    print(f'Flest kanaler i {svar}:')
    print(utvalg['Country'].value_counts().head(10))

# Med input() blir d) slik:
# while True:
#     svar = input('Kategori: ')
#     if svar in kategorier:
#         break
#     print('Velg en av disse:', ', '.join(sorted(kategorier)))


# OPPGAVE 3 - VIRUSSPREDNING (eksamen H2024, oppgave 10)

FRISK = 0
SMITTET = 1
SYK = 2
IMMUN = 3
DOD = 4
NAVN = ['frisk', 'smittet', 'syk', 'immun', 'død']


# DEL 1
class Person:
    def __init__(self):
        self.tilstand = FRISK
        self.dager = 0

    def smitt(self):
        if self.tilstand == FRISK:
            self.tilstand = SMITTET
            self.dager = 0

    def kan_smitte(self):
        return self.tilstand == SMITTET or self.tilstand == SYK

    def ny_dag(self):
        if self.tilstand == SMITTET:
            self.dager += 1
            if self.dager == 3:
                self.tilstand = SYK
                self.dager = 0
        elif self.tilstand == SYK:
            self.dager += 1
            if random.random() < 0.01:
                self.tilstand = DOD
            elif self.dager == 4:
                self.tilstand = IMMUN

    def __str__(self):
        return NAVN[self.tilstand]


# b) Testprogram
person = Person()
person.smitt()
forlop = [str(person)]
for dag in range(8):
    person.ny_dag()
    forlop.append(str(person))
print(' -> '.join(forlop))
# Tre dager smittet, så fire dager syk, som i figuren på eksamen.
assert forlop[:3] == ['smittet'] * 3
assert forlop[3] in ['syk', 'død']
assert forlop[-1] in ['immun', 'død']


# DEL 2
class Populasjon:
    def __init__(self, storrelse, andel_vaksinert=0):
        self.storrelse = storrelse
        self.personer = []
        for rad in range(storrelse):
            ny_rad = []
            for kolonne in range(storrelse):
                person = Person()
                if random.random() < andel_vaksinert:
                    person.tilstand = IMMUN
                ny_rad.append(person)
            self.personer.append(ny_rad)

    def naboer(self, rad, kolonne):
        resultat = []
        for dr, dk in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = rad + dr
            k = kolonne + dk
            if 0 <= r < self.storrelse and 0 <= k < self.storrelse:
                resultat.append(self.personer[r][k])
        return resultat

    def ny_dag(self):
        # Først finner vi alle som blir smittet, så smitter vi dem.
        # Da smitter ikke de nye videre før i morgen.
        nye_smittede = []
        for rad in range(self.storrelse):
            for kolonne in range(self.storrelse):
                if self.personer[rad][kolonne].kan_smitte():
                    for nabo in self.naboer(rad, kolonne):
                        if nabo.tilstand == FRISK and random.random() < 0.3:
                            nye_smittede.append(nabo)
        for rad in self.personer:
            for person in rad:
                person.ny_dag()
        for person in nye_smittede:
            person.smitt()

    def som_tall(self):
        return [[person.tilstand for person in rad] for rad in self.personer]

    def tell(self):
        antall = [0, 0, 0, 0, 0]
        for rad in self.personer:
            for person in rad:
                antall[person.tilstand] += 1
        return antall

    def smitte_pagar(self):
        return self.tell()[SMITTET] + self.tell()[SYK] > 0


# Testprogram for naboene
liten = Populasjon(3)
assert len(liten.naboer(1, 1)) == 4
assert len(liten.naboer(0, 0)) == 2


# DEL 3
def start_populasjon(andel_vaksinert=0):
    populasjon = Populasjon(49, andel_vaksinert)
    midt = 24
    populasjon.personer[midt][midt].tilstand = SYK
    for nabo in populasjon.naboer(midt, midt):
        nabo.tilstand = FRISK
        nabo.smitt()
    return populasjon


# e)
populasjon = start_populasjon()
farger = ListedColormap(['lightgrey', 'pink', 'red', 'dimgrey', 'black'])
historikk = []
dag = 0
while populasjon.smitte_pagar():
    historikk.append(populasjon.tell())
    if dag % 10 == 0:
        plt.clf()
        plt.imshow(populasjon.som_tall(), cmap=farger, vmin=0, vmax=4)
        plt.title(f'Virusspredning, dag {dag}')
        plt.xlabel('Kolonne')
        plt.ylabel('Rad')
        plt.pause(0.05)
    populasjon.ny_dag()
    dag += 1
historikk.append(populasjon.tell())
plt.show()

# f)
for tilstand in range(5):
    plt.plot([antall[tilstand] for antall in historikk], label=NAVN[tilstand])
plt.title('Virusspredning i en populasjon på 49 ganger 49')
plt.xlabel('Dag')
plt.ylabel('Antall personer')
plt.legend()
plt.grid()
plt.show()

# g)
for andel in [0, 0.3, 0.6]:
    dode = []
    for forsok in range(5):
        populasjon = start_populasjon(andel)
        while populasjon.smitte_pagar():
            populasjon.ny_dag()
        dode.append(populasjon.tell()[DOD])
    print(f'{andel:.0%} vaksinerte: døde i fem kjøringer: {dode}')
# Med 60 % vaksinerte stopper smitten nesten med en gang, fordi de fleste
# har for få naboer som kan smittes.
