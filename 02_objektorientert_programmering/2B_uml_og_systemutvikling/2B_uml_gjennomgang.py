# IT2 2B - UML-klassediagram
# Diagrammene står som kommentarer over klassen de beskriver.
# Tegn diagrammene selv mens du leser, så kjør koden under.


# 1. Hvorfor UML

# Et klassediagram er en tegning av klassene i et program, uten koden.
# Det brukes til to ting:
#   planlegge før du koder
#   forklare et program til noen som ikke skal lese koden
#
# Det er ikke Python. Det er ikke engang bundet til Python.
# Samme diagram kan bli Java eller C#.


# 2. De tre feltene

#   +----------------------------+
#   |            Bil             |   1. klassenavnet
#   +----------------------------+
#   | - merke: str               |   2. attributtene
#   | - kilometer: int           |
#   +----------------------------+
#   | + kjor(distanse: int)      |   3. metodene
#   | + trenger_service(): bool  |
#   +----------------------------+


class Bil:
    def __init__(self, merke, kilometer=0):
        self._merke = merke
        self._kilometer = kilometer

    def kjor(self, distanse):
        self._kilometer += distanse

    def trenger_service(self):
        return self._kilometer > 150000


# Øverst navnet, i midten det objektet VET, nederst det det KAN.
# Datatypen står etter kolon. Returtypen står etter parentesen.
# __init__ tegnes vanligvis ikke. Attributtene viser hva den tar imot.


# 3. Pluss og minus

#   -   privat, bare klassen selv rører den    self._merke
#   +   offentlig, alle kan bruke den          def kjor(...)
#
# Regelen i praksis: attributter får minus, metoder får pluss.
# Vil du at noen skal lese en verdi utenfra, lager du en metode
# med pluss som returnerer den.


# 4. Fra diagram til kode

# Dette er veien de må kunne gå. Diagrammet først:

#   +--------------------------+
#   |          Konto           |
#   +--------------------------+
#   | - eier: str              |
#   | - saldo: float           |
#   +--------------------------+
#   | + sett_inn(belop: float) |
#   | + ta_ut(belop: float)    |
#   | + vis_saldo(): float     |
#   +--------------------------+


class Konto:
    def __init__(self, eier, saldo=0.0):
        self._eier = eier
        self._saldo = saldo

    def sett_inn(self, belop):
        if belop < 0:
            raise ValueError('Beløpet kan ikke være negativt.')
        self._saldo += belop

    def ta_ut(self, belop):
        if belop > self._saldo:
            raise ValueError('Ikke dekning på kontoen.')
        self._saldo -= belop

    def vis_saldo(self):
        return self._saldo


konto = Konto('Kari Nordmann', 500)
konto.sett_inn(250)
konto.ta_ut(100)
print(konto.vis_saldo())

# Legg merke til at diagrammet ikke sier noe om ValueError.
# Et klassediagram viser strukturen, ikke oppførselen.


# 5. Arv

# Pilen peker OPP mot superklassen, og har åpen spiss.

#            +------------------+
#            |       Dyr        |
#            +------------------+
#            | - navn: str      |
#            | - alder: int     |
#            +------------------+
#            | + spis()         |
#            +------------------+
#                     ^
#                     |
#          +----------+----------+
#          |                     |
#   +--------------+      +--------------+
#   |     Hund     |      |     Katt     |
#   +--------------+      +--------------+
#   | - rase: str  |      |              |
#   +--------------+      +--------------+
#   | + bjeff()    |      | + mjau()     |
#   +--------------+      +--------------+


class Dyr:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder

    def spis(self):
        print(f'{self._navn} spiser.')


class Hund(Dyr):
    def __init__(self, navn, alder, rase):
        super().__init__(navn, alder)
        self._rase = rase

    def bjeff(self):
        print(f'{self._navn} sier voff.')


class Katt(Dyr):
    def mjau(self):
        print(f'{self._navn} sier mjau.')


Hund('Rex', 4, 'border collie').bjeff()
Katt('Pus', 7).spis()

# Hund og Katt gjentar IKKE navn og alder i diagrammet.
# De arver dem. Står de der likevel, er diagrammet feil.


# 6. Forhold mellom klasser

# Når en klasse inneholder objekter av en annen, tegnes en strek
# mellom dem, med antall i hver ende.

#   +------------------+                 +------------------+
#   |    Kortstokk     | 1          0..* |       Kort       |
#   +------------------+-----------------+------------------+
#   | - kort: list     |                 | - farge: str     |
#   +------------------+                 | - verdi: int     |
#   | + stokk()        |                 +------------------+
#   | + del_ut(): Kort |                 | + poeng(): int   |
#   +------------------+                 +------------------+
#
#   Les den slik: én kortstokk har null eller flere kort.
#
# Antallene du trenger:
#
#   1       nøyaktig én
#   0..1    ingen eller én
#   0..*    ingen eller flere
#   1..*    minst én
#
# * leses "mange".

import random


class Kort:
    def __init__(self, farge, verdi):
        self._farge = farge
        self._verdi = verdi

    def poeng(self):
        if self._verdi > 10:
            return 10
        return self._verdi

    def __str__(self):
        return f'{self._farge} {self._verdi}'


class Kortstokk:
    def __init__(self):
        self._kort = []
        for farge in ['hjerter', 'ruter', 'spar', 'kløver']:
            for verdi in range(1, 14):
                self._kort.append(Kort(farge, verdi))

    def stokk(self):
        random.shuffle(self._kort)

    def del_ut(self):
        if len(self._kort) == 0:
            raise ValueError('Kortstokken er tom.')
        return self._kort.pop()

    def antall_igjen(self):
        return len(self._kort)


stokk = Kortstokk()
stokk.stokk()
kort = stokk.del_ut()
print(kort, '-', kort.poeng(), 'poeng')
print(stokk.antall_igjen(), 'kort igjen')

# Attributten _kort er en liste MED objekter. Det er derfor det
# tegnes en strek og ikke bare skrives "list" i boksen.


# 7. Fem slags forhold

# Eksamen spør nesten hvert år hvilket forhold to klasser har.
# Det finnes fem, og hvert tegnes på sin måte.
#
#   Assosiasjon      A ---------- B    A kjenner B. Laaner og Bok.
#
#   Aggregering      A ◇--------- B    A har B, men B kan finnes uten A.
#                                      Spilleliste og Sang: sangen finnes
#                                      selv om lista slettes, og kan stå
#                                      i flere lister.
#
#   Komposisjon      A ◆--------- B    A består av B, og B finnes bare inne
#                                      i A. Kortstokk og Kort: kortene lages
#                                      i Kortstokk sin __init__.
#
#   Generalisering   A ◁--------- B    B arver fra A. Det er arv, fra
#                                      seksjon 5. Spissen er en åpen trekant.
#
#   Avhengighet      A - - - - -> B    A bruker B en kort stund, for eksempel
#                                      som parameter i én metode.
#
# Diamanten står alltid ved helheten, den som HAR de andre.
# Åpen diamant: delene kan leve videre. Fylt diamant: delene dør med helheten.
#
# Testen for komposisjon: blir B laget inne i A, og forsvinner B når A
# forsvinner? Da er det komposisjon. Kommer B utenfra? Da er det aggregering.
#
# Kortstokken over er komposisjon, fordi Kort-objektene lages i __init__.
# Ordene arv, polymorfisme og innkapsling fra uke 45 hører også hjemme
# her: generalisering i et diagram er arv i koden.


# 8. Et helt diagram

# Datalabben fra fagdagen, tegnet som UML:

#   +-----------------------+                  +-------------------------+
#   |      Sykkelsystem     | 1           0..* |        Sykkeltur        |
#   +-----------------------+------------------+-------------------------+
#   | - turer: list         |                  | - dato: str             |
#   +-----------------------+                  | - starttid: str         |
#   | + les_turer(fil: str) |                  | - startstasjon: str     |
#   | + lange_turer(): list |                  | - sluttstasjon: str     |
#   | + snitt(): float      |                  | - varighet: float       |
#   +-----------------------+                  +-------------------------+
#                                              | + er_lang(): bool       |
#                                              | + time(): int           |
#                                              | + maned(): int          |
#                                              +-------------------------+
#
# Dette er programmet de skrev på fredag. Forskjellen er at det
# nå står på én side, og at man ser strukturen før man ser koden.


# 9. Verktøy

# Tegn for hånd først. Det går fortere, og det er for hånd det
# skjer på en tavle eller i et møte.
#
# Skal det inn i en rapport:
#   draw.io        gratis, i nettleseren, har ferdige UML-former
#   PlantUML       du skriver tekst, verktøyet tegner
#
# Begge holder for det vi trenger.
