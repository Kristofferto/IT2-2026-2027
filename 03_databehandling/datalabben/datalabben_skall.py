"""
DATALABBEN
Fagdag uke 44, etter prøven. Omtrent to timer. Arbeid i par.

Datasettet er 600 bysykkelturer i Oslo, i fila
data/sykkelturer.csv. Kolonnene er:

    dato;starttid;startstasjon;sluttstasjon;varighet_min
    2026-04-11;14:26;Carl Berners plass;Majorstuen;15.4

Første time er steg 1 til 4: fra rader til objekter.
Andre time er steg 5 til 8: analysen, figurene og det dere fant.

REKKER DERE IKKE ALT: gjør oppgavene merket (viktig) først.
De andre kan dere ta hvis det er tid.

NØDUTGANG: står du fast på klassen i steg 2, les fila inn i vanlige
lister slik du gjorde i uke 43, og gjør resten av labben med dem.
Alt fra steg 5 og utover kan løses begge veier. Ikke sitt fast på
steg to i en time.
"""

import csv

import matplotlib.pyplot as plt


"""
STEG 1 - se på dataene

Åpne fila i VS Code og se på den. Svar i kommentarer:

  a) Hvor mange linjer er det, og hvor mange turer er det?
  b) Hvilken type er varigheten når du leser den fra fil?
  c) Hvilke tre av kolonnene er tekst som skal forbli tekst?
"""


"""
STEG 2 - klassen

Lag klassen Sykkeltur.

  a) Konstruktør som tar imot dato, starttid, startstasjon,
     sluttstasjon og varighet
  b) __str__ som gir én lesbar linje
  c) Metoden er_lang() som returnerer True over 30 minutter
  d) Metoden time() som returnerer timen turen startet, som tall.
     Hint: starttid er tekst på formen '14:26'.
  e) Metoden maned() som returnerer måneden som tall.
     Hint: dato er tekst på formen '2026-04-11'.
"""


class Sykkeltur:
    pass  # erstatt denne


"""
STEG 3 - les inn hele datasettet

Skriv funksjonen les_turer(filnavn) som returnerer en liste med
ett Sykkeltur-objekt per rad i fila.

  a) Åpne med encoding='utf-8-sig'
  b) Bruk csv.reader med delimiter=';'
  c) Hopp over overskriftslinja med next()
  d) Husk float() på varigheten
  e) Skriv ut hvor mange turer du fikk, og de tre første
"""


def les_turer(filnavn):
    """Returnerer en liste med Sykkeltur-objekter lest fra fila."""
    turer = []
    # din kode her
    return turer


"""
STEG 4 - sjekk at det stemmer

Se på utskriften fra steg 3e før du går videre.
Du skal få 600 turer. De tre første skal være de samme som de tre
første radene i fila, med varighetene 15.4, 7.6 og 50.6 minutter.
Stemmer det, er innlesingen riktig, og du er i gang.
"""


"""
STEG 5 - søk og filtrering

Skriv disse funksjonene. Alle skal ta imot lista med turer og
returnere noe, ikke skrive ut.

  a) lange_turer(turer)               alle over 30 minutter (viktig)
  b) turer_fra(stasjon, turer)        alle som startet på én stasjon (viktig)
  c) turer_i_maned(maned, turer)      alle i én måned
  d) lengste_tur(turer)               hele objektet, ikke bare tallet (viktig)
  e) korteste_tur(turer)              hele objektet

Finn lengste og korteste med løkke. Ikke bruk max() eller min().
"""


"""
STEG 6 - statistikk

  a) Gjennomsnittlig varighet, regnet med løkke (viktig)
  b) Hvor mange turer varte under 5 minutter?
  c) Hvor stor andel av turene er lange? Oppgi i prosent.
  d) Hvilken startstasjon er mest brukt? (viktig)
     Hint: bruk en ordbok med stasjonsnavn som nøkkel.
  e) Hvilken strekning er mest brukt?
     Hint: samme teknikk, men nøkkelen er 'A til B'.
"""


"""
STEG 7 - figurene

Minst to figurer, a og c. Alle skal ha tittel og tekst på begge akser.

  a) Histogram over varighetene. Prøv flere verdier for bins. (viktig)
  b) Søylediagram over antall turer per startstasjon.
     Sorter gjerne stasjonene etter antall.
  c) Søylediagram eller kurve over antall turer per time på dagen. (viktig)
     Se om du finner rushtidene.
  d) Valgfri fjerde figur: noe du selv ble nysgjerrig på.

Lagre den du er mest fornøyd med som en png-fil.
"""


"""
STEG 8 - én ting dere fant

Skriv tre til fem setninger nederst i fila, som kommentar:

  Hva så dere i dataene som ikke var åpenbart på forhånd?
  Hvilken figur viser det best?
  Hva ville dere trengt for å sjekke om det stemmer?

Hvert par viser denne figuren og sier disse setningene til klassen
de siste tjue minuttene. To minutter per par.
"""


"""
EKSTRA - hvis dere blir ferdige

  1. Legg til metoden er_rushtid() på Sykkeltur, som returnerer True
     hvis time() er 7, 8 eller 9, eller 15, 16 eller 17.
     Er rushtidsturene lengre eller kortere enn snittet?

  2. Lag klassen Stasjon med navn, antall avganger og antall ankomster.
     Lag ett objekt per stasjon ved å gå gjennom turene. Hvilken
     stasjon har størst ubalanse mellom de to?

  3. Les samme fil med pandas og regn ut gjennomsnittet på nytt.
     Får du samme tall? Hvor mange linjer kode sparte du?

  4. Hvilken dag i uka er travlest? Datoen er tekst, så dette krever
     litt tenking. Hint: 2026-04-11 var en lørdag.
"""
