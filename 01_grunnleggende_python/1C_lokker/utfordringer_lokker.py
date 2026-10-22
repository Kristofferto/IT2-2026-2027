"""
IT2 1C - UTFORDRINGER

For deg som er ferdig med oppgavene i boka.

REGELEN: du har variabler, operatorer, tekst, input(), f-strenger,
if/elif/else, for, while og bibliotekene numpy og random.

Ingen funksjoner - de kommer senere. Lister kan du bruke, men bare
til å løkke gjennom. Resten kommer på fagdagen.
"""

"""
1. GANGETABELLEN

Skriv ut hele den lille gangetabellen som en pen tabell:

         1    2    3    4    5    6    7    8    9   10
    1    1    2    3    4    5    6    7    8    9   10
    2    2    4    6    8   10   12   14   16   18   20
    ...

  a) Få tallene til å stå rett under hverandre
  b) Legg på rad- og kolonneoverskrifter
  c) Skriv ut bare den nedre halvdelen, altså der raden er større
     enn eller lik kolonnen
  d) Hvorfor holder det med halvparten?

Hint: print(..., end='') skriver uten linjeskift.
Da må du selv si fra når raden er ferdig med en tom print().
"""


"""
2. PRIMTALL

Et primtall er bare delelig med 1 og seg selv.

  a) Les inn et tall og avgjør om det er et primtall
  b) Tell hvor mange primtall det finnes under 100. Fasit: 25.
  c) Du trenger ikke teste alle delere opp til tallet selv.
     Hvor langt holder det å gå? Begrunn svaret.
  d) Bruk break til å stoppe med én gang du finner en deler.
     Hvor mye raskere blir programmet for tallet 1000000?
"""


"""
3. FIBONACCI OG DET GYLNE SNITT

Fibonaccitallene starter på 1, 1 og deretter er hvert tall summen
av de to foregående: 1, 1, 2, 3, 5, 8, 13, 21 ...

  a) Skriv ut de 20 første. Du trenger bare to variabler.
  b) Regn ut forholdet mellom to nabotall etter hvert som du går.
     Hva nærmer det seg?
  c) Sammenlign med (1 + sqrt(5)) / 2. Gjenkjenner du tallet?
  d) Hvor mange ledd trengs før forholdet stemmer på seks desimaler?
"""


"""
4. COLLATZ

Ta et tall. Er det partall, del på 2. Er det oddetall, gang med 3
og legg til 1. Gjenta. Alle tall ender til slutt på 1 - det tror vi
i hvert fall, for ingen har klart å bevise det.

  a) Skriv ut hele rekka for et tall du velger. Prøv 27.
  b) Tell hvor mange steg det tar å komme til 1
  c) Hvilket starttall under 1000 gir den lengste rekka?
     Fasit: 871, med 178 steg.
  d) Hvorfor må dette være en while-løkke og ikke en for-løkke?
"""


"""
5. KVADRATROT UTEN np.sqrt

Newtons metode finner kvadratroten av n ved å gjette, og deretter
forbedre gjettet om og om igjen:

    x_ny = 0.5 * (x + n / x)

  a) Finn kvadratroten av 2. Start med gjettet x = 1.
  b) Skriv ut gjettet for hver runde. Hvor mange runder trengs før
     det stemmer med np.sqrt(2) på femten desimaler?
  c) Bytt for-løkka med en while som stopper når to gjett på rad
     er like. Bruk np.isclose.
  d) Prøv å starte med x = 1000. Hvor mye tregere blir det?
"""


"""
6. PI MED TILFELDIGE TALL

Tenk deg et kvadrat med side 1, og en kvartsirkel inni med radius 1.
Kaster du tilfeldige punkter i kvadratet, vil andelen som havner
innenfor sirkelen nærme seg pi/4.

  a) Kast 10 000 tilfeldige punkter og regn ut et estimat for pi.
     Et punkt er innenfor når x**2 + y**2 <= 1.
  b) Prøv 100, 10 000 og 1 000 000 kast. Hvor mange riktige
     desimaler får du?
  c) Ti ganger så mange kast gir ikke ti ganger så godt svar.
     Hvordan ser sammenhengen ut?
  d) Legg inn random.seed(2026) øverst. Hva skjer nå når du kjører
     programmet flere ganger? Hvorfor kan det være nyttig?
"""


"""
7. KVITTERING FRA TO LISTER

Dette er en forsmak på fagdagen.

    varer = ['Melk', 'Kaffefilter', 'Brød']
    priser = [21.90, 34.50, 89.00]

  a) Skriv ut en kvittering med varenavn og pris i to kolonner
  b) Regn ut totalsummen
  c) Finn den dyreste varen og skriv ut navnet på den
  d) Finn det lengste varenavnet, og bruk lengden til å bestemme
     kolonnebredden automatisk

Hint: du kommer langt med for i in range(len(varer)).
"""


"""
8. BINÆRSØK

Du tenker på et tall mellom 1 og 1000. Maskinen skal finne det ved
alltid å gjette midt i det som er igjen.

  a) La programmet lete etter et tall du har skrevet inn i koden.
     Skriv ut hvert gjett.
  b) Tell antall gjett. Prøv flere hemmelige tall - hva er det verste
     tilfellet?
  c) Sammenlign med np.log2(1000). Ser du sammenhengen?
  d) Hvor mange gjett trengs for en million? For en milliard?
"""


"""
9. HAR DU KOMMET GJENNOM ALT?

Perfekte tall
    Et tall er perfekt når summen av delerne, uten tallet selv,
    er lik tallet. 6 = 1 + 2 + 3. Finn alle perfekte tall under
    10 000. Det er ikke mange.

Terningstatistikk
    Kast to terninger en million ganger og tell hvor ofte du får
    hver sum fra 2 til 12. Stemmer det med det du ville regnet
    ut for hånd?

Din egen
    Finn på en oppgave som er vanskelig med disse verktøyene,
    og lever den til læreren med fasit.
"""
