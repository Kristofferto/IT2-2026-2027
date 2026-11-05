"""
IT2 2B - UML-OPPGAVER
Mandag uke 46, første del av økta.

Oppgave 1 til 4 tegnes for hånd på papir. Ta bilde og lever.
Oppgave 5 og 6 skrives som kode i din egen fil.
Oppgave 7 er eksamensoppgaver om forhold mellom klasser.

Rekker du ikke alt: oppgave 2, 5 og 7 er de viktigste.
"""

"""
1. FRA KODE TIL DIAGRAM

Tegn klassediagrammet for denne klassen. Husk de tre feltene,
pluss og minus, datatyper og returtyper.

    class Elev:
        def __init__(self, fornavn, etternavn, trinn):
            self._fornavn = fornavn
            self._etternavn = etternavn
            self._trinn = trinn
            self._karakterer = []

        def legg_til_karakter(self, karakter):
            self._karakterer.append(karakter)

        def snitt(self):
            sum_k = 0
            for k in self._karakterer:
                sum_k += k
            return sum_k / len(self._karakterer)

        def fullt_navn(self):
            return f'{self._fornavn} {self._etternavn}'
"""


"""
2. FRA DIAGRAM TIL KODE

Skriv Python-kodene som svarer til dette diagrammet.
Lengden på en sang står i sekunder.

  +---------------------------+                  +----------------------+
  |        Spilleliste        | 1           0..* |         Sang         |
  +---------------------------+------------------+----------------------+
  | - navn: str               |                  | - tittel: str        |
  | - sanger: list            |                  | - artist: str        |
  +---------------------------+                  | - lengde: int        |
  | + legg_til(sang: Sang)    |                  +----------------------+
  | + total_lengde(): int     |                  | + minutter(): float  |
  | + finn(artist: str): list |                  +----------------------+
  +---------------------------+

  a) Skriv begge klassene
  b) Lag en spilleliste med minst fire sanger
  c) Skriv ut total lengde, både i sekunder og i minutter
  d) Finn alle sangene av én artist
  e) Legg til __str__ på begge klassene. Hvorfor står ikke __str__
     i diagrammet?
"""


"""
3. ARV

Tegn klassediagrammet for et bibliotek som har tre typer medier:
bok, lydbok og film.

  a) Finn ut hva alle tre har felles, og legg det i en superklasse
     som du kaller Medium
  b) Gi hver subklasse minst én attributt som bare den har
  c) Tegn pilene riktig vei
  d) Pass på at subklassene ikke gjentar det de arver
  e) Hvilken metode er det naturlig at alle tre har, men gjør
     forskjellig? Marker den i alle fire boksene.
"""


"""
4. FINN FEILENE

Diagrammet under har fire feil. Finn dem og skriv hva som er galt.

  +--------------------+
  |      Kjoretoy      |
  +--------------------+
  | + merke            |
  | + kilometer: int   |
  +--------------------+
  | - kjor(distanse)   |
  +--------------------+
            |
            v
  +--------------------------+
  |         Elbil            |
  +--------------------------+
  | + merke                  |
  | + kilometer: int         |
  | + batterikapasitet: int  |
  +--------------------------+
  | - kjor(distanse)         |
  | - lad(): int             |
  +--------------------------+
"""


"""
5. DIN EGEN KODE FRA FAGDAGEN

Hent fram Sykkeltur-klassen du skrev på fagdagen. Fikk du ikke laget den,
bruk Fjelltur-klassen fra oppgave 9 på prøven.

  a) Tegn klassediagrammet for den, slik den faktisk ble
  b) Tegn Stasjon-klassen i tillegg hvis du laget den
  c) Tegn streken mellom dem, med antall i hver ende. Bruker du Fjelltur,
     hopp over b og c
  d) Er det noe i diagrammet som ser rart ut nå som du ser
     strukturen samlet? Skriv én setning om det.
"""


"""
6. PLANLEGG FØR DU KODER

Nå den andre veien: tegn først, kod etterpå.

Et program skal holde orden på utlån av utstyr på skolen —
laptoper, kalkulatorer, kameraer.

  a) Tegn diagrammet FØRST, på papir. To eller tre klasser.
  b) Vis det til paret ved siden av. Kan de forklare programmet
     bare ved å se på tegningen?
  c) Skriv så koden etter diagrammet ditt
  d) Måtte du endre noe underveis? Skriv hva, og hvorfor
     diagrammet ikke fanget det.
"""


"""
7. EKSAMEN: FORHOLD MELLOM KLASSER

  a) Eksamen V2025, oppgave 2. Objekter av en klasse eksisterer og
     brukes kun innenfor objekter av en annen klasse. Hva er riktig
     type relasjon mellom de to klassene?
     assosiasjon, generalisering, komposisjon eller avhengighet

  b) Eksamen H2025, oppgave 2a og 2b. På et universitet kan studentene
     velge å knytte seg til et fakultet og da bli en del av fakultetet.
     Klassene er Student og Fakultet. Hva er riktig type relasjon?
     aggregering, generalisering, komposisjon eller avhengighet
     Begrunn svaret.

  c) Eksamen H2025, oppgave 5a. En Digitalklokke består av to
     Tallviser-objekter, ett for timer og ett for minutter, som lages
     når klokka lages. Tegn de to klassene med riktig strek og antall,
     og forklar forholdet.

  d) Eksamen V2025, oppgave 6a. Tegn klassediagrammet for Bok og Laaner
     fra 2A oppgave 11. Hvilket forhold har de, og hvilke antall står
     i hver ende av streken?

  e) Hvilket forhold er det mellom Spilleliste og Sang i oppgave 2?
     Ville svaret endret seg hvis sangene ble laget inne i Spilleliste
     sin __init__? Hva skjer, og hvorfor?
"""
