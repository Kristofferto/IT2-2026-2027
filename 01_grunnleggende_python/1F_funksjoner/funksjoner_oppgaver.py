"""
IT2 - funksjoner
OPPGAVER

REGELEN: regn ut selv med løkke der du kan.
Ikke bruk sum(), max() eller min().
"""

"""
1. OPPVARMING

  a) Lag en funksjon som tar bredde og høyde og returnerer arealet
     av et rektangel
  b) Lag en til for omkretsen
  c) Lag en tredje som bruker begge to og skriver ut en setning med
     både areal og omkrets
  d) Bytt ut return med print i den første. Hva skjer når den tredje
     prøver å regne videre med svaret?
"""


"""
2. STANDARDVERDIER OG NAVNGITTE ARGUMENTER

  a) Lag en funksjon rente(belop, sats=0.05, aar=1) som returnerer
     beløpet etter renter
  b) Kall den med bare beløp, med beløp og sats, og med alle tre
  c) Kall den med navngitte argumenter i omvendt rekkefølge
  d) Prøv å lage funksjonen med sats=0.05 FØRST i parameterlista.
     Hva sier Python?
"""


"""
3. RETURNERE FLERE VERDIER

  a) Lag en funksjon som tar en liste med tall og returnerer både
     minste, største og snittet
  b) Test med [12.4, 8.1, 15.7, 3.2, 11.0]
  c) Hva får du hvis du skriver resultat = funksjonen(tall) i stedet
     for å dele opp i tre navn? Skriv det ut og se.
  d) Hent ut bare den andre verdien fra det du fikk i c
"""


"""
4. TIDLIG RETURN

En funksjon stopper med én gang den treffer return.

  a) Lag en funksjon som tar en liste og et tall, og returnerer True
     så snart tallet finnes i lista
  b) Lag en funksjon som returnerer indeksen til det første negative
     tallet i en liste, eller -1 hvis det ikke finnes noen
  c) Lag er_primtall(tall) som returnerer False så snart den finner
     en deler
"""


"""
5. REKKEVIDDE

  a) Lag en funksjon som setter en lokal variabel og returnerer den.
     Prøv å skrive ut variabelen utenfor funksjonen.
  b) Lag en global variabel og en funksjon som LESER den. Virker det?
  c) La funksjonen prøve å ENDRE den globale variabelen. Skriv ut
     variabelen etterpå. Hva skjedde?
  d) Lag en funksjon som tar en liste og legger til et element.
     Hva skjer med originalen? Hvorfor er det annerledes enn i c?
  e) Rett funksjonen i d så originalen ikke røres
"""


"""
6. EGET BIBLIOTEK

  a) Lag en fil minstat.py med funksjonene summer, snitt, storste
     og minste. Alle skal ta en liste og returnere et tall.
  b) Gi hver funksjon en docstring
  c) Lag en ny fil som importerer minstat og bruker alle fire
  d) Legg testkode nederst i minstat.py bak
     if __name__ == '__main__':
     Sjekk at den IKKE kjører når du importerer fila
  e) Importer bare én av funksjonene med from minstat import snitt
"""


"""
7. FUNKSJONER SOM BYGGER PÅ HVERANDRE

  a) Lag er_vokal(bokstav) som returnerer True eller False
  b) Lag tell_vokaler(ord) som BRUKER er_vokal
  c) Lag vokalandel(setning) som returnerer hvor stor andel av
     tegnene som er vokaler
  d) Test med 'informasjonsteknologi'
"""


"""
8. ORDBOK INN OG UT

    lager = {'melk': 12, 'brød': 0, 'kaffe': 8}

  a) Lag en funksjon som returnerer totalt antall varer
  b) Lag en som returnerer navnet på varen det er flest av
  c) Lag en som returnerer en liste med alt som er utsolgt
  d) Lag selg(lager, vare) som trekker fra én og returnerer True
     hvis det gikk, False hvis varen var tom eller ikke finnes
  e) Kall selg to ganger på samme vare og skriv ut lageret.
     Hvorfor ble ordboka endret utenfor funksjonen?
"""


"""
9. TALLSPILL

  a) Lag en funksjon som trekker et tilfeldig tall mellom 1 og 100
  b) Lag les_gyldig_tall(tekst, lav, hoy) som spør til brukeren
     skriver et helt tall innenfor området
  c) Lag sjekk(gjett, fasit) som returnerer 'for lavt', 'for høyt'
     eller 'riktig'
  d) Sett det sammen til et spill og tell antall gjett
  e) Hvilken av funksjonene kan du gjenbruke i et helt annet program?
"""
