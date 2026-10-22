"""
IT2 - REPETISJON
Programmeringsoppgaver

Oppgavene er hentet og tilpasset fra eksamen i IN1000 ved
Universitetet i Oslo, høsten 2023 og 2024.

Alt skal løses som funksjoner. Lagre dem i en fil som heter
mine_svar.py, og kjør repetisjon_tester.py for å sjekke svarene dine.
Du kan kjøre testene så ofte du vil - oppgaver du ikke har gjort ennå
blir bare meldt som IKKE LAGET.

Bruk nøyaktig de funksjonsnavnene som står i oppgavene,
ellers finner ikke testene dem.

REGELEN: regn ut selv med løkke.
Ikke bruk sum(), max(), min() eller count().
"""

"""
DEL 1 - FUNKSJONER OG BETINGELSER
"""

"""
1. BADMINTON

Per, Palle og Espen lurer på om de skal spille badminton. De spiller
bare hvis nøyaktig to av dem vil.

Skriv badminton(per_vil, palle_vil, espen_vil) som tar tre boolske
verdier og returnerer True hvis nøyaktig to av dem er True.

    badminton(True, True, False)  ->  True
    badminton(True, True, True)   ->  False
"""


"""
2. POENG

Skriv poeng(kort) som tar en streng. Vi antar at strengen er en av
'firkløver', 'hjerte', 'lyn' eller 'lyspære'.

Funksjonen skal returnere antall bokstaver i strengen - bortsett fra
'lyn', der den skal returnere 0.

    poeng('hjerte')  ->  6
    poeng('lyn')     ->  0
"""


"""
3. JAGES

Skriv jages(dyreliste) som tar en liste der hvert element er 'mus',
'katt' eller 'hund'. Samme dyr kan stå flere ganger.

En hund jager alltid katt, og en katt jager alltid mus. Ellers
ignorerer dyrene hverandre. Returner True hvis noen i lista vil jage
noen andre i lista.

    jages(['mus', 'katt'])          ->  True
    jages(['mus', 'mus', 'hund'])   ->  False
"""


"""
DEL 2 - LISTER
"""

"""
4. POENGSUM

Anta at funksjonen poeng fra oppgave 2 finnes og virker.

Skriv poengsum(kort) som tar en liste med strenger og returnerer
summen av poengene for alle strengene i lista.

    poengsum(['hjerte', 'lyspære'])  ->  13
"""


"""
5. BORDSETTING

Du skal plassere gjester langs én side av et bord, med annenhver
introvert og ekstrovert.

Skriv bordsetting(introverte, ekstroverte) som tar to like lange
lister med navn og returnerer én liste der annenhver kommer fra hver
av dem.

    bordsetting(['Per', 'Palle'], ['Kari', 'Mia'])
        ->  ['Per', 'Kari', 'Palle', 'Mia']
"""


"""
6. FELLES

Skriv felles(tall_lister) som tar en nøstet liste - en liste av
lister med heltall. Returner en liste med alle heltall som finnes to
eller flere ganger totalt. Det spiller ingen rolle om de står i samme
indre liste eller i hver sin. Rekkefølgen er likegyldig.

    felles([[1, 5, 1], [3, 4], [2, 3]])  ->  [1, 3]
"""


"""
7. ADSKILT

Skriv adskilt(tall_lister) som tar en nøstet liste av tall.
Returner True hvis det finnes to indre lister der hvert tall i den
ene er større enn alle tallene i den andre.

    adskilt([[1, 10], [6, 8], [2, 3]])     ->  True
    adskilt([[1, 10], [6, 8], [2, 3, 7]])  ->  False
"""


"""
DEL 3 - ORDBØKER
"""

"""
8. HEIE

Du heier på Brann så lenge de gjør det bra, ellers heier du på laget
som leder.

Skriv heie(tabell) som tar en ordbok der nøklene er lagnavn og
verdiene er plassering. Er Brann på plass 3 eller bedre, returner
'Brann'. Ellers returner navnet på laget som ligger på plass 1.

Du kan anta at 'Brann' finnes i ordboka, og at et lag har plass 1.

    heie({'Rosenborg': 4, 'Odd': 1, 'Molde': 3, 'Brann': 2})  ->  'Brann'
    heie({'Rosenborg': 2, 'Odd': 1, 'Molde': 3, 'Brann': 4})  ->  'Odd'
"""


"""
9. FLERTALL

Skriv flertall(dyreliste) som returnerer navnet på det dyret det
finnes flest av i lista. Er det likt mellom to, returner 'uavgjort'.

    flertall(['ulv', 'sau', 'ulv'])          ->  'ulv'
    flertall(['ulv', 'sau', 'sau', 'ulv'])   ->  'uavgjort'
"""


"""
10. UTVIDET JAGES

Som oppgave 3, men nå skal hvilke dyr som jager hvilke være
fleksibelt.

Skriv utvidet_jages(dyreliste, jaging) der jaging er en ordbok med
jegeren som nøkkel og byttet som verdi.

    utvidet_jages(['ulv', 'mus', 'sau'], {'ulv': 'sau'})   ->  True
    utvidet_jages(['ulv', 'mus', 'hund'],
                  {'ulv': 'sau', 'katt': 'mus'})           ->  False
"""


"""
11. INTERESSEGRUPPER

Skriv lag_interessegrupper(personers_interesse) som tar en ordbok med
personnavn som nøkkel og én interesse som verdi. Returner én ordbok
der hver interesse er nøkkel og verdien er en liste med alle personene
som har den interessen.

    lag_interessegrupper({'Per': 'Mat', 'Palle': 'Film', 'Espen': 'Mat'})
        ->  {'Mat': ['Per', 'Espen'], 'Film': ['Palle']}
"""


"""
DEL 4 - SAMMENSATT
"""

"""
12. FORENKLE MED EN FUNKSJON

Her er et program skrevet uten funksjoner:

    navn = input('Skriv inn navn: ')
    while len(navn) == 0:
        print('Ugyldig verdi!')
        navn = input('Skriv inn navn: ')
    print('Velkommen, ' + navn + '!')

    reisemal = input('Skriv inn hvor du skal: ')
    while len(reisemal) == 0:
        print('Ugyldig verdi!')
        reisemal = input('Skriv inn hvor du skal: ')
    print('God tur til ' + reisemal + '!')

Forenkle programmet med én funksjon som kalles to ganger. Funksjonen
skal kunne gjenbrukes i andre programmer som leser inn tekst på samme
måte. Skriv både funksjonen og programmet som bruker den.
"""


"""
13. VELG

Skriv velg(liste) som ber brukeren skrive et heltall. Du kan anta at
brukeren alltid skriver et heltall.

Er tallet en gyldig indeks i lista, returner elementet på den
indeksen. Er det ikke det, spør på nytt til du får en gyldig indeks.
"""


"""
14. STIGESPILLET

I stigespillet starter du på rute 0. For hvert terningkast flytter du
fram så mange ruter. Lander du på en rute der en stige begynner,
følger du stigen til ruten den ender på.

Skriv stigespill(terningkast, stiger) der terningkast er en liste med
heltall og stiger er en ordbok med startrute som nøkkel og sluttrute
som verdi. Returner posisjonen etter alle kastene.

    stigespill([5, 4, 2, 2], {5: 12, 18: 7})  ->  9
"""


"""
15. HVILKE TRE KAST?

Skriv hvilke_tre_kast(slutt_rute, stiger) som returnerer en nøstet
liste. Hver indre liste skal være tre terningkast som ville endt på
slutt_rute i spillet fra oppgave 14.

Du kan gjerne bruke funksjonen fra oppgave 14.

    hvilke_tre_kast(5, {3: 15, 17: 4})
        ->  [[1, 1, 3], [1, 3, 1], [2, 2, 1], [3, 2, 1]]
"""


"""
16. TELLEFUNKSJON

Her er to nesten like kodebiter:

    tegn_liste = ['F', 'E', 'R', 'S', 'K', 'E', 'N']
    tell_tegn = {}
    for tegn in tegn_liste:
        if tegn not in tell_tegn:
            tell_tegn[tegn] = 0
        tell_tegn[tegn] += 1
    for tegn in tell_tegn:
        print('Antall', tegn, ':', tell_tegn[tegn])

    setning = ['flodhest', 'er', 'best', 'ingen', 'protest']
    tell_ord = {}
    for ordet in setning:
        if ordet not in tell_ord:
            tell_ord[ordet] = 0
        tell_ord[ordet] += 1
    for ordet in tell_ord:
        print('Antall', ordet, ':', tell_ord[ordet])

Forenkle programmet så mye som mulig med én funksjon som kalles to
ganger og kan gjenbrukes på andre lister. Utskriften skal bli den
samme.
"""
