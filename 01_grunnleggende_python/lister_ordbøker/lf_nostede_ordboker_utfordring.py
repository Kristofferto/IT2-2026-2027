# Nøstede ordbøker — utfordringer, løsningsforslag med poeng
# Totalt 60 poeng


# Felles for alle oppgavene
# Små slurvefeil overses. Gjennomgående feil som viser manglende forståelse gir trekk
# (for eksempel at eleven regner snitt av snitt i 2a, eller endrer på ordboka som kom inn
# som parameter der oppgaven sier at den ikke skal endres).
# Løsninger som bruker sum(), max() eller min() godtas ikke — vi regner selv.


# Datasettet for oppgave 1 til 3

elever = {
    'Mia': {
        'matematikk': {'karakterer': [4, 5, 3], 'fravær': 2},
        'naturfag': {'karakterer': [5, 5], 'fravær': 0},
        'norsk': {'karakterer': [3, 4, 4], 'fravær': 5},
    },
    'Jonas': {
        'matematikk': {'karakterer': [6, 5, 6], 'fravær': 1},
        'norsk': {'karakterer': [3, 3], 'fravær': 4},
    },
    'Sara': {
        'naturfag': {'karakterer': [2, 3, 4], 'fravær': 7},
        'norsk': {'karakterer': [4, 5, 6], 'fravær': 1},
    },
}


# Oppgave 1a (5p)
# 2p: riktig oppslag i alle tre nivåene av ordboka
# 2p: alle tre None-tilfellene håndtert (ukjent elev, ukjent fag, tom karakterliste)
# 1p: helt korrekt, inkludert avrunding

# Skriv funksjonen snitt_i_fag som har tre parametre: elever (den nøstede ordboka),
# navn og fag. Funksjonen skal returnere snittkarakteren til eleven i det faget,
# avrundet til én desimal. Dersom eleven ikke finnes, eleven ikke har faget, eller
# faget ikke har noen karakterer, skal funksjonen returnere None.
# Kallet snitt_i_fag(elever, 'Mia', 'matematikk') skal returnere 4.0, mens kallet
# snitt_i_fag(elever, 'Jonas', 'naturfag') skal returnere None.


def snitt_i_fag(elever, navn, fag):
    if navn not in elever:
        return None
    if fag not in elever[navn]:
        return None
    karakterer = elever[navn][fag]['karakterer']
    if len(karakterer) == 0:
        return None
    total = 0
    for karakter in karakterer:
        total += karakter
    return round(total / len(karakterer), 1)


assert snitt_i_fag(elever, 'Mia', 'matematikk') == 4.0
assert snitt_i_fag(elever, 'Jonas', 'matematikk') == 5.7
assert snitt_i_fag(elever, 'Jonas', 'naturfag') is None
assert snitt_i_fag(elever, 'Ida', 'norsk') is None


# Oppgave 1b (6p)
# 2p: løkke gjennom fagene til én elev
# 2p: riktig kall på snitt_i_fag og sammenlikning som finner det høyeste
# 1p: riktig håndtering av likt snitt (alfabetisk først)
# 1p: helt korrekt

# Skriv funksjonen beste_fag som har to parametre: elever og navn. Funksjonen skal
# returnere navnet på faget der eleven har høyest snitt. Dersom to fag har nøyaktig
# samme snitt, skal det faget som kommer først alfabetisk returneres. Dersom eleven
# ikke finnes, skal funksjonen returnere None.
# Kallet beste_fag(elever, 'Mia') skal altså returnere 'naturfag'.


def beste_fag(elever, navn):
    if navn not in elever:
        return None
    beste = None
    beste_snitt = 0
    for fag in elever[navn]:
        snitt = snitt_i_fag(elever, navn, fag)
        if snitt is None:
            continue
        if beste is None or snitt > beste_snitt:
            beste = fag
            beste_snitt = snitt
        elif snitt == beste_snitt and fag < beste:
            beste = fag
    return beste


likt = {
    'Kari': {
        'norsk': {'karakterer': [4], 'fravær': 0},
        'matematikk': {'karakterer': [4], 'fravær': 0},
    },
}

assert beste_fag(elever, 'Mia') == 'naturfag'
assert beste_fag(elever, 'Jonas') == 'matematikk'
assert beste_fag(elever, 'Sara') == 'norsk'
assert beste_fag(elever, 'Ida') is None
assert beste_fag(likt, 'Kari') == 'matematikk'


# Oppgave 2a (7p)
# 2p: dobbel løkke gjennom elever og fag
# 3p: samler opp sum og antall per fag — alle karakterene i samme pott
# 1p: riktig avrunding til slutt, ikke underveis
# 2p: helt korrekt
# Merk: en løsning som regner snitt av elevenes snitt gir maks 3p. Den er feil fordi
# elever med ulikt antall karakterer da teller like mye.

# Skriv funksjonen snitt_per_fag som har én parameter elever. Funksjonen skal returnere
# en ny ordbok der nøklene er fagene som finnes i datasettet, og verdien er snittet av
# alle karakterene som er gitt i faget, uansett hvilken elev de tilhører. Snittet skal
# avrundes til én desimal.
# Kallet snitt_per_fag(elever) skal altså returnere
# {'matematikk': 4.8, 'naturfag': 3.8, 'norsk': 4.0}.


def snitt_per_fag(elever):
    total = {}
    antall = {}
    for navn in elever:
        for fag in elever[navn]:
            if fag not in total:
                total[fag] = 0
                antall[fag] = 0
            for karakter in elever[navn][fag]['karakterer']:
                total[fag] += karakter
                antall[fag] += 1
    snitt = {}
    for fag in total:
        if antall[fag] > 0:
            snitt[fag] = round(total[fag] / antall[fag], 1)
    return snitt


assert snitt_per_fag(elever) == {'matematikk': 4.8, 'naturfag': 3.8, 'norsk': 4.0}
assert snitt_per_fag({}) == {}


# Oppgave 2b (8p)
# 2p: bygger opp en ny ordbok med fag som nøkkel
# 2p: legger inn en ny indre ordbok med alle tre nøklene første gang faget dukker opp
# 2p: elevlista fylles opp i riktig rekkefølge, fraværet summeres
# 1p: riktig gjenbruk av snitt_per_fag i stedet for å regne på nytt
# 1p: helt korrekt

# Skriv funksjonen fag_oversikt som har én parameter elever. Funksjonen skal returnere
# en nøstet ordbok der hvert fag peker på en ordbok med tre nøkler:
#   'elever'  — en liste med navnene på elevene som har faget, i samme rekkefølge
#               som elevene står i datasettet
#   'snitt'   — snittet i faget, slik det er definert i oppgave 2a
#   'fravær'  — summen av fraværet til alle elevene i faget
# Bruk funksjonen fra oppgave 2a som en del av løsningen.


def fag_oversikt(elever):
    snitt = snitt_per_fag(elever)
    oversikt = {}
    for navn in elever:
        for fag in elever[navn]:
            if fag not in oversikt:
                oversikt[fag] = {'elever': [], 'snitt': snitt[fag], 'fravær': 0}
            oversikt[fag]['elever'].append(navn)
            oversikt[fag]['fravær'] += elever[navn][fag]['fravær']
    return oversikt


fasit_oversikt = {
    'matematikk': {'elever': ['Mia', 'Jonas'], 'snitt': 4.8, 'fravær': 3},
    'naturfag': {'elever': ['Mia', 'Sara'], 'snitt': 3.8, 'fravær': 7},
    'norsk': {'elever': ['Mia', 'Jonas', 'Sara'], 'snitt': 4.0, 'fravær': 10},
}

assert fag_oversikt(elever) == fasit_oversikt


# Oppgave 3a (10p + 1p refleksjon)
# 2p: går gjennom begge ordbøkene og får med elever og fag som bare finnes i den ene
# 3p: karakterlistene skjøtes sammen i riktig rekkefølge, høst før vår
# 2p: fraværet summeres
# 2p: kopierer listene i stedet for å gjenbruke dem — originalene er uendret etterpå
# 1p: helt korrekt
# 1p: refleksjonssvar som nevner at listene deles mellom gammel og ny ordbok, slik at
#     et append i resultatet også endrer originalen

# Skriv funksjonen slaa_sammen som har to parametre, hoest og vaar. Begge er nøstede
# ordbøker med samme oppbygning som datasettet over. Funksjonen skal returnere en helt
# ny ordbok der:
#   - alle elever og fag fra begge ordbøkene er med
#   - karakterlista er karakterene fra høst etterfulgt av karakterene fra vår
#   - fraværet er summen av fraværet fra høst og vår
# Verken hoest eller vaar skal være endret etter kallet.
#
# Refleksjon: forklar i en kommentar hva som går galt dersom du skriver
# resultat[navn][fag] = hoest[navn][fag] i stedet for å bygge en ny indre ordbok.


def slaa_sammen(hoest, vaar):
    resultat = {}
    for navn in hoest:
        resultat[navn] = {}
        for fag in hoest[navn]:
            kopi = []
            for karakter in hoest[navn][fag]['karakterer']:
                kopi.append(karakter)
            resultat[navn][fag] = {
                'karakterer': kopi,
                'fravær': hoest[navn][fag]['fravær'],
            }
    for navn in vaar:
        if navn not in resultat:
            resultat[navn] = {}
        for fag in vaar[navn]:
            if fag not in resultat[navn]:
                resultat[navn][fag] = {'karakterer': [], 'fravær': 0}
            for karakter in vaar[navn][fag]['karakterer']:
                resultat[navn][fag]['karakterer'].append(karakter)
            resultat[navn][fag]['fravær'] += vaar[navn][fag]['fravær']
    return resultat


# Refleksjon: da peker den nye ordboka på nøyaktig de samme indre ordbøkene og listene
# som hoest gjør. Når vi så legger til vårkarakterene, legges de også inn i hoest —
# originalen blir ødelagt uten at vi har skrevet en eneste linje som endrer den.

hoest = {
    'Mia': {'norsk': {'karakterer': [3, 4], 'fravær': 2}},
}
vaar = {
    'Mia': {
        'norsk': {'karakterer': [5], 'fravær': 1},
        'matematikk': {'karakterer': [4], 'fravær': 0},
    },
    'Jonas': {'norsk': {'karakterer': [6], 'fravær': 3}},
}
fasit_sammen = {
    'Mia': {
        'norsk': {'karakterer': [3, 4, 5], 'fravær': 3},
        'matematikk': {'karakterer': [4], 'fravær': 0},
    },
    'Jonas': {'norsk': {'karakterer': [6], 'fravær': 3}},
}

assert slaa_sammen(hoest, vaar) == fasit_sammen
assert hoest == {
    'Mia': {'norsk': {'karakterer': [3, 4], 'fravær': 2}}
}  # originalen er urørt
assert len(vaar['Mia']['norsk']['karakterer']) == 1


# Datasettet for oppgave 4
# Her vet vi ikke hvor dypt ordboka er nøstet. En verdi er enten et tall,
# eller en ny ordbok.

skole = {
    'realfag': {
        'fysikk': {'elever': 24, 'timer': 5},
        'kjemi': {'elever': 18, 'timer': 5},
    },
    'språk': {
        'tysk': {'elever': 12, 'timer': 4},
        'fransk': {
            'nivå 1': {'elever': 9, 'timer': 4},
            'nivå 2': {'elever': 6, 'timer': 4},
        },
    },
}


# Oppgave 4a (6p)
# 2p: løkke gjennom nøklene og oppslag av verdien
# 2p: skiller mellom tall og ordbok, og kaller seg selv på ordboka
# 1p: summerer returverdien fra det indre kallet i stedet for å ignorere den
# 1p: helt korrekt, inkludert at en tom ordbok gir 0

# Skriv funksjonen tell_tall som har én parameter data, en nøstet ordbok av ukjent dybde.
# Funksjonen skal returnere summen av alle tallene som ligger i ordboka, uansett hvor
# dypt de ligger. Du vet ikke hvor mange nivåer det er, så du kan ikke løse dette med
# et fast antall løkker inni hverandre.
# Kallet tell_tall(skole) skal altså returnere 91.


def tell_tall(data):
    total = 0
    for noekkel in data:
        verdi = data[noekkel]
        if isinstance(verdi, dict):
            total += tell_tall(verdi)
        else:
            total += verdi
    return total


assert tell_tall({}) == 0
assert tell_tall({'elever': 24, 'timer': 5}) == 29
assert tell_tall(skole) == 91


# Oppgave 4b (8p)
# 2p: sjekker om nøkkelen finnes på dette nivået før den går videre nedover
# 3p: kaller seg selv på hver indre ordbok og tar vare på svaret
# 2p: bygger opp stien ved å sette nøkkelen på dette nivået foran svaret nedenfra
# 1p: returnerer None når nøkkelen ikke finnes noe sted

# Skriv funksjonen finn_sti som har to parametre: data (en nøstet ordbok av ukjent dybde)
# og noekkel. Funksjonen skal returnere en liste med nøklene man må følge fra toppen og
# ned for å komme til noekkel. Dersom nøkkelen finnes flere steder, skal den første som
# blir funnet returneres. Dersom nøkkelen ikke finnes, skal funksjonen returnere None.
# Kallet finn_sti(skole, 'tysk') skal altså returnere ['språk', 'tysk'], og kallet
# finn_sti(skole, 'nivå 2') skal returnere ['språk', 'fransk', 'nivå 2'].


def finn_sti(data, noekkel):
    for denne in data:
        if denne == noekkel:
            return [denne]
        if isinstance(data[denne], dict):
            resten = finn_sti(data[denne], noekkel)
            if resten is not None:
                return [denne] + resten
    return None


assert finn_sti(skole, 'tysk') == ['språk', 'tysk']
assert finn_sti(skole, 'nivå 2') == ['språk', 'fransk', 'nivå 2']
assert finn_sti(skole, 'elever') == ['realfag', 'fysikk', 'elever']
assert finn_sti(skole, 'historie') is None


# Oppgave 4c (9p)
# 3p: kaller seg selv på den indre ordboka og tar vare på den flate ordboka som kommer ut
# 3p: setter nøkkelen på dette nivået foran hver av nøklene nedenfra, med skråstrek mellom
# 2p: tall på øverste nivå havner rett i resultatet uten skråstrek
# 1p: helt korrekt
# Merk: en løsning som kaller flat_ut(verdi) inne i løkka for hver eneste nøkkel gir
# riktig svar, men gjør den samme jobben om og om igjen. Nevn det, men ikke trekk for det.

# Skriv funksjonen flat_ut som har én parameter data, en nøstet ordbok av ukjent dybde.
# Funksjonen skal returnere en helt flat ordbok uten nøsting, der hver nøkkel er hele
# stien ned til tallet, satt sammen med skråstrek mellom hvert ledd.
# Kallet flat_ut(skole) skal altså gi en ordbok med ti nøkler, der blant annet
# 'realfag/fysikk/elever' peker på 24 og 'språk/fransk/nivå 2/timer' peker på 4.


def flat_ut(data):
    flat = {}
    for noekkel in data:
        verdi = data[noekkel]
        if isinstance(verdi, dict):
            indre = flat_ut(verdi)
            for indre_noekkel in indre:
                flat[noekkel + '/' + indre_noekkel] = indre[indre_noekkel]
        else:
            flat[noekkel] = verdi
    return flat


flat = flat_ut(skole)

assert len(flat) == 10
assert flat['realfag/fysikk/elever'] == 24
assert flat['språk/fransk/nivå 2/timer'] == 4
assert flat_ut({'timer': 3}) == {'timer': 3}
assert tell_tall(flat) == tell_tall(skole)  # ingenting har gått tapt

print('Alt riktig')
