"""
IT2 3B - OPPGAVER
Reelle datasett

Datafilene ligger i mappa data/.
Hver figur skal ha tittel og aksetitler. Uten det er den ikke ferdig.

Oppgave 1-5 hører til mandag, oppgave 6-11 til onsdag.
"""

"""
1. LESE EN TEKSTFIL

Fila data/temperaturer.txt har én måned og én temperatur per linje.

  a) Skriv ut hele fila
  b) Skriv ut linjene uten blanke linjer mellom
  c) Del opp hver linje og lag to lister: måneder og temperaturer
  d) Skriv ut hvor mange måneder som har minusgrader
  e) Tegn temperaturen som linjegraf
"""


"""
2. SKRIVE TIL FIL

  a) Lag en fil varme_maneder.txt med alle måneder over 10 grader
  b) Skriv måned og temperatur med tabulator mellom
  c) Legg til en oppsummeringslinje nederst med 'a' i stedet for 'w'
  d) Kjør programmet to ganger. Hva skjer med fila? Hvorfor?
"""


"""
3. CSV

Fila data/vaer_oslo.csv har semikolon som skilletegn.

  a) Les fila med csv.reader og skriv ut overskriftsraden for seg
  b) Les temperatur og nedbør inn i hver sin liste
  c) Finn våteste og tørreste måned med løkke
  d) Tegn nedbøren som søylediagram
  e) Tegn temperatur og nedbør i hver sin subplot
  f) Les fila med encoding='utf-8' i stedet for 'utf-8-sig'.
     Hva skjer med den første overskriften?
"""


"""
4. JSON

Fila data/skole.json er nøstet.

  a) Les inn fila og skriv den ut formatert med json.dumps
  b) Skriv ut navnet på skolen
  c) Skriv ut alle klassene med antall elever
  d) Skriv ut alle fagene til den første klassen
  e) Regn ut totalt antall elever
  f) Lag en liste med alle fag som finnes, uten gjentakelser
"""


"""
5. SSB-FILA FOR HÅND

Fila data/ssbmedier.csv er fra Statistisk sentralbyrå. Den viser hvor mange
minutter vi bruker på ulike medier en gjennomsnittsdag.

  a) Skriv ut de fire første linjene med encoding='latin-1'. Svar på:
     Hva skiller verdiene? Hva står over overskriftene?
     Hvordan ser et tall som mangler ut?
  b) Prøv å lese fila med encoding='utf-8'. Hva skjer? Hvorfor?
  c) Les Radio-raden inn i to lister, årstall og minutter.
     Hopp over årene der tallet mangler.
  d) Tegn radiotallene som linjegraf med prikker, marker='o'
  e) Finn med løkke året da folk hørte mest på radio
"""


"""
6. RYDDIG FIL: TRENINGSØKTER

Fila data/treningsdata.csv er eksempelfila fra w3schools. Den har varighet,
puls, makspuls og kalorier for 169 treningsøkter.

  a) Åpne fila i VS Code og se på den. Trenger pd.read_csv noen
     ekstra innstillinger for å lese den?
  b) Les den inn og gi kolonnene norske navn
  c) Hvor mange økter mangler kalorier? Bruk describe()
  d) Hva er gjennomsnittspulsen?
  e) Tegn puls og makspuls for hver økt, med øktnummer fra 1 på x-aksen
  f) Tegn kalorier mot varighet som punktdiagram. Er det en sammenheng?
  g) Les fila med sep=';' og index_col=0. Hva skjer, og hvorfor?
"""


"""
7. STYGG FIL: MEDIEBRUK FRA SSB

Samme fil som i oppgave 5, nå med pandas. Oppgaven bygger på NDLA-artikkelen
«Behandling av store datamengder i Python». Koden der er laget for en eldre
versjon av fila, så den virker ikke uendret.

  a) Les fila med pd.read_csv. Velg innstillingene ut fra det du fant i 5a
  b) Bytt kolonnenavnene med årstallene 2013 til 2025
  c) Hva viser describe() for denne fila? Hva betyr count her?
  d) Tegn alle medietypene i samme figur, med forklaringen utenfor.
     Hvorfor har noen linjer samme farge?
  e) Velg to medietyper og tegn dem med prikker.
     Skriv kilden øverst med plt.suptitle()
  f) Hvorfor har Hjemme-PC og digitale spill så få punkter?
  g) NDLA bruker skiprows=(0, 1), ti årstall fra 2010 og iloc[[1, 10]].
     Prøv dem på vår fil. Hva går galt med hver av dem?
  h) Last ned tabell 04495 fra ssb.no selv, men med andre år.
     Hva må du endre i koden?
"""


"""
8. SYKKELTURER: FILTRERE OG GRUPPERE

Fila data/sykkelturer.csv har 600 bysykkelturer.

  a) Les den inn med sep=';'. Hvor mange rader og kolonner er det?
  b) Hva sier describe() om varigheten? Hva er lengste og korteste tur?
  c) Hvor mange turer varte under fem minutter?
  d) Hvor mange turer startet på Jernbanetorget?
  e) Hvilken stasjon har flest avganger? Bruk value_counts()
  f) Hva er gjennomsnittlig varighet per startstasjon? Bruk groupby()
  g) Finn turene som både startet OG endte på Grunerlokka-siden
     av byen. Velg selv hvilke stasjoner det er.
"""


"""
9. FRA DATA TIL FIGUR

  a) Tegn antall turer per startstasjon som liggende søylediagram
  b) Tegn et histogram over varigheten
  c) Lag en ny kolonne 'måned' fra datoen, og tegn antall turer per måned
  d) Hvilken måned har flest turer? Er forskjellene store?
  e) Lagre den beste figuren din som png
"""


"""
10. SAMME JOBB, TO VERKTØY

  a) Finn gjennomsnittlig varighet med csv.reader og en løkke
  b) Finn det samme med pandas
  c) Sammenlign antall linjer kode
  d) Når ville du valgt hver av dem?
"""


"""
11. HAR DU KOMMET GJENNOM ALT?

Egen fil
    Last ned et ekte datasett fra ssb.no eller data.norge.no og
    les det inn. Åpne fila først, og velg innstillingene ut fra det du ser.
    Tegn én figur som sier noe du ikke visste.

Ruteanalyse
    Finn den vanligste ruta i sykkeldatasettet, altså kombinasjonen
    av start og slutt som går igjen flest ganger.

Din egen
    Finn på en oppgave og lever den til meg med fasit.
"""
