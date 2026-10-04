"""
IT2 1A - UTFORDRINGER

For deg som er ferdig med oppgave 1-23.

REGELEN: du har bare variabler, operatorer, tekst, input(),
f-strenger og bibliotekene math og random.

Ingen løkker, ingen if, ingen funksjoner - de kommer senere.
Halve utfordringen er å klare seg uten.
Det er lov å bruke internett, men ikke AI!
"""

"""
1. KLOKKA

Les inn et antall sekunder og skriv ut hvor lang tid det er,
på formen 21:42:05.

  a) 78125 sekunder skal gi nøyaktig 21:42:05
  b) Alle tre feltene skal alltid ha to siffer: 01:05:09, ikke 1:5:9
  c) Hva skjer med 100000 sekunder? Gjør om programmet så det viser
     klokkeslettet på et døgn, altså starter på nytt etter 24 timer.

Hint: // og % er de eneste to verktøyene du trenger.
"""


"""
2. SIFFERSUM

Les inn et femsifret tall og skriv ut summen av sifrene.
48219 gir 24.

  a) Løs det med // og %
  b) Løs det på nytt, uten // og % i det hele tatt
  c) Hvilken av de to ville du selv lest om et halvt år? Én setning.
"""


"""
3. PALINDROM

  a) Les inn et ord og skriv det baklengs
  b) Skriv ut om ordet er likt baklengs. Dette skal gjøres UTEN if.
  c) Test med regninger og agnes
  d) Regninger med stor R gir feil svar. Fiks det.
"""


"""
4. TALLSYSTEMER

  a) Skriv ut 255 i totallsystemet, åttetallsystemet og
     sekstentallsystemet
  b) int('11111111', 2) gjør motsatt vei. Bekreft at du får 255 tilbake.
  c) Hvor mange bits trengs for tallet 1000? La programmet regne det ut,
     ikke tell for hånd.
  d) Største tall i 8 bits? I 16?
"""

print(f"{255:b}")  # start her


"""
5. DET UMULIGE REGNESTYKKET

Python mener at 0,1 + 0,2 ikke er 0,3. Kjør linjene under.

  b) Finn ut hvorfor. Stikkord: flyttall, binær representasjon.
  c) math.isclose(0.1 + 0.2, 0.3) gir True. Hvorfor trengs den?
  d) Finn et annet regnestykke med samme problem. Og ett der det ikke
     skjer - hvorfor ikke akkurat der?

Dette er ikke en feil i Python. Slik regner alle datamaskiner,
og det har veltet ekte systemer.
"""

print(0.1 + 0.2 == 0.3)
print(f"{0.1 + 0.2:.20f}")


"""
6. RAMME

Les inn et ord og tegn en ramme rundt det:

    ********
    * Kari *
    ********

  a) Rammen skal tilpasse seg lengden på ordet
  b) Ordet skal stå midtstilt

Hint: bredden kan regnes ut inne i selve f-strengen.
f'{navn:^{bredde}}' er lov, og krøllparentesene inni er
ikke en skrivefeil.
"""


"""
7. HEMMELIG KODE

Hver bokstav har et nummer. ord() gir nummeret, chr() gir bokstaven.

  a) Les inn én liten bokstav og skriv ut bokstaven tre plasser lenger
     ute i alfabetet. a blir d.
  b) Hva skjer med z? Fiks det, så z blir c. Alfabetet skal gå rundt.
  c) Utvid til et ord på nøyaktig tre bokstaver. hei skal bli khl.
  d) Skriv programmet som dekoder igjen.

Dette heter et cæsarchiffer, og Julius Cæsar brukte det på ekte.
"""

print(ord("a"))  # 97
print(chr(97))  # a


"""
8. KVITTERINGEN

Les inn tre varenavn med pris og antall, og skriv ut en kvittering med
kolonner som står rett under hverandre - også når ett av navnene er
mye lengre enn de andre.

  a) Kolonnebredden skal regnes ut fra det lengste varenavnet,
     ikke settes til et fast tall
  b) Legg til 25 % mva og en totalsum nederst
  c) Alle beløp med to desimaler, høyrejustert

Hint: max(len(a), len(b), len(c))
"""


"""
9. HAR DU KOMMET GJENNOM ALT?

Fødselsnummer
    De to siste sifrene er kontrollsiffer, regnet ut fra de ni første
    med faste vektfaktorer. Slå opp reglene og skriv et program som
    sjekker om et nummer er gyldig. Bruk ditt eget.

Terningkast
    random.seed(2026) gjør at tilfeldige tall blir de samme hver gang.
    Hvorfor kan det være nyttig? Og hva sier det om hvor tilfeldige
    de egentlig er?

Din egen
    Finn på en oppgave du selv synes er vanskelig med disse verktøyene,
    og lever den til læreren med fasit.
"""
