# IT2 2A - arv, økt 3


# 1. Problemet arv løser


class Hund:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def spis(self):
        print(f'{self.navn} spiser.')

    def bjeff(self):
        print(f'{self.navn} sier voff.')


class Katt:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def spis(self):
        print(f'{self.navn} spiser.')

    def mjau(self):
        print(f'{self.navn} sier mjau.')


# __init__ og spis er helt like. Det er dobbeltarbeid.


# 2. Superklasse og subklasse


class Dyr:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def spis(self):
        print(f'{self.navn} spiser.')

    def __str__(self):
        return f'{self.navn}, {self.alder} år'


class Hund(Dyr):
    def bjeff(self):
        print(f'{self.navn} sier voff.')


class Katt(Dyr):
    def mjau(self):
        print(f'{self.navn} sier mjau.')


hund = Hund('Rex', 4)
katt = Katt('Pus', 7)

print(hund)
hund.spis()
hund.bjeff()
katt.mjau()

# Hund(Dyr) betyr "Hund arver fra Dyr".
# Hund har ingen __init__ selv, men får den fra Dyr.


# 3. Utvide konstruktøren


class Hund(Dyr):
    def __init__(self, navn, alder, rase):
        super().__init__(navn, alder)  # kjør Dyr sin __init__ først
        self.rase = rase

    def __str__(self):
        return f'{self.navn}, {self.alder} år, {self.rase}'


hund = Hund('Rex', 4, 'border collie')
print(hund)
hund.spis()

# super() er superklassen. Vi lar den gjøre jobben den kan,
# og legger bare til det nye.


# 4. Overstyre en metode


class Fisk(Dyr):
    def spis(self):
        print(f'{self.navn} spiser under vann.')


fisk = Fisk('Nemo', 1)
fisk.spis()

# Fisk har sin egen spis. Den overstyrer den fra Dyr.
# Python bruker alltid den som ligger nærmest.


# 5. En blandet liste

dyr = [Hund('Rex', 4, 'border collie'), Katt('Pus', 7), Fisk('Nemo', 1)]

for d in dyr:
    print(d)
    d.spis()

# Alle er Dyr, så alle kan spise. Men hver gjør det på sin måte.
# Dette er hovedgrunnen til at arv er nyttig.


# 6. Et eksempel fra kapitlet

import numpy as np


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


kvadrat = Kvadrat(5)
print(kvadrat.areal(), kvadrat.omkrets())
print(f'{Sirkel(3).areal():.2f}')

# Kvadrat skriver ingen areal-metode. Den arver den.


# 7. Fire ord som kommer på eksamen

# Arv
#   Hund arver __init__ og spis fra Dyr. Kode som er skrevet én gang,
#   brukes av flere klasser. Det er gjenbruk av kode.
#
# Polymorfisme
#   Seksjon 5: samme kall, d.spis(), gjør forskjellige ting avhengig
#   av hvilket objekt det er. Ordet betyr «mange former».
#
# Innkapsling
#   Understreken fra uke 44: self._saldo endres bare gjennom metodene,
#   som sjekker verdien. Dataene er pakket inn i objektet, og resten
#   av programmet bruker bare metodene.
#
# Abstraksjon
#   Vi kaller kvadrat.areal() uten å tenke på hvordan arealet regnes ut.
#   Vi ser hva objektet kan, ikke hvordan det gjør det.
#
# Innkapsling og abstraksjon ligner. Innkapsling handler om å beskytte
# dataene. Abstraksjon handler om å skjule detaljene i hvordan noe gjøres.


# 8. Polymorfisme i pseudokode

# Eksamen kan beskrive løkka fra seksjon 5 slik:
#
#   SET dyr TO liste med en hund, en katt og en fisk
#   FOR hvert d i dyr
#       DISPLAY d
#       CALL d.spis()
#   ENDFOR
#
# CALL betyr at en funksjon eller metode kjøres.
# Hvilken spis som kjøres, avgjøres av hvilket objekt d er.
