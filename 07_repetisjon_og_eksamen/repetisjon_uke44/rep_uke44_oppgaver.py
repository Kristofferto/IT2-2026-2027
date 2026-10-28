"""
IT2 - REPETISJONSOPPGAVER
Onsdag uke 44. Prøve i kapittel 3 og klasser på fredag.

Bolkene kommer i samme rekkefølge som prøven.
Rekker du ikke alt: gjør A, B og E1 først.
Bolk F er ekstra trening på funksjoner fra kapittel 1.
"""

"""
BOLK A - FORSTÅELSE UTEN PC

Svar i kommentarer, ikke ved å kjøre koden.

  a) Fila tall.txt har tre linjer: 4, 10 og 7. Hva skrives ut?

        total = 0
        with open('tall.txt', encoding='utf-8') as fil:
            for linje in fil:
                total += int(linje.strip())
        print(total)

  b) Hva skjer hvis int() mangler i a)? Hvorfor?

  c) Finn de to feilene. Figuren skal ha alt den trenger, og
     bildet som lagres skal ikke være tomt.

        plt.bar(['a', 'b', 'c'], [3, 5, 2])
        plt.title('Antall')
        plt.ylabel('Stykker')
        plt.show()
        plt.savefig('antall.png')

  d) Hva skrives ut?

        data = {'by': 'Oslo', 'bydeler': [{'navn': 'Frogner', 'skoler': ['A', 'B']},
                                         {'navn': 'Grorud', 'skoler': ['C']}]}
        print(data['bydeler'][0]['navn'])
        print(data['bydeler'][0]['skoler'][1])
        print(len(data['bydeler']))

  e) Fila elever.csv har overskriftene navn;alder og fire elever:
     Ida 17, Ali 16, Per 18 og Nora 17. Hva skrives ut?

        elever = pd.read_csv('elever.csv', sep=';')
        print(elever.shape)
        print(len(elever[elever['alder'] == 17]))

  f) Hvor mange ganger kjører den innerste linja?

        for i in range(4):
            for j in range(3):
                print(i, j)
"""


"""
BOLK B - FILER OG CSV

Bruk data/vaer_oslo.csv. Den er semikolondelt med
kolonnene Maned, Temperatur og Nedbor. Bruk csv.reader, ikke pandas.

  1. Skriv les_vaerdata(filnavn) som returnerer tre lister:
     måneder, temperaturer og nedbør.
     Husk encoding='utf-8-sig' og float().

  2. Regn ut gjennomsnittstemperaturen med en løkke.

  3. Finn den våteste måneden. Skriv ut navn og mm.

  4. Tell hvor mange måneder som har snittemperatur under null.

  5. Skriv en funksjon manedene_over(grense, maneder, temperaturer)
     som returnerer en liste med navnene på månedene over grensen.

  6. Lag en ny fil varme_maneder.txt med bare månedene over
     10 grader, én per linje.
"""


"""
BOLK C - PANDAS OG JSON

Bruk data/ssbmedier.csv og data/skole.json.

  1. Åpne ssbmedier.csv i VS Code. Hva skiller verdiene? Hva står
     over overskriftene? Hvordan ser et tall som mangler ut?

  2. Les fila med pd.read_csv slik at medietypen blir navn på
     radene og .. blir NaN. Skriv en kommentar til hver innstilling.

  3. Bytt kolonnenavnene til årstallene 2013 til 2025.

  4. Skriv ut gjennomsnittlig tid brukt på radio per år.

  5. Hvilke medietyper brukte vi over 50 minutter på i 2025?

  6. Les skole.json. Skriv ut navnet og antall elever for hver klasse
     med en løkke, og regn ut hvor mange elever det er til sammen.
"""


"""
BOLK D - GRAFTEGNING

  1. Tegn temperaturen fra bolk B som kurve med markører.

  2. Legg på tittel, aksetitler, rutenett og en vannrett
     linje på null grader.

  3. Tegn tid brukt på internett og radio fra bolk C som to
     kurver i samme figur, med forklaring (legend).

  4. Legg figuren fra 1-2 og figuren fra 3 i samme vindu med
     subplot, den ene over den andre.

  5. Lagre figuren som repetisjon.png. Pass på rekkefølgen.
"""


"""
BOLK E - KLASSER

  1. Lag en klasse Bok med tittel, forfatter og antall sider.

     a) Konstruktør med de tre attributtene
     b) En metode er_lang() som returnerer True over 300 sider
     c) __str__ som viser tittel og forfatter
     d) La konstruktøren kaste ValueError hvis sidetallet er 0 eller
        mindre, og vis med try/except at det virker
     e) Lag tre bøker i en liste og skriv ut de lange med en løkke

  2. Les klassen under. Svar i kommentarer:

        class Vannmaler:
            def __init__(self, sted):
                self.sted = sted
                self._maalinger = []

            def legg_til(self, verdi):
                if verdi < 0:
                    raise ValueError('Vannstand kan ikke være negativ.')
                self._maalinger.append(verdi)

            def hoyeste(self):
                beste = self._maalinger[0]
                for m in self._maalinger:
                    if m > beste:
                        beste = m
                return beste

     a) Hva skjer når du skriver Vannmaler('Mjøsa')?
     b) Hvorfor har _maalinger understrek foran navnet?
     c) Hva går galt hvis du kaller hoyeste() rett etter at
        objektet er laget?
     d) Skriv et testprogram med try/except som viser at
        ValueError faktisk kastes.

  3. Lag en klasse Elev med fornavn og karakter.
     Lag seks elever i en liste. Regn ut snittkarakteren
     med en løkke, og finn eleven med høyest karakter.
     Returner hele objektet, ikke bare tallet.
"""


"""
BOLK F - EKSTRA: FUNKSJONER

  1. Skriv storst(a, b) som returnerer det største av to tall.
     Ikke bruk max().

  2. Skriv antall_vokaler(tekst) som returnerer hvor mange
     vokaler teksten inneholder. Husk æ, ø og å.

  3. Skriv tell_ord(setning) som returnerer en ordbok med
     hvert ord som nøkkel og antall forekomster som verdi.
"""


"""
SJEKKLISTE FØR FREDAG

Klarer du disse uten å slå opp, er du klar:

  [ ] skrive en funksjon med parameter og return
  [ ] lese en semikolondelt CSV med csv.reader og gjøre tekst til tall
  [ ] regne snitt og største med løkke
  [ ] skrive til en fil
  [ ] lese en stygg fil med pd.read_csv og forklare innstillingene
  [ ] hente en rad med loc og filtrere med en betingelse i klammer
  [ ] grave seg ned i nøstede ordbøker og lister fra JSON
  [ ] tegne en figur med tittel, aksetitler og forklaring
  [ ] to figurer med subplot, og savefig før show
  [ ] skrive en klasse med konstruktør, attributter, metoder og __str__
  [ ] kaste ValueError og fange den med try/except
  [ ] forklare hva self er
"""
