"""
IT2 3A og 3B - LØSNINGSFORSLAG

Alle figurer kommenteres bort nederst i hver oppgave hvis du vil
kjøre hele fila uten å klikke deg gjennom seksten vinduer.
"""

import csv
import json

import matplotlib.pyplot as plt
import pandas as pd

"""
3A OPPGAVE 2 - fra løkke til graf
"""

x = []
kvadrat = []
kube = []

for i in range(21):
    x.append(i)
    kvadrat.append(i**2)
    kube.append(i**3)

plt.plot(x, kvadrat, label='x^2')
plt.plot(x, kube, label='x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('To potensfunksjoner')
plt.legend()
plt.ylim(0, 400)
plt.show()

# e) x^3 forsvinner ut av bildet etter x = 7. Dataene er der,
#    men utsnittet skjuler dem.


"""
3A OPPGAVE 3 - karakterer
"""

karakterer = [4, 5, 3, 6, 4, 4, 2, 5, 6, 3, 4, 5, 4, 3, 5, 6, 2, 4]

plt.hist(karakterer, bins=[1, 2, 3, 4, 5, 6, 7])
plt.xlabel('karakter')
plt.ylabel('antall')
plt.title('Fordeling')
plt.show()

fordeling = {}
for k in karakterer:
    if k in fordeling:
        fordeling[k] += 1
    else:
        fordeling[k] = 1

verdier = sorted(fordeling)
antall = []
for k in verdier:
    antall.append(fordeling[k])

plt.bar(verdier, antall)
plt.xlabel('karakter')
plt.ylabel('antall')
plt.show()

# d) Histogram teller selv. Søylediagram tegner tall du allerede har.
#    Har du rådata, bruk histogram. Har du en oppsummering, bruk bar.


"""
3A OPPGAVE 5 - to byer
"""

maaneder = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'des']
oslo = [-3.2, -2.1, 1.8, 6.4, 12.1, 16.3, 18.0, 16.8, 12.4, 6.9, 1.5, -1.8]
bergen = [1.4, 1.9, 3.6, 6.1, 10.2, 13.0, 14.1, 14.2, 11.5, 8.4, 4.3, 2.1]

plt.plot(maaneder, oslo, linestyle='--', marker='o', label='Oslo')
plt.plot(maaneder, bergen, marker='s', label='Bergen')
plt.axhline(0)
plt.xlabel('måned')
plt.ylabel('grader celsius')
plt.title('Middeltemperatur')
plt.legend()
plt.show()

# d) største forskjell
storst = 0
maaned_storst = ''
forskjell = []

for i in range(len(maaneder)):
    diff = oslo[i] - bergen[i]
    forskjell.append(diff)
    if abs(diff) > storst:
        storst = abs(diff)
        maaned_storst = maaneder[i]

print(f'Størst forskjell i {maaned_storst}: {storst:.1f} grader')

plt.bar(maaneder, forskjell)
plt.axhline(0)
plt.xlabel('måned')
plt.ylabel('Oslo minus Bergen')
plt.show()


"""
3A OPPGAVE 6 - subplot
"""

plt.subplot(1, 2, 1)
plt.plot(maaneder, oslo)
plt.title('Oslo')
plt.ylim(-5, 20)

plt.subplot(1, 2, 2)
plt.plot(maaneder, bergen)
plt.title('Bergen')
plt.ylim(-5, 20)

plt.show()

# c) Lik y-akse er det som gjør figurene sammenlignbare.
#    Uten den ser Bergen ut til å svinge like mye som Oslo.


"""
3B OPPGAVE 1 - tekstfil
"""

måneder = []
temperaturer = []

with open('data/temperaturer.txt', encoding='utf-8') as fil:
    for linje in fil:
        deler = linje.strip().split(' ')
        måneder.append(deler[0])
        temperaturer.append(float(deler[1]))

antall_minus = 0
for t in temperaturer:
    if t < 0:
        antall_minus += 1

print(f'{antall_minus} måneder med minusgrader')

plt.plot(måneder, temperaturer)
plt.title('Temperatur i Oslo')
plt.xlabel('Måned')
plt.ylabel('Temperatur')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


"""
3B OPPGAVE 2 - skrive til fil
"""

with open('varme_maneder.txt', 'w', encoding='utf-8') as fil:
    for i in range(len(måneder)):
        if temperaturer[i] > 10:
            fil.write(f'{måneder[i]}\t{temperaturer[i]}\n')

with open('varme_maneder.txt', 'a', encoding='utf-8') as fil:
    fil.write('Ferdig\n')

# d) Med 'w' starter fila på nytt hver gang. Med 'a' vokser den.
#    Skriver du begge delene med 'a', står alt to ganger etter to kjøringer.


"""
3B OPPGAVE 3 - CSV
"""

måneder = []
temperatur = []
nedbør = []

with open('data/vaer_oslo.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    overskrifter = next(innhold)
    print(overskrifter)
    for rad in innhold:
        måneder.append(rad[0])
        temperatur.append(float(rad[1]))
        nedbør.append(int(rad[2]))

våtest = måneder[0]
tørrest = måneder[0]
mest = nedbør[0]
minst = nedbør[0]

for i in range(len(måneder)):
    if nedbør[i] > mest:
        mest = nedbør[i]
        våtest = måneder[i]
    if nedbør[i] < minst:
        minst = nedbør[i]
        tørrest = måneder[i]

print(f'Våtest: {våtest} ({mest} mm). Tørrest: {tørrest} ({minst} mm).')

plt.subplot(2, 1, 1)
plt.plot(måneder, temperatur)
plt.title('Temperatur')
plt.ylabel('Grader')
plt.xticks([])  # månedsnavnene står under figuren nedenfor

plt.subplot(2, 1, 2)
plt.bar(måneder, nedbør)
plt.title('Nedbør')
plt.xlabel('Måned')
plt.ylabel('Millimeter')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# f)
with open('data/vaer_oslo.csv', encoding='utf-8') as fil:
    innhold = csv.reader(fil, delimiter=';')
    print(next(innhold))

# Første overskrift blir '\ufeffManed'. Excel har lagt et usynlig tegn først i fila,
# og utf-8 lar det stå. Da finnes ingen kolonne som heter bare 'Maned'.


"""
3B OPPGAVE 4 - JSON
"""

with open('data/skole.json', encoding='utf-8') as fil:
    skole = json.load(fil)

print(json.dumps(skole, indent=2, ensure_ascii=False))
print(skole['skole'])
print(skole['klasser'][0]['fag'])

totalt = 0
alle_fag = []

for klasse in skole['klasser']:
    print(f'{klasse["navn"]:<8}{klasse["antall"]:>4}')
    totalt += klasse['antall']
    for fag in klasse['fag']:
        if fag not in alle_fag:
            alle_fag.append(fag)

print(f'Totalt {totalt} elever')
print(alle_fag)


"""
3B OPPGAVE 5 - SSB-fila for hånd
"""

# a)
with open('data/ssbmedier.csv', encoding='latin-1') as fil:
    for i in range(4):
        print(fil.readline().strip())

# Semikolon mellom verdiene. Én tittellinje over overskriftene.
# Tall som mangler, står som ..

# b) UnicodeDecodeError. Fila er lagret som latin-1. Der er å én byte,
#    og den byten finnes ikke i utf-8. Python stopper på første å, i «år» i tittellinja.

# c)
årstall = []
minutter = []

with open('data/ssbmedier.csv', encoding='latin-1') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)  # tittellinja
    overskrifter = next(innhold)
    for rad in innhold:
        if rad[0] == 'Radio':
            for i in range(1, len(rad)):
                if rad[i] != '..':
                    årstall.append(int(overskrifter[i][-4:]))
                    minutter.append(int(rad[i]))

print(årstall)
print(minutter)

# d)
plt.plot(årstall, minutter, marker='o')
plt.title('Tid brukt på radio')
plt.xlabel('Årstall')
plt.ylabel('Minutter per dag')
plt.grid()
plt.show()

# e)
mest = minutter[0]
år_mest = årstall[0]

for i in range(len(minutter)):
    if minutter[i] > mest:
        mest = minutter[i]
        år_mest = årstall[i]

print(f'Mest radio i {år_mest}: {mest} minutter per dag')


"""
3B OPPGAVE 6 - ryddig fil: treningsøkter
"""

# a) Komma mellom verdiene og kolonnenavn på første linje. Det er det pandas venter,
#    så ingen ekstra innstillinger trengs.

# b)
trening = pd.read_csv('data/treningsdata.csv')
trening.columns = ['Varighet', 'Puls', 'Makspuls', 'Kalorier']
print(trening)

# c)
print(trening.describe())

# count er 164 for Kalorier og 169 for de andre. Fem økter mangler kalorier.

# d)
print(f'Gjennomsnittspuls: {trening["Puls"].mean():.1f}')

# e)
økt_nr = trening.index + 1

plt.plot(økt_nr, trening['Puls'], label='Puls')
plt.plot(økt_nr, trening['Makspuls'], label='Makspuls')
plt.title('Puls per treningsøkt')
plt.xlabel('Økt nummer')
plt.ylabel('Puls')
plt.legend()
plt.grid()
plt.show()

# f)
plt.scatter(trening['Varighet'], trening['Kalorier'])
plt.title('Kalorier mot varighet')
plt.xlabel('Varighet')
plt.ylabel('Kalorier')
plt.grid()
plt.show()

# Lengre økter gir flere kalorier. Men økter med samme varighet kan variere mye,
# for eksempel fra 200 til nesten 500 kalorier for en økt på 60 minutter.

# g)
feil = pd.read_csv('data/treningsdata.csv', sep=';', index_col=0)
print(feil)

# Empty DataFrame, men ingen feilmelding. Fila har ikke semikolon, så hver linje
# blir ett eneste felt. index_col=0 gjør det feltet til radnavn, og da er det
# ingen kolonner igjen. Prøver du å gi kolonnene navn etterpå, får du Length mismatch.


"""
3B OPPGAVE 7 - stygg fil: mediebruk fra SSB
"""

# a)
medier = pd.read_csv(
    'data/ssbmedier.csv',
    skiprows=1,
    sep=';',
    index_col=0,
    na_values=['.', '..'],
    encoding='latin-1',
)

# b)
årstall = range(2013, 2026)
medier.columns = årstall
print(medier)

# c)
print(medier.describe())

# describe() regner per kolonne, altså per år. count er hvor mange medietyper
# som har tall det året. Den er bare 6 i 2022: SSB mangler sju medietyper det året.

# d)
for medietype in medier.index:
    plt.plot(årstall, medier.loc[medietype], label=medietype)
plt.title('Tid brukt på ulike medier')
plt.xlabel('Årstall')
plt.ylabel('Minutter per dag')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.grid()
plt.tight_layout()
plt.show()

# Matplotlib har ti standardfarger. Det er 13 medietyper, så de tre siste
# gjenbruker fargene til de tre første. Hjemme-PC er like grønn som Radio.

# e)
plt.plot(årstall, medier.loc['Radio'], marker='o', label='Radio')
plt.plot(årstall, medier.loc['Lydmedier'], marker='o', label='Lydmedier')
plt.title('Radio og lydmedier')
plt.suptitle('Kilde: Statistisk sentralbyrå', fontsize=8)
plt.xlabel('Årstall')
plt.ylabel('Minutter per dag')
plt.legend()
plt.grid()
plt.show()

# Linjene krysser rundt 2020. Til sammen er lyttingen nesten den samme:
# 127 minutter i 2013 og 129 i 2025. Den har bare flyttet seg fra radio til lydmedier.

# f) Tallene finnes ikke. Hjemme-PC er bare målt i 2013 og 2014. Digitale spill
#    mangler 2013 til 2015 og 2022. NaN blir hull i linja, og et år alene blir
#    bare synlig med marker='o'.

# g)
#    skiprows=(0, 1) hopper også over overskriftslinja. Da blir Papiravis-raden
#    brukt som overskrifter, og Papiravis forsvinner fra tabellen uten feilmelding.
#
#    Ti årstall fra 2010 passer ikke. Fila har 13 kolonner, så det gir Length mismatch.
#
#    iloc[[1, 10]] henter rad nummer 1 og 10. Internett er rad 7 i vår fil:
print(medier.iloc[[1, 10]].index)
#    Bruk loc med navn. Navnet står fast selv om SSB endrer rekkefølgen.

# h) Årstallene i b) må stemme med det du lastet ned. Vil du slippe det,
#    kan du hente årstallet fra overskriftene før du bytter dem:
#
#    årstall = []
#    for navn in medier.columns:
#        årstall.append(int(navn[-4:]))
#    medier.columns = årstall


"""
3B OPPGAVE 8 - sykkelturer: filtrere og gruppere
"""

turer = pd.read_csv('data/sykkelturer.csv', sep=';')

print(turer.head())
print(turer.shape)
print(turer['varighet_min'].describe())

lengst = turer['varighet_min'].max()
kortest = turer['varighet_min'].min()
print(f'Lengste tur: {lengst} minutter. Korteste: {kortest} minutter.')

korte = turer[turer['varighet_min'] < 5]
print(f'{len(korte)} turer under fem minutter')

fra_jernbanetorget = turer[turer['startstasjon'] == 'Jernbanetorget']
print(f'{len(fra_jernbanetorget)} turer startet på Jernbanetorget')

per_stasjon = turer['startstasjon'].value_counts()
print(per_stasjon)

print(turer.groupby('startstasjon')['varighet_min'].mean())

# g) Fire stasjoner rundt Grünerløkka, øst for Akerselva. Valget er elevens.
løkka = ['Grunerlokka', 'Sofienberg', 'Torshov', 'Carl Berners plass']
lokale = turer[turer['startstasjon'].isin(løkka) & turer['sluttstasjon'].isin(løkka)]
print(f'{len(lokale)} turer startet og endte på Grunerlokka-siden')


"""
3B OPPGAVE 9 - fra data til figur
"""

# a)
plt.barh(per_stasjon.index, per_stasjon.values)
plt.title('Turer per startstasjon')
plt.xlabel('Antall turer')
plt.ylabel('Startstasjon')
plt.tight_layout()
plt.show()

# b)
plt.hist(turer['varighet_min'], bins=20)
plt.title('Hvor lenge varer en tur?')
plt.xlabel('Varighet')
plt.ylabel('Antall turer')
plt.show()

# c)
turer['måned'] = turer['dato'].str[5:7].astype(int)
per_måned = turer['måned'].value_counts().sort_index()
print(per_måned)

plt.bar(per_måned.index, per_måned.values)
plt.title('Turer per måned')
plt.xlabel('Måned')
plt.ylabel('Antall turer')
plt.savefig('turer_per_maned.png')  # e) før show(), ellers lagres et tomt bilde
plt.show()

# d) April og juni har flest, 94 hver. Forskjellene er små: fra 78 til 94.
#    Datasettet er laget med lik sjanse for hver måned, så her finnes ingen sesong.
#    Et godt svar sier at forskjellene er for små til å bety noe.


"""
3B OPPGAVE 10 - samme jobb, to verktøy
"""

# a) Med csv og løkke
sum_varighet = 0
antall_turer = 0

with open('data/sykkelturer.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)
    for rad in innhold:
        sum_varighet += float(rad[4])
        antall_turer += 1

print(f'Med løkke:  {sum_varighet / antall_turer:.2f}')

# b) Med pandas
print(f'Med pandas: {turer["varighet_min"].mean():.2f}')

# c) Løkka trenger ni linjer. Pandas trenger to, read_csv medregnet.
# d) Løkka når du må gjøre noe spesielt for hver rad, eller når
#    du vil forstå hva som skjer. Pandas når datasettet er stort
#    og spørsmålet er standard.


"""
3B OPPGAVE 11 - vanligste rute
"""

turer['rute'] = turer['startstasjon'] + ' til ' + turer['sluttstasjon']
print(turer['rute'].value_counts().head(5))
