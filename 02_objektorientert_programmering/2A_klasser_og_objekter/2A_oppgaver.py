'''
IT2 2A - OPPGAVER
Klasser og objekter

Oppgave 1-5 hører til økt 1, 6-11 til økt 2, 12-15 til økt 3.
Oppgavene merket EKSAMEN er tidligere eksamensoppgaver eller laget
på samme måte.
'''

'''
1. FØRSTE KLASSE

Lag en klasse Elev med fornavn, etternavn og trinn.

  a) Lag konstruktøren og tre objekter
  b) Skriv ut fornavnet til det andre objektet
  c) Endre trinnet på det første. Sjekk at de andre er urørt.
  d) Legg til en metode fullt_navn() som returnerer begge navnene
  e) Legg til __str__ og skriv ut et objekt direkte
'''


'''
2. KONTO

Lag en klasse Konto med eier og saldo. Saldoen starter på 0.

  a) Lag metoden sett_inn(belop)
  b) Lag metoden ta_ut(belop)
  c) Lag __str__ som viser eier og saldo med to desimaler
  d) Test med noen innskudd og uttak
  e) Hva skjer hvis du tar ut mer enn du har? Fiks det i oppgave 4.
'''


'''
3. TERNING

Lag en klasse Terning med et antall sider, som standard 6.

  a) Lag metoden kast() som returnerer et tilfeldig tall
  b) La klassen huske siste kast i en attributt
  c) Lag en metode antall_kast() som sier hvor mange ganger den er kastet
  d) Lag to terninger med ulikt antall sider og kast begge
'''


'''
4. BESKYTTE VERDIENE

Ta utgangspunkt i Konto fra oppgave 2.

  a) Sett understrek foran saldoen: self._saldo
  b) Lag en metode vis_saldo() som returnerer den
  c) La sett_inn kaste ValueError hvis beløpet er negativt
  d) La ta_ut kaste ValueError hvis det ikke er dekning
  e) Skriv et testprogram med try/except som viser at begge virker
'''


'''
5. BATTERIBANK

Lag en klasse Batteri med batteri_id, kapasitet og energinivå som
starter på null.

  a) lad_opp(energi) som aldri lar nivået overstige kapasiteten
  b) bruk_energi(energi) som kaster ValueError ved for lite energi
  c) vis_energiniva() og __str__
  d) En metode prosent() som returnerer hvor fullt batteriet er
  e) Skriv et testprogram som dekker alle grensetilfellene
'''


'''
6. KLASSEVARIABEL

Ta utgangspunkt i Elev fra oppgave 1.

  a) Legg til en klassevariabel elevnummer som starter på 1
  b) La hver nye elev få sitt eget nummer, og tell opp
  c) Lag fem elever og skriv ut alle
  d) Skriv ut Elev.elevnummer etterpå. Hva er den nå, og hvorfor?
  e) Hva er forskjellen på Elev.elevnummer og self.elevnummer?
'''


'''
7. SAMLING AV OBJEKTER

  a) Lag en liste med ti Elev-objekter ved hjelp av en løkke
  b) Skriv en funksjon finn_elev(nummer, liste) som returnerer
     objektet med det nummeret, eller None
  c) Skriv finn_ved_fornavn(fornavn, liste) som returnerer en liste
  d) Skriv ut alle elevene på et trinn
  e) Hvorfor må du bruke en løkke for å skrive dem ut pent?
'''


'''
8. STATISTIKK PÅ OBJEKTER

    class Maaling:
        def __init__(self, sted, temperatur):
            ...

  a) Lag åtte målinger i en liste
  b) Finn gjennomsnittstemperaturen med løkke
  c) Finn det kaldeste stedet. Returner hele objektet, ikke bare tallet.
  d) Tell hvor mange målinger som er under null
  e) Tegn målingene som søylediagram
'''


'''
9. FRA FIL TIL OBJEKTER

Bruk data/sykkelturer.csv.

  a) Lag en klasse Sykkeltur med de fem feltene fra fila
  b) Les inn hele fila og lag ett objekt per rad
  c) Skriv ut de tre første turene
  d) Lag metoden er_lang() som returnerer True over 30 minutter
  e) Tell hvor mange lange turer det er
  f) Finn den lengste turen og skriv den ut
'''


'''
10. EKSAMEN: PSEUDOKODE

  a) Eksamen H2024, oppgave 3. Hva vil vises som resultat av
     programmet? Svar uten å kjøre koden.

        FUNCTION beregn(n):
           SET s TO 0
           FOR hvert tall i fra og med 1 til og med n
              IF i % 2 EQUAL TO 0
                 SET s TO s + i
              ELSE
                 SET s TO s - i
              ENDIF
           ENDFOR
           RETURN s
        ENDFUNCTION

        DISPLAY beregn(7)

     Alternativene er 1, -1, -4 og 3.

  b) Implementer pseudokoden under i Python, og test den på
     målingene fra oppgave 8.

        FUNCTION finnKaldeste(maalinger)
           SET kaldeste TO første måling i maalinger
           FOR hver m i maalinger
              IF m.temperatur LESSER THAN kaldeste.temperatur
                 SET kaldeste TO m
              ENDIF
           ENDFOR
           RETURN kaldeste
        ENDFUNCTION

  c) Skriv finn_elev fra oppgave 7b som pseudokode.

  d) Skriv pseudokode for en funksjon som teller hvor mange
     målinger som er under null. Bruk INCREMENT.
'''


'''
11. EKSAMEN: BIBLIOTEK

Eksamen V2025, oppgave 6, med en ekstra del til slutt.

Du skal lage et program for et bibliotek med to klasser, Bok og Laaner.

Klassen Bok:
  - tittel: tittelen på boka
  - forfatter: forfatteren
  - utlant: Laaner-objektet som har lånt boka, eller None
  - vis_info(): viser tittel, forfatter og om boka er utlånt

Klassen Laaner:
  - laaner_id: et unikt nummer
  - laante_boker: liste med Bok-objektene låneren har
  - laan_bok(bok): låner boka og merker den som utlånt
  - lever_tilbake(bok): leverer boka og merker den som ledig

  a) Skriv i en kommentar hvilke attributter og metoder hver klasse
     har. I uke 46 tegner du dette som et klassediagram.
  b) Implementer klassene Bok og Laaner.
  c) Lag et testprogram som
       1. lager noen bøker og låner dem ut til en låner
       2. sjekker at en bok kan lånes ut og leveres tilbake
       3. sjekker at en bok som allerede er utlånt, ikke kan lånes
  d) Håndter feil og unntak: laan_bok skal kaste ValueError hvis
     boka er utlånt, og lever_tilbake hvis låneren ikke har boka.
     Fang feilene med try/except i testprogrammet.
  e) Et hakk over eksamen: lag klassen Bibliotek med en liste med
     bøker og metodene legg_til(bok), ledige_boker() og
     finn_forfatter(forfatter). La Laaner-objektene få nummer fra
     en klassevariabel.
'''


'''
12. ARV

    class Dyr:
        def __init__(self, navn, alder):
            ...
        def spis(self):
            ...

  a) Lag superklassen Dyr med navn, alder, spis og __str__
  b) Lag Hund og Katt som arver, med hver sin lyd-metode
  c) Lag en liste med begge typer og gå gjennom den med en løkke
  d) Gi Hund en egen __init__ med rase, og bruk super()
  e) Lag Fisk som overstyrer spis
'''


'''
13. FIGURER

  a) Lag Rektangel med bredde, hoyde, areal og omkrets
  b) Lag Kvadrat som arver fra Rektangel og bare tar én sidekant
  c) Sjekk at kvadratet kan regne areal uten å ha metoden selv
  d) Lag Sirkel med radius og areal. Hvorfor kan ikke den arve
     fra Rektangel?
'''


'''
14. KJØRETØY

  a) Lag Kjoretoy med merke, kilometer og metoden kjor(distanse)
  b) Lag Elbil som arver, med batterikapasitet i tillegg
  c) Lag Lastebil som arver, med maks lastevekt
  d) Gi Elbil en egen kjor som også trekker fra på batteriet
  e) Lag en liste med alle tre typer og kjør dem 100 km hver
'''


'''
15. EKSAMEN: PRINSIPPENE I OOP

Svar uten å kjøre kode. Skriv svaret og én setning om hvorfor.

  a) Eksamen H2024, oppgave 1. Hvilket av prinsippene innen
     objektorientert programmering handler om gjenbruk av kode?
     abstraksjon, polymorfisme, innkapsling eller arv

  b) Eksamen V2025, oppgave 3. En utvikler samler felles metoder i
     en superklasse, men beholder spesialiserte varianter av metodene
     i subklassene. Hvilket prinsipp gjør at metodene kan ha samme
     navn i superklassen og subklassene, og likevel kalles riktig
     på objektene?
     abstraksjon, polymorfisme, innkapsling eller arv

  c) Eksamen V2025, oppgave 4. Hvilket prinsipp innebærer å skille
     mellom grensesnittet og de interne detaljene til objekter?
     abstraksjon, polymorfisme, innkapsling eller arv
     To av svarene kan forsvares. Hvilke, og hva skiller dem?

  d) Eksamen V2024, oppgave 2. Hvis klasse B arver fra klasse A,
     hvilken betegnelse er mest korrekt for B i forhold til A?
     B er en spesialisering av A, B er en assosiert klasse til A,
     B er en generalisering av A, eller B er en avhengig klasse av A

  e og f bygger på oppgave 14. Har du ikke gjort den, hopp over dem.

  e) Pek på ett sted i Kjoretoy-oppgaven (14) der du bruker arv,
     ett der du bruker polymorfisme, og ett der du kunne brukt
     innkapsling.

  f) Skriv pseudokode for løkka i 14e, med CALL når en metode kjøres.
'''


'''
16. HAR DU KOMMET GJENNOM ALT?

Eksamen V2024, oppgave 6
    Lag klassen Kalkulator med metodene pluss, minus, gange og dele.
    Skriv et testprogram, finn mulige feil og unntak, og håndter dem.
    Hva skjer med dele(5, 0)?

Spillkort
    Lag Kort og Kortstokk. Kortstokken skal kunne stokkes og dele ut.

Din egen
    Finn på en klasse som beskriver noe du bryr deg om, og skriv et
    testprogram til den.
'''
