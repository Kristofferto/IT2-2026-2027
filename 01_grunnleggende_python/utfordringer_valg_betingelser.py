"""
IT2 1B - UTFORDRINGER

For deg som er ferdig med oppgavene i boka.

REGELEN: du har variabler, operatorer, tekst, input(), f-strenger,
if/elif/else og bibliotekene math og random.

Ingen løkker, ingen lister, ingen funksjoner - de kommer senere.
"""

"""
1. SKUDDÅR

Et år er skuddår hvis det er delelig med 4, men ikke med 100 -
med mindre det også er delelig med 400.

  a) Skriv et program som avgjør om et årstall er skuddår
  b) Test med 2024, 1900, 2000 og 2023. Fasit: ja, nei, ja, nei.
  c) Klarer du det med én eneste betingelse, uten elif?
  d) Hvorfor er regelen så rar? Finn ut hvorfor 1900 ikke var skuddår.
"""


"""
2. ANNENGRADSLIGNING

En ligning ax² + bx + c = 0 har null, én eller to løsninger,
avhengig av diskriminanten b² - 4ac.

  a) Les inn a, b og c og skriv ut løsningene
  b) Alle tre tilfellene skal håndteres, med forklarende tekst
  c) Test med (1, -3, 2), (1, -2, 1) og (1, 0, 1)
  d) Hva skjer hvis a er 0? Er det fortsatt en annengradsligning?
     Fiks programmet.
"""


"""
3. TREKANTEN

Tre tall skal være sidene i en trekant.

  a) Er det i det hele tatt en trekant? Summen av to sider må alltid
     være større enn den tredje.
  b) Er den likesidet, likebeint eller ulikesidet?
  c) Er den rettvinklet? Bruk Pytagoras.
  d) Test med sidene 3, 4 og 5. Får du at den er rettvinklet?
     Prøv så 0.3, 0.4 og 0.5. Hvorfor går det galt, og hva heter
     funksjonen i math som løser det?
"""


"""
4. TRINNSKATT

Skatten regnes trinnvis. Bare den delen av inntekten som ligger
inne i hvert trinn skattlegges med den satsen:

     0 -  200 000        0 %
   200 - 400 000         5 %
   400 - 800 000        15 %
   over 800 000         25 %

  a) Regn ut skatten for en inntekt
  b) Test med 350 000. Riktig svar er 7 500, ikke 17 500.
  c) Skriv også ut hvor mange prosent av hele inntekten det utgjør
  d) Snu rekkefølgen på elif-grenene dine. Hva skjer, og hvorfor?
"""


"""
5. STEIN, SAKS, PAPIR

To spillere velger hver sin. Stein slår saks, saks slår papir,
papir slår stein.

  a) Løs det med if og elif. Hvor mange grener trengte du?
  b) Løs det på nytt med maks tre grener. Gi valgene tallene
     0, 1 og 2, og se hva (spiller1 - spiller2) % 3 gir deg.
  c) Hvilken av dem er lettest å utvide til fem valg?
"""


"""
6. DE MORGAN

To uttrykk er logisk like hvis de gir samme svar for alle
kombinasjoner av True og False.

  a) Sjekk om not (a and b) er det samme som (not a) or (not b).
     Du må teste alle fire kombinasjonene.
  b) Sjekk om not (a or b) er det samme som (not a) and (not b).
  c) Skriv ut resultatet som en pen sannhetstabell
  d) Hva er det motsatte av alder >= 18 and har_billett?
     Skriv det uten å bruke not.
"""


"""
7. PASSORDSJEKK

Et passord godkjennes hvis det er minst åtte tegn langt og
inneholder både store bokstaver, små bokstaver og et siffer.

  a) Sjekk lengden
  b) Sjekk resten - UTEN løkke. Det finnes strengmetoder som gjør
     jobben, men du må tenke litt vrient.
  c) Skriv ut hva som mangler, ikke bare om det er godkjent
  d) Løsningen din på sifferkravet er sannsynligvis ikke helt riktig.
     Finn et passord som slipper gjennom uten å ha et siffer.

Hint til b: hva er forskjellen på passord og passord.lower()
hvis passordet inneholder en stor bokstav?
"""


"""
8. UKEDAG

Zellers kongruens gir ukedagen for en hvilken som helst dato:

    h = (q + 13(m + 1)//5 + K + K//4 + J//4 + 5J) % 7

der q er dagen i måneden, m er måneden, K er de to siste sifrene
i årstallet og J er de to første. h = 0 er lørdag, 1 er søndag,
og så videre.

  a) Skriv programmet. Sjekk mot en dato du vet svaret på.
  b) Januar og februar teller som måned 13 og 14 i året FØR.
     Legg inn den regelen.
  c) Test med din egen fødselsdato. Hvilken ukedag ble du født?
  d) Formelen bruker heltallsdivisjon fem steder. Bytt én av dem
     med vanlig divisjon og se hva som skjer.
"""


"""
9. HAR DU KOMMET GJENNOM ALT?

Fødselsnummer
    De to siste sifrene i et fødselsnummer er kontrollsiffer.
    Slå opp reglene og skriv et program som sjekker om et nummer
    er gyldig. Bruk ditt eget.

Terningspill
    To terninger kastes. Du vinner på 7 eller 11, taper på 2, 3
    eller 12, ellers uavgjort. Skriv spillet. Hvor ofte vinner du,
    tror du? Test det når du har lært løkker.

Din egen
    Finn på en oppgave som er vanskelig med disse verktøyene,
    og lever den til læreren med fasit.
"""
