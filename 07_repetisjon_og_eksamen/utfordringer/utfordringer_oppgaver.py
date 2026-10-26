"""
IT2 - UTFORDRINGER
Vanskelige eksamensoppgaver, til deg som vil prøve deg på mer.

Dette er frivillig, og du jobber i ditt eget tempo. Oppgavene er hentet fra
tidligere eksamener og er blant de vanskeligste der. Hver oppgave har til
slutt en deloppgave som ligger et hakk over eksamen.

Oppgave 1 trenger kapittel 1, oppgave 2 kapittel 3, og oppgave 3 klasser.
Du kan ta dem i den rekkefølgen du vil.

Skriv koden i din egen fil, ikke i denne. Kopier data/ til mappa di.
Vis det til meg når du er ferdig med en oppgave, så ser vi på det sammen.
"""

"""
OPPGAVE 1 - TALLSPILL
Eksamen H2025, oppgave 4. Omtrent 45 minutter.

Pseudokoden under behandler et positivt firesifret heltall der det første
sifferet ikke er 0:

    FUNCTION tallspill(tall)
        REPEAT
            SET stigendeTall TO sortAscending(sifrene i tall)
            SET synkendeTall TO sortDescending(sifrene i tall)
            SET nyttTall TO synkendeTall - stigendeTall
            DISPLAY tall, "->", synkendeTall, "-", stigendeTall, "=", nyttTall
            SET tall TO nyttTall
        UNTIL tall er det samme som i forrige runde
        RETURN tall
    ENDFUNCTION

sortAscending gir sifrene i stigende rekkefølge, slik at 3142 blir 1234.
sortDescending gir dem i synkende rekkefølge, slik at 3142 blir 4321.

a) Forklar med egne ord hva algoritmen gjør, og hvordan den fortsetter til
   et tall gjentas. Ikke forklar hver linje, men algoritmen som helhet.

b) Implementer algoritmen. Programmet skal ta inn et heltall fra brukeren,
   for eksempel 3142, og vise hvert steg slik pseudokoden beskriver, helt
   til tallet ikke endrer seg lenger.

   3142 -> 4321 - 1234 = 3087
   3087 -> 8730 - 378 = 8352
   ...

c) Hva skjer med 2111? Og med 1000? Når nyttTall har færre enn fire
   sifre, skal du fylle på med nuller foran, slik at 999 blir 0999.
   Sørg for at programmet ditt gjør det.

d) Hva skjer med 5555, og hvorfor? La programmet si fra i stedet for å
   regne videre.

e) Et hakk over eksamen. Gå gjennom alle firesifrede tall fra 1000 til 9999,
   unntatt dem med fire like sifre. Hvilket tall ender alle på? Hva er det
   største antallet runder et tall trenger, og hvor mange tall trenger så
   mange? Lag en figur som viser hvor mange tall som trenger 1, 2, 3 ...
   runder.
"""

"""
OPPGAVE 2 - YOUTUBE-STATISTIKK
Eksamen H2023, oppgave 11. Omtrent én time.

data/global_youtube_statistics.csv har de nesten 1000 største
YouTube-kanalene i verden. Åpne fila og se på den før du leser den inn.
Fila er ikke lagret med utf-8, og tall som mangler, står som nan.

Programmet skal ha en kommentar med tre anførselstegn øverst som beskriver
valgene du har gjort for å vaske og forberede datasettet. Du velger selv
om du vil vise svarene som tabell, figur eller begge deler, så lenge det
viser det oppgaven spør etter.

a) Finn og vis de ti landene som har flest YouTube-kanaler i datasettet.

b) Regn ut og vis gjennomsnittlig antall abonnenter og videovisninger per
   kanal for hvert av de ti landene.

c) Noen kanaler har 0 videovisninger. Finn dem. Bør de være med i
   gjennomsnittet i b)? Begrunn valget ditt i kommentaren øverst.

d) Et hakk over eksamen. Brukeren skriver inn en kategori, for eksempel
   Music eller Gaming. Vis de ti landene med flest kanaler i den kategorien.
   Skriver brukeren en kategori som ikke finnes, skal programmet vise hvilke
   kategorier som finnes og spørre på nytt, uten å krasje.
"""

"""
OPPGAVE 3 - VIRUSSPREDNING
Eksamen H2024, oppgave 10. Omtrent to timer.

Du skal lage en objektorientert simulering av smitte, sykdom og død eller
friskhet med immunitet. En person kan være:

    frisk uten immunitet     lys grå
    smittet uten symptomer   rosa
    syk                      rød
    frisk med immunitet      mørk grå
    død                      svart

DEL 1 - KLASSEN PERSON
a) Lag klassen Person. En ny person er frisk uten immunitet og kan bli
   smittet. Etter tre dager som smittet blir personen syk. Etter fire dager
   som syk blir personen frisk med immunitet. Hver dag personen er syk, er
   sannsynligheten 1 % for at personen dør.
b) Lag et testprogram som følger én person gjennom sykdomsforløpet og viser
   tilstanden hver dag.

DEL 2 - KLASSEN POPULASJON
c) Lag klassen Populasjon, som holder orden på personene i et rutenett.
   Naboene til en person er de fire som står inntil, vannrett og loddrett,
   men ikke på skrå.
d) En person som er smittet eller syk, smitter naboer som er friske uten
   immunitet. Sannsynligheten for å bli smittet av en nabo er 30 %.
   Pass på at personer som blir smittet i dag, ikke smitter videre før
   i morgen.

DEL 3 - SIMULERINGEN
e) Lag et rutenett på 49 ganger 49. Personen i midten er syk, og de fire
   naboene er smittet. Vis rutenettet med fargene over, dag for dag.
f) Vis til slutt hvor mange som var friske, smittet, syke, immune og døde
   hver dag, som en figur med fem kurver.
g) Et hakk over eksamen. En andel av befolkningen er vaksinert fra start og
   kan ikke smittes. Kjør simuleringen med 0 %, 30 % og 60 % vaksinerte.
   Hvor mange dør i hvert tilfelle? Kjør hver variant flere ganger, siden
   svaret varierer.

Tips til tilfeldighet: random.random() gir et tilfeldig tall fra og med 0
og opp til 1. Da er random.random() < 0.3 sant i omtrent 30 % av tilfellene.

Tips til grafikken: et rutenett av tall kan vises med plt.imshow, og
plt.pause oppdaterer figuren mens programmet kjører. Gjør tilstandene om til
tallene 0 til 4, og lag fargene selv:

    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    farger = ListedColormap(['lightgrey', 'pink', 'red', 'dimgrey', 'black'])

    for dag in range(60):
        # ... oppdater populasjonen, og lag rutenettet med tall ...
        plt.clf()
        plt.imshow(tall, cmap=farger, vmin=0, vmax=4)
        plt.title(f'Dag {dag}')
        plt.xlabel('Kolonne')
        plt.ylabel('Rad')
        plt.pause(0.1)
    plt.show()
"""
