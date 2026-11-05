"""
IT2 2A - LØSNINGSFORSLAG
"""

import csv
import random

import matplotlib.pyplot as plt
import numpy as np

"""
1. FØRSTE KLASSE
"""


class Elev:
    def __init__(self, fornavn, etternavn, trinn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.trinn = trinn

    def fullt_navn(self):
        return f'{self.fornavn} {self.etternavn}'

    def __str__(self):
        return f'{self.fullt_navn()}, {self.trinn}. trinn'


a = Elev('Kari', 'Nordmann', 3)
b = Elev('Ola', 'Hansen', 2)
a.trinn = 1
print(a, '|', b)


"""
2 og 4. KONTO MED BESKYTTELSE
"""


class Konto:
    def __init__(self, eier):
        self.eier = eier
        self._saldo = 0.0

    def sett_inn(self, belop):
        if belop < 0:
            raise ValueError('Beløpet kan ikke være negativt.')
        self._saldo += belop

    def ta_ut(self, belop):
        if belop < 0:
            raise ValueError('Beløpet kan ikke være negativt.')
        if belop > self._saldo:
            raise ValueError('Ikke dekning på kontoen.')
        self._saldo -= belop

    def vis_saldo(self):
        return self._saldo

    def __str__(self):
        return f'{self.eier}: {self._saldo:.2f} kr'


konto = Konto('Kari')
konto.sett_inn(500)
konto.ta_ut(120)
print(konto)

try:
    konto.ta_ut(10000)
except ValueError as feil:
    print('Feil fanget:', feil)

try:
    konto.sett_inn(-50)
except ValueError as feil:
    print('Feil fanget:', feil)


"""
3. TERNING
"""


class Terning:
    def __init__(self, sider=6):
        self.sider = sider
        self.siste = 0
        self._antall = 0

    def kast(self):
        self.siste = random.randint(1, self.sider)
        self._antall += 1
        return self.siste

    def antall_kast(self):
        return self._antall


random.seed(2026)
d6 = Terning()
d20 = Terning(20)

for i in range(3):
    d6.kast()
    d20.kast()

print(d6.siste, d20.siste, d6.antall_kast())


"""
5. BATTERI
"""


class Batteri:
    def __init__(self, batteri_id, kapasitet):
        self._batteri_id = batteri_id
        self._kapasitet = kapasitet
        self._energiniva = 0.0

    def lad_opp(self, energi):
        if energi < 0:
            raise ValueError('Energimengden kan ikke være negativ.')
        self._energiniva += energi
        if self._energiniva > self._kapasitet:
            self._energiniva = self._kapasitet

    def bruk_energi(self, energi):
        if energi < 0:
            raise ValueError('Energimengden kan ikke være negativ.')
        if energi > self._energiniva:
            raise ValueError('Ikke nok energi i batteriet.')
        self._energiniva -= energi

    def vis_energiniva(self):
        return self._energiniva

    def prosent(self):
        return self._energiniva / self._kapasitet * 100

    def __str__(self):
        return f'{self._batteri_id}: {self._energiniva:.1f} av {self._kapasitet:.1f} ({self.prosent():.0f} %)'


batteri = Batteri('BAT001', 100.0)
batteri.lad_opp(50.0)
batteri.bruk_energi(20.0)
batteri.lad_opp(200.0)
print(batteri)


"""
6 og 7. KLASSEVARIABEL OG SAMLING
"""


class Elev:
    elevnummer = 1

    def __init__(self, fornavn, etternavn, trinn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.trinn = trinn
        self.elevnummer = Elev.elevnummer
        Elev.elevnummer += 1

    def __str__(self):
        return f'{self.elevnummer:>3}  {self.fornavn} {self.etternavn}, {self.trinn}. trinn'


klassen = []

for i in range(10):
    klassen.append(Elev(f'Elev{i}', 'Hansen', 1 + i % 3))

for elev in klassen:
    print(elev)

print(Elev.elevnummer)

# d) Den står på 11. Ti elever er laget, og neste ville fått nummer 11.
# e) Elev.elevnummer er felles og teller oppover.
#    self.elevnummer tilhører ett objekt og står fast.


def finn_elev(nummer, liste):
    """Returnerer eleven med dette nummeret, eller None."""
    for elev in liste:
        if elev.elevnummer == nummer:
            return elev
    return None


def finn_ved_fornavn(fornavn, liste):
    """Returnerer en liste med alle som har dette fornavnet."""
    funn = []
    for elev in liste:
        if elev.fornavn == fornavn:
            funn.append(elev)
    return funn


print(finn_elev(5, klassen))
print(finn_elev(999, klassen))

for funn in finn_ved_fornavn('Elev3', klassen):
    print(funn)

# e) print() på en liste bruker ikke __str__ på elementene.
#    Du får objektadresser. Derfor må du løkke.


"""
8. STATISTIKK PÅ OBJEKTER
"""


class Maaling:
    def __init__(self, sted, temperatur):
        self.sted = sted
        self.temperatur = temperatur

    def __str__(self):
        return f'{self.sted}: {self.temperatur} grader'


maalinger = [
    Maaling('Oslo', -3.2),
    Maaling('Bergen', 1.4),
    Maaling('Tromso', -8.7),
    Maaling('Kristiansand', 2.1),
    Maaling('Trondheim', -1.5),
    Maaling('Stavanger', 3.0),
    Maaling('Bodo', -4.4),
    Maaling('Lillehammer', -6.1),
]

sum_temp = 0
kaldest = maalinger[0]
under_null = 0

for m in maalinger:
    sum_temp += m.temperatur
    if m.temperatur < kaldest.temperatur:
        kaldest = m
    if m.temperatur < 0:
        under_null += 1

print(f'Snitt: {sum_temp / len(maalinger):.2f}')
print(f'Kaldest: {kaldest}')
print(f'{under_null} steder under null')

steder = []
temperaturer = []

for m in maalinger:
    steder.append(m.sted)
    temperaturer.append(m.temperatur)

plt.bar(steder, temperaturer)
plt.axhline(0)
plt.ylabel('grader celsius')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


"""
9. FRA FIL TIL OBJEKTER
"""


class Sykkeltur:
    def __init__(self, dato, starttid, start, slutt, varighet):
        self.dato = dato
        self.starttid = starttid
        self.start = start
        self.slutt = slutt
        self.varighet = varighet

    def er_lang(self):
        return self.varighet > 30

    def __str__(self):
        return f'{self.dato} {self.starttid}  {self.start} til {self.slutt}  {self.varighet} min'


turer = []

with open('data/sykkelturer.csv', encoding='utf-8-sig') as fil:
    innhold = csv.reader(fil, delimiter=';')
    next(innhold)
    for rad in innhold:
        turer.append(Sykkeltur(rad[0], rad[1], rad[2], rad[3], float(rad[4])))

for tur in turer[0:3]:
    print(tur)

antall_lange = 0
lengste = turer[0]

for tur in turer:
    if tur.er_lang():
        antall_lange += 1
    if tur.varighet > lengste.varighet:
        lengste = tur

print(f'{antall_lange} lange turer')
print(f'Lengste: {lengste}')


"""
10. EKSAMEN: PSEUDOKODE
"""

# a) -4. Løkka regner -1 + 2 - 3 + 4 - 5 + 6 - 7.
#    Partall legges til, oddetall trekkes fra.


# b)
def finn_kaldeste(maalinger):
    """Returnerer målingen med lavest temperatur."""
    kaldeste = maalinger[0]
    for m in maalinger:
        if m.temperatur < kaldeste.temperatur:
            kaldeste = m
    return kaldeste


print(finn_kaldeste(maalinger))

# c)
#   FUNCTION finnElev(nummer, liste)
#       FOR hver elev i liste
#           IF elev.elevnummer EQUAL TO nummer
#               RETURN elev
#           ENDIF
#       ENDFOR
#       RETURN ingenting
#   ENDFUNCTION

# d)
#   FUNCTION tellFrost(maalinger)
#       SET antall TO 0
#       FOR hver m i maalinger
#           IF m.temperatur LESSER THAN 0
#               INCREMENT antall
#           ENDIF
#       ENDFOR
#       RETURN antall
#   ENDFUNCTION


"""
11. EKSAMEN: BIBLIOTEK
"""

# a)
#   Bok:    tittel, forfatter, utlant          vis_info()
#   Laaner: laaner_id, laante_boker            laan_bok(bok), lever_tilbake(bok)
#   En låner kan ha mange bøker. En bok er lånt av ingen eller én låner.


class Bok:
    """En bok som kan lånes ut."""

    def __init__(self, tittel, forfatter):
        self.tittel = tittel
        self.forfatter = forfatter
        self.utlant = None  # Laaner-objektet, eller None hvis boka er ledig

    def vis_info(self):
        # is None sjekker om attributten er None, altså at ingen har lånt boka
        if self.utlant is None:
            status = 'ledig'
        else:
            status = f'utlånt til låner {self.utlant.laaner_id}'
        print(f'{self.tittel} av {self.forfatter}, {status}')


class Laaner:
    """En låner som kan låne og levere bøker."""

    neste_id = 1  # e) klassevariabel som gir hver låner sitt nummer

    def __init__(self):
        self.laaner_id = Laaner.neste_id
        Laaner.neste_id += 1
        self.laante_boker = []

    def laan_bok(self, bok):
        if bok.utlant is not None:
            raise ValueError(f'{bok.tittel} er allerede utlånt.')
        bok.utlant = self
        self.laante_boker.append(bok)

    def lever_tilbake(self, bok):
        if bok not in self.laante_boker:
            raise ValueError(f'Låner {self.laaner_id} har ikke {bok.tittel}.')
        bok.utlant = None
        self.laante_boker.remove(bok)


# c) og d) testprogram
def test_bibliotek():
    sult = Bok('Sult', 'Knut Hamsun')
    naiv = Bok('Naiv. Super', 'Erlend Loe')
    kari = Laaner()
    ola = Laaner()

    kari.laan_bok(sult)
    kari.laan_bok(naiv)
    sult.vis_info()
    print(f'Kari har {len(kari.laante_boker)} bøker')  # 2

    kari.lever_tilbake(sult)
    sult.vis_info()  # ledig igjen

    try:
        ola.laan_bok(naiv)  # Kari har den
    except ValueError as feil:
        print('Feil fanget:', feil)

    try:
        ola.lever_tilbake(sult)  # Ola har aldri lånt den
    except ValueError as feil:
        print('Feil fanget:', feil)


test_bibliotek()


# e)
class Bibliotek:
    """Et bibliotek med en samling bøker."""

    def __init__(self):
        self.boker = []

    def legg_til(self, bok):
        self.boker.append(bok)

    def ledige_boker(self):
        ledige = []
        for bok in self.boker:
            if bok.utlant is None:
                ledige.append(bok)
        return ledige

    def finn_forfatter(self, forfatter):
        funn = []
        for bok in self.boker:
            if bok.forfatter == forfatter:
                funn.append(bok)
        return funn


biblioteket = Bibliotek()
biblioteket.legg_til(Bok('Sult', 'Knut Hamsun'))
biblioteket.legg_til(Bok('Markens grøde', 'Knut Hamsun'))
biblioteket.legg_til(Bok('Doppler', 'Erlend Loe'))

Laaner().laan_bok(biblioteket.boker[2])

for bok in biblioteket.ledige_boker():
    bok.vis_info()
print(len(biblioteket.finn_forfatter('Knut Hamsun')), 'bøker av Hamsun')


"""
12. ARV
"""


class Dyr:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def spis(self):
        print(f'{self.navn} spiser.')

    def __str__(self):
        return f'{self.navn}, {self.alder} år'


class Hund(Dyr):
    def __init__(self, navn, alder, rase):
        super().__init__(navn, alder)
        self.rase = rase

    def bjeff(self):
        print(f'{self.navn} sier voff.')

    def __str__(self):
        return f'{self.navn}, {self.alder} år, {self.rase}'


class Katt(Dyr):
    def mjau(self):
        print(f'{self.navn} sier mjau.')


class Fisk(Dyr):
    def spis(self):
        print(f'{self.navn} spiser under vann.')


dyr = [Hund('Rex', 4, 'border collie'), Katt('Pus', 7), Fisk('Nemo', 1)]

for d in dyr:
    print(d)
    d.spis()


"""
13. FIGURER
"""


class Rektangel:
    def __init__(self, bredde, hoyde):
        self.bredde = bredde
        self.hoyde = hoyde

    def areal(self):
        return self.bredde * self.hoyde

    def omkrets(self):
        return 2 * self.bredde + 2 * self.hoyde


class Kvadrat(Rektangel):
    """Et kvadrat er et rektangel med like sider."""

    def __init__(self, sidekant):
        super().__init__(sidekant, sidekant)


class Sirkel:
    def __init__(self, radius):
        self.radius = radius

    def areal(self):
        return np.pi * self.radius**2


print(Kvadrat(5).areal(), Kvadrat(5).omkrets())
print(f'{Sirkel(3).areal():.2f}')

# d) En sirkel har ikke bredde og høyde. Arv skal bare brukes når
#    subklassen virkelig ER en spesialvariant av superklassen.


"""
14. KJØRETØY
"""


class Kjoretoy:
    def __init__(self, merke, kilometer=0):
        self.merke = merke
        self.kilometer = kilometer

    def kjor(self, distanse):
        self.kilometer += distanse

    def __str__(self):
        return f'{self.merke}: {self.kilometer} km'


class Elbil(Kjoretoy):
    def __init__(self, merke, batterikapasitet, kilometer=0):
        super().__init__(merke, kilometer)
        self.batterikapasitet = batterikapasitet
        self.batteri = batterikapasitet

    def kjor(self, distanse):
        super().kjor(distanse)
        self.batteri -= distanse * 0.2
        if self.batteri < 0:
            self.batteri = 0

    def __str__(self):
        return f'{self.merke}: {self.kilometer} km, {self.batteri:.1f} kWh igjen'


class Lastebil(Kjoretoy):
    def __init__(self, merke, maks_last, kilometer=0):
        super().__init__(merke, kilometer)
        self.maks_last = maks_last

    def __str__(self):
        return f'{self.merke}: {self.kilometer} km, laster {self.maks_last} tonn'


bilene = [Kjoretoy('Volvo', 120000), Elbil('Tesla', 75), Lastebil('Scania', 18)]

for bil in bilene:
    bil.kjor(100)
    print(bil)


"""
15. EKSAMEN: PRINSIPPENE I OOP
"""

# a) Arv. Subklassene bruker koden i superklassen uten å skrive den på nytt.
# b) Polymorfisme. Samme metodenavn, men hvert objekt gjør det på sin måte.
# c) Innkapsling er det vanligste svaret: dataene skjules inne i objektet,
#    og resten av programmet bruker bare metodene.
#    Abstraksjon kan også forsvares: man viser hva objektet kan, og skjuler
#    hvordan. Udirs løsningsforslag til V2025
#    sier abstraksjon. Godt svar her: nevn begge og hva som skiller dem.
# d) B er en spesialisering av A. A er en generalisering av B.
# e) Arv: Elbil(Kjoretoy) arver merke, kilometer og __str__-ideen.
#    Polymorfisme: bil.kjor(100) i løkka kjører Elbil sin egen kjor.
#    Innkapsling: batteri burde hete _batteri og bare endres i kjor og lad.

# f)
#   SET bilene TO liste med en Kjoretoy, en Elbil og en Lastebil
#   FOR hver bil i bilene
#       CALL bil.kjor(100)
#       DISPLAY bil
#   ENDFOR


"""
16. HAR DU KOMMET GJENNOM ALT?
"""

# Eksamen V2024, oppgave 6
#
# a)  +--------------------------------------+
#     |              Kalkulator              |
#     +--------------------------------------+
#     +--------------------------------------+
#     | + pluss(a: float, b: float): float   |
#     | + minus(a: float, b: float): float   |
#     | + gange(a: float, b: float): float   |
#     | + dele(a: float, b: float): float    |
#     +--------------------------------------+
#
# Klassen har ingen attributter. Det er lov, og diagrammet viser det
# med et tomt felt i midten.


# b) og d)
class Kalkulator:
    """De fire regneartene, med sjekk av det som sendes inn."""

    def _sjekk(self, a, b):
        for tall in [a, b]:
            if type(tall) not in [int, float]:
                raise TypeError(f'{tall!r} er ikke et tall.')

    def pluss(self, a, b):
        self._sjekk(a, b)
        return a + b

    def minus(self, a, b):
        self._sjekk(a, b)
        return a - b

    def gange(self, a, b):
        self._sjekk(a, b)
        return a * b

    def dele(self, a, b):
        self._sjekk(a, b)
        if b == 0:
            raise ZeroDivisionError('Kan ikke dele på null.')
        return a / b


# c) Testprogram. Mulige feil: deling på null, og noe som ikke er et tall,
#    for eksempel tekst fra input().
kalkulator = Kalkulator()
assert kalkulator.pluss(2, 3) == 5
assert kalkulator.minus(2, 3) == -1
assert kalkulator.gange(2.5, 4) == 10
assert kalkulator.dele(7, 2) == 3.5

for a, b in [(5, 0), ('5', 2)]:
    try:
        kalkulator.dele(a, b)
    except (ZeroDivisionError, TypeError) as feil:  # to unntak i parentes fanger begge
        print(f'dele({a!r}, {b!r}): {feil}')

# dele(5, 0) uten sjekken gir ZeroDivisionError fra Python selv.
# Med sjekken får brukeren en melding vi har skrevet. Begge er unntak
# som kan fanges, men vår egen melding sier hva som var galt.
# _sjekk har understrek fordi den bare skal brukes inne i klassen.


# Spillkort
class Kort:
    def __init__(self, farge, verdi):
        self.farge = farge
        self.verdi = verdi

    def __str__(self):
        return f'{self.farge} {self.verdi}'


class Kortstokk:
    def __init__(self):
        self._kort = []
        for farge in ['spar', 'hjerter', 'ruter', 'kløver']:
            for verdi in range(1, 14):
                self._kort.append(Kort(farge, verdi))

    def stokk(self):
        random.shuffle(self._kort)

    def del_ut(self, antall):
        if antall > len(self._kort):
            raise ValueError(f'Bare {len(self._kort)} kort igjen.')
        hand = []
        for i in range(antall):
            hand.append(self._kort.pop())
        return hand


stokk = Kortstokk()
stokk.stokk()
hand = stokk.del_ut(5)
for kort in hand:
    print(kort)
assert len(stokk._kort) == 47

# Kortstokk og Kort er komposisjon: kortene lages i konstruktøren og
# finnes bare i stokken. random.shuffle stokker lista der den står.
