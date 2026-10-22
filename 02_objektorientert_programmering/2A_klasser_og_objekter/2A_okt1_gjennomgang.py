# IT2 2A - klasser og objekter, økt 1


# 1. Problemet klasser løser

# Slik har dere gjort det til nå:
bil1_merke = 'Volvo'
bil1_km = 120000
bil2_merke = 'Tesla'
bil2_km = 45000

# Tre biler til, og det blir uhåndterlig.
# En klasse er en oppskrift på hvordan en ting ser ut.


# 2. Den enkleste klassen

class Bil:
    def __init__(self, merke, kilometer):
        self.merke = merke
        self.kilometer = kilometer


bil1 = Bil('Volvo', 120000)
bil2 = Bil('Tesla', 45000)

print(bil1.merke)
print(bil2.kilometer)

# class lager oppskriften. Bil('Volvo', 120000) lager ett objekt.
# __init__ kjører automatisk når objektet lages.


# 3. Hva self er

bil1.kilometer = 130000
print(bil1.kilometer, bil2.kilometer)

# Bare den ene endret seg.
# self betyr "dette objektet". Hvert objekt har sine egne verdier.
# Vi skriver self når vi lager klassen, men ikke når vi lager objektet.


# 4. Metoder

class Bil:
    def __init__(self, merke, kilometer):
        self.merke = merke
        self.kilometer = kilometer

    def kjor(self, distanse):
        self.kilometer += distanse

    def trenger_service(self):
        return self.kilometer > 150000


bil = Bil('Volvo', 149000)
bil.kjor(2000)
print(bil.kilometer)
print(bil.trenger_service())

# En metode er en funksjon som hører til klassen.
# self må stå først i parameterlista, men sendes ikke med i kallet.


# 5. __str__

class Bil:
    def __init__(self, merke, kilometer):
        self.merke = merke
        self.kilometer = kilometer

    def __str__(self):
        return f'{self.merke} med {self.kilometer} km'


bil = Bil('Volvo', 120000)
print(bil)

# Uten __str__ skriver print noe slikt som
#   <__main__.Bil object at 0x7f8b1c0d4e50>
# Prøv det ved å kommentere bort metoden.


# 6. Standardverdier

class Bil:
    def __init__(self, merke, kilometer=0):
        self.merke = merke
        self.kilometer = kilometer

    def __str__(self):
        return f'{self.merke} med {self.kilometer} km'


print(Bil('Tesla'))
print(Bil('Tesla', 45000))

# Som i vanlige funksjoner: standardverdier må stå sist.


# 7. Dokumentasjon

class Bil:
    '''Representerer en bil med merke og kilometerstand.'''

    def __init__(self, merke, kilometer=0):
        self.merke = merke
        self.kilometer = kilometer

    def kjor(self, distanse):
        '''Øker kilometerstanden med distanse.'''
        self.kilometer += distanse


print(Bil.__doc__)


# 8. Å beskytte verdiene

# Problemet: ingenting hindrer dette.
bil = Bil('Volvo', 120000)
bil.kilometer = -500
print(bil.kilometer)

# En kilometerstand kan ikke være negativ. Vi vil at endringer
# skal gå gjennom en metode som sjekker.


class Batteri:
    '''Et batteri med en kapasitet og et energinivå.'''

    def __init__(self, batteri_id, energikapasitet):
        self._batteri_id = batteri_id
        self._energikapasitet = energikapasitet
        self._energiniva = 0.0  # starter tomt

    def lad_opp(self, energi):
        self._energiniva += energi
        if self._energiniva > self._energikapasitet:
            self._energiniva = self._energikapasitet

    def bruk_energi(self, energi):
        self._energiniva -= energi

    def vis_energiniva(self):
        return self._energiniva


batteri = Batteri('BAT001', 100.0)
batteri.lad_opp(50.0)
print(batteri.vis_energiniva())
batteri.bruk_energi(20.0)
print(batteri.vis_energiniva())
batteri.lad_opp(200.0)  # stopper ved kapasiteten
print(batteri.vis_energiniva())

# Understreken foran navnet betyr "ikke rør denne utenfra".
# Python hindrer deg ikke, det er en avtale mellom programmerere.
# Den gjør at vi kan stole på at lad_opp er eneste vei inn.


# 9. Å si fra når noe er galt

class Batteri:
    '''Et batteri med en kapasitet og et energinivå.'''

    def __init__(self, batteri_id, energikapasitet):
        self._batteri_id = batteri_id
        self._energikapasitet = energikapasitet
        self._energiniva = 0.0

    def lad_opp(self, energi):
        if energi < 0:
            raise ValueError('Energimengden kan ikke være negativ.')
        self._energiniva += energi
        if self._energiniva > self._energikapasitet:
            self._energiniva = self._energikapasitet

    def bruk_energi(self, energi):
        if energi < 0:
            raise ValueError('Energimengden kan ikke være negativ.')
        if energi > self._energiniva:
            raise ValueError('Ikke nok energi i batteriet.')
        self._energiniva -= energi

    def vis_energiniva(self):
        return self._energiniva

    def __str__(self):
        return f'{self._batteri_id}: {self._energiniva} av {self._energikapasitet}'


# raise stopper programmet med en feilmelding du har skrevet selv.
# Det er samme ValueError som int('tre') gir.


# 10. Testprogram

def test_batteri():
    batteri = Batteri('BAT001', 100.0)

    batteri.lad_opp(50.0)
    print(batteri.vis_energiniva())  # 50.0

    batteri.bruk_energi(20.0)
    print(batteri.vis_energiniva())  # 30.0

    try:
        batteri.bruk_energi(50.0)
    except ValueError as feil:
        print('Feil fanget:', feil)

    try:
        batteri.lad_opp(-10.0)
    except ValueError as feil:
        print('Feil fanget:', feil)

    batteri.lad_opp(100.0)
    print(batteri.vis_energiniva())  # 100.0, stoppet ved maks

    print(batteri)


test_batteri()

# try/except er det samme som i testfila fra IT-olympiaden.
# Forskjellen er at feilen nå kommer fra vår egen raise.
