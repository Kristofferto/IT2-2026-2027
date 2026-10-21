# IT2 3B - reelle datasett, økt 2
# Pandas: et ryddig, et stygt og et stort datasett
# Datafilene ligger i mappa data/

import matplotlib.pyplot as plt
import pandas as pd


# 1. Problemet pandas løser

# Slik leste vi en CSV på mandag:
#
#   måneder = []
#   with open('data/vaer_oslo.csv', encoding='utf-8-sig') as fil:
#       innhold = csv.reader(fil, delimiter=';')
#       next(innhold)
#       for rad in innhold:
#           måneder.append(rad[0])
#
# Med pandas:
vær = pd.read_csv('data/vaer_oslo.csv', sep=';')
print(vær)

# Hele fila havner i én tabell. pandas kaller den en DataFrame.
# Det usynlige tegnet fra Excel fjerner pandas selv.


# 2. Et ryddig datasett

trening = pd.read_csv('data/treningsdata.csv')

print(trening.head())
print(trening.shape)  # rader, kolonner
print(trening.columns)
print(trening.describe())

# Fila er eksempelfila fra w3schools: komma mellom verdiene og kolonnenavn på første linje.
# Det er det pandas venter, så vi trenger ingen ekstra innstillinger.
# count er 164 for Calories, men 169 ellers. Fem økter mangler kalorier.
# Tomme felt blir NaN, «ikke et tall», helt av seg selv.


# 3. Norske kolonnenavn

trening.columns = ['Varighet', 'Puls', 'Makspuls', 'Kalorier']
print(trening.head())

# Lista må ha like mange navn som det er kolonner.
# Ellers: ValueError: Length mismatch.


# 4. Hente ut en kolonne

print(trening['Puls'])
print(trening['Puls'].mean())
print(trening['Kalorier'].max())

# Her bruker vi ferdige funksjoner med vilje. Det er hele poenget med biblioteket.
# mean() hopper over NaN.


# 5. Tegne med plt, slik som i uke 42

økt_nr = trening.index + 1

plt.plot(økt_nr, trening['Puls'], label='Puls')
plt.plot(økt_nr, trening['Makspuls'], label='Makspuls')
plt.title('Puls per treningsøkt')
plt.xlabel('Økt nummer')
plt.ylabel('Puls')
plt.legend()
plt.grid()
plt.show()

# En kolonne kan gis rett til plt.plot, akkurat som en liste.
# index er radnumrene 0, 1, 2 ... Med + 1 starter øktene på 1.
# Får plt.plot bare y, bruker den radnumrene som x av seg selv.
# Skriv x likevel, så ser du hva som skjer.

plt.scatter(trening['Varighet'], trening['Kalorier'])
plt.title('Kalorier mot varighet')
plt.xlabel('Varighet')
plt.ylabel('Kalorier')
plt.grid()
plt.show()

# pandas kan også tegne selv med trening.plot(). Vi bruker plt, som dere kjenner.


# 6. Et stygt datasett

medier = pd.read_csv(
    'data/ssbmedier.csv',
    skiprows=1,
    sep=';',
    index_col=0,
    na_values=['.', '..'],
    encoding='latin-1',
)
print(medier)

# SSB-fila fra mandag. Hver innstilling svarer til noe vi gjorde for hånd:
#   skiprows=1          hopp over tittellinja             next(innhold)
#   sep=';'             semikolon mellom verdiene         delimiter=';'
#   index_col=0         medietypen blir navn på radene    rad[0]
#   na_values           . og .. blir NaN                  if rad[i] != '..'
#   encoding='latin-1'  fila er lagret som latin-1        samme som mandag


# 7. Innstillingene må passe fila

feil = pd.read_csv('data/treningsdata.csv', sep=';', index_col=0)
print(feil)

# SSB-innstillingene på treningsfila. Ingen feilmelding, bare en tom tabell:
# fila har ikke semikolon, så hver linje blir ett felt, og index_col=0 tar det feltet.
# Kopierer du kode fra nettet, må innstillingene passe din fil.
# Åpne fila først, og velg innstillingene ut fra det du ser.


# 8. Årstall som kolonnenavn

print(medier.columns[0])

årstall = range(2013, 2026)
medier.columns = årstall
print(medier)

# Overskriftene er lange, så vi bytter dem med årstallet.
# Årene må stemme med det du lastet ned, ellers får du Length mismatch igjen.


# 9. Hente en rad med navn

print(medier.loc['TV'])
print(medier.loc['Internett'].mean())

# loc henter raden med det navnet. Ikke bruk radnummeret:
# SSB endrer tabellen, og da flytter radene seg.
# Internett var rad 10 i NDLA-artikkelen. I fila vi har nå, er den rad 7.

plt.plot(årstall, medier.loc['TV'], marker='o', label='TV')
plt.plot(årstall, medier.loc['Internett'], marker='o', label='Internett')
plt.title('TV og internett')
plt.suptitle('Kilde: Statistisk sentralbyrå', fontsize=8)
plt.xlabel('Årstall')
plt.ylabel('Minutter per dag')
plt.legend()
plt.grid()
plt.show()

# NaN blir hull i linja. TV mangler 2020 og 2022, så 2021 står alene.
# Uten marker='o' ville det punktet vært usynlig. En linje trenger to punkter.
# På mandag hoppet vi over .. , og da gikk linja rett over hullene.


# 10. Alle radene i samme figur

for medietype in medier.index:
    plt.plot(årstall, medier.loc[medietype], label=medietype)
plt.title('Tid brukt på ulike medier')
plt.xlabel('Årstall')
plt.ylabel('Minutter per dag')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.grid()
plt.tight_layout()
plt.show()

# index er radnavnene, så løkka går gjennom alle medietypene.
# bbox_to_anchor flytter forklaringen ut av figuren, og tight_layout gir den plass.
# Matplotlib har bare ti farger. Hjemme-PC får samme farge som Radio.


# 11. Et stort datasett

turer = pd.read_csv('data/sykkelturer.csv', sep=';')
print(turer.head())
print(turer.shape)

# 600 bysykkelturer. Her begynner løkker å føles tungt.


# 12. Filtrere

lange = turer[turer['varighet_min'] > 30]
print(f'{len(lange)} turer varte over 30 minutter')

fra_majorstuen = turer[turer['startstasjon'] == 'Majorstuen']
print(f'{len(fra_majorstuen)} turer startet på Majorstuen')

# Betingelsen inni klammene sjekkes for hver rad. Radene der den er sann, blir med.

lange_majorstuen = turer[(turer['startstasjon'] == 'Majorstuen') & (turer['varighet_min'] > 30)]
print(f'{len(lange_majorstuen)} lange turer startet på Majorstuen')

vestkanten = ['Majorstuen', 'Bislett', 'Frogner stadion']
fra_vest = turer[turer['startstasjon'].isin(vestkanten)]
print(f'{len(fra_vest)} turer startet på vestkanten')

# & betyr OG. Hver betingelse må stå i sin egen parentes, ellers blir det feil.
# isin() sjekker om verdien finnes i lista. Det sparer mange ==.


# 13. Telle og gruppere

per_stasjon = turer['startstasjon'].value_counts()
print(per_stasjon)

snitt_per_stasjon = turer.groupby('startstasjon')['varighet_min'].mean()
print(snitt_per_stasjon)

# value_counts() teller forekomster. Samme som ordbok-trikset, men ferdig skrevet.
# groupby() deler radene i grupper og regner ut snittet i hver.

plt.barh(per_stasjon.index, per_stasjon.values)
plt.title('Turer per startstasjon')
plt.xlabel('Antall turer')
plt.ylabel('Startstasjon')
plt.tight_layout()
plt.show()

# index er stasjonsnavnene, values er antallet.


# 14. Ny kolonne

turer['måned'] = turer['dato'].str[5:7].astype(int)
per_måned = turer['måned'].value_counts().sort_index()
print(per_måned)

plt.bar(per_måned.index, per_måned.values)
plt.title('Turer per måned')
plt.xlabel('Måned')
plt.ylabel('Antall turer')
plt.show()

# .str[5:7] klipper ut måneden fra '2026-04-17', akkurat som med vanlig tekst.
# astype(int) gjør teksten om til tall. sort_index() sorterer etter måned.


# 15. Slik ser det ut i virkeligheten

# Masteroppgaven min besto av fire program, i denne rekkefølgen:
#
#   SWARM_Data_Retrieval.py   hent data fra satellittene, lagre lokalt
#   MLT_conversion.py         regn om koordinater
#   PCP_std.py                finn det vi leter etter, regn statistikk
#   PCP_std_plots.py          lag figurene
#
# Hent -> rydd -> regn -> plott.
# Det er nøyaktig de stegene dere har gjort på to økter.
# Forskjellen er at datasettet var noen gigabyte og tok dager å kjøre.
