# Nøstede ordbøker — utfordringer
# Totalt 60 poeng
#
# Fyll ut funksjonene. Under hver oppgave står det asserts som må gå gjennom.
# Kommenter ut testene for oppgavene du ikke har gjort ennå, ellers stopper fila der.
# Du skal ikke bruke sum(), max() eller min() — regn selv.


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
# Skriv funksjonen snitt_i_fag som har tre parametre: elever (den nøstede ordboka),
# navn og fag. Funksjonen skal returnere snittkarakteren til eleven i det faget,
# avrundet til én desimal. Dersom eleven ikke finnes, eleven ikke har faget, eller
# faget ikke har noen karakterer, skal funksjonen returnere None.
# Kallet snitt_i_fag(elever, 'Mia', 'matematikk') skal returnere 4.0, mens kallet
# snitt_i_fag(elever, 'Jonas', 'naturfag') skal returnere None.


def snitt_i_fag(elever, navn, fag): ...


assert snitt_i_fag(elever, 'Mia', 'matematikk') == 4.0
assert snitt_i_fag(elever, 'Jonas', 'matematikk') == 5.7
assert snitt_i_fag(elever, 'Jonas', 'naturfag') is None
assert snitt_i_fag(elever, 'Ida', 'norsk') is None


# Oppgave 1b (6p)
# Skriv funksjonen beste_fag som har to parametre: elever og navn. Funksjonen skal
# returnere navnet på faget der eleven har høyest snitt. Dersom to fag har nøyaktig
# samme snitt, skal det faget som kommer først alfabetisk returneres. Dersom eleven
# ikke finnes, skal funksjonen returnere None.
# Kallet beste_fag(elever, 'Mia') skal altså returnere 'naturfag'.
# Bruk funksjonen fra oppgave 1a som en del av løsningen.


def beste_fag(elever, navn): ...


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
# Skriv funksjonen snitt_per_fag som har én parameter elever. Funksjonen skal returnere
# en ny ordbok der nøklene er fagene som finnes i datasettet, og verdien er snittet av
# alle karakterene som er gitt i faget, uansett hvilken elev de tilhører. Snittet skal
# avrundes til én desimal.
# Kallet snitt_per_fag(elever) skal altså returnere
# {'matematikk': 4.8, 'naturfag': 3.8, 'norsk': 4.0}.
# Pass på: dette er ikke det samme som snittet av elevenes snitt. Tenk gjennom hvorfor.


def snitt_per_fag(elever): ...


assert snitt_per_fag(elever) == {'matematikk': 4.8, 'naturfag': 3.8, 'norsk': 4.0}
assert snitt_per_fag({}) == {}


# Oppgave 2b (8p)
# Skriv funksjonen fag_oversikt som har én parameter elever. Funksjonen skal returnere
# en nøstet ordbok der hvert fag peker på en ordbok med tre nøkler:
#   'elever'  — en liste med navnene på elevene som har faget, i samme rekkefølge
#               som elevene står i datasettet
#   'snitt'   — snittet i faget, slik det er definert i oppgave 2a
#   'fravær'  — summen av fraværet til alle elevene i faget
# Bruk funksjonen fra oppgave 2a som en del av løsningen.


def fag_oversikt(elever): ...


fasit_oversikt = {
    'matematikk': {'elever': ['Mia', 'Jonas'], 'snitt': 4.8, 'fravær': 3},
    'naturfag': {'elever': ['Mia', 'Sara'], 'snitt': 3.8, 'fravær': 7},
    'norsk': {'elever': ['Mia', 'Jonas', 'Sara'], 'snitt': 4.0, 'fravær': 10},
}

assert fag_oversikt(elever) == fasit_oversikt


# Oppgave 3a (10p + 1p refleksjon)
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


def slaa_sammen(hoest, vaar): ...


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
# Skriv funksjonen tell_tall som har én parameter data, en nøstet ordbok av ukjent dybde.
# Funksjonen skal returnere summen av alle tallene som ligger i ordboka, uansett hvor
# dypt de ligger. Du vet ikke hvor mange nivåer det er, så du kan ikke løse dette med
# et fast antall løkker inni hverandre.
# Kallet tell_tall(skole) skal altså returnere 91.
# Hint: isinstance(verdi, dict) er True dersom verdi er en ordbok.


def tell_tall(data): ...


assert tell_tall({}) == 0
assert tell_tall({'elever': 24, 'timer': 5}) == 29
assert tell_tall(skole) == 91


# Oppgave 4b (8p)
# Skriv funksjonen finn_sti som har to parametre: data (en nøstet ordbok av ukjent dybde)
# og noekkel. Funksjonen skal returnere en liste med nøklene man må følge fra toppen og
# ned for å komme til noekkel. Dersom nøkkelen finnes flere steder, skal den første som
# blir funnet returneres. Dersom nøkkelen ikke finnes, skal funksjonen returnere None.
# Kallet finn_sti(skole, 'tysk') skal altså returnere ['språk', 'tysk'], og kallet
# finn_sti(skole, 'nivå 2') skal returnere ['språk', 'fransk', 'nivå 2'].


def finn_sti(data, noekkel): ...


assert finn_sti(skole, 'tysk') == ['språk', 'tysk']
assert finn_sti(skole, 'nivå 2') == ['språk', 'fransk', 'nivå 2']
assert finn_sti(skole, 'elever') == ['realfag', 'fysikk', 'elever']
assert finn_sti(skole, 'historie') is None


# Oppgave 4c (9p)
# Skriv funksjonen flat_ut som har én parameter data, en nøstet ordbok av ukjent dybde.
# Funksjonen skal returnere en helt flat ordbok uten nøsting, der hver nøkkel er hele
# stien ned til tallet, satt sammen med skråstrek mellom hvert ledd.
# Kallet flat_ut(skole) skal altså gi en ordbok med ti nøkler, der blant annet
# 'realfag/fysikk/elever' peker på 24 og 'språk/fransk/nivå 2/timer' peker på 4.


def flat_ut(data): ...


flat = flat_ut(skole)

assert len(flat) == 10
assert flat['realfag/fysikk/elever'] == 24
assert flat['språk/fransk/nivå 2/timer'] == 4
assert flat_ut({'timer': 3}) == {'timer': 3}
assert tell_tall(flat) == tell_tall(skole)  # ingenting har gått tapt

print('Alt riktig')
