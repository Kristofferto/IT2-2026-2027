"""
IT2 - IT-OLYMPIADEN

Ni oppgaver. De blir vanskeligere.

SLIK FUNGERER DET
  Dere er tre på laget og har én maskin.
  Én person koder av gangen, og bytter etter hver løste oppgave.
  De andre to kan snakke, men ikke røre tastaturet.

  Lagre funksjonene i mine_svar.py og kjør olympiade_tester.py.
  Dere kommer ikke videre til neste oppgave før den forrige er grønn.

  Testene som står i hver oppgave er de samme som testfila bruker.
  Begge må passere.

  Bruk nøyaktig de funksjonsnavnene som står i oppgaven.

Oppgavene er hentet og tilpasset fra eksamen i IN1000 ved
Universitetet i Oslo.

REGELEN: ikke bruk sum(), max(), min(), count() eller set().
"""

"""
1. SAMME SOPP

Per, Kari og Nils plukker én sopp hver. Skriv
samme_sopp(per_sopp, kari_sopp, nils_sopp) som tar tre strenger og
returnerer True hvis minst to av dem er like.

    assert samme_sopp('kantarell', 'fluesopp', 'kantarell') == True
    assert samme_sopp('kantarell', 'fluesopp', 'steinsopp') == False
"""


"""
2. TELL GIFTIGE

Skriv tell_giftige(giftige, plukket) som tar to lister med strenger
og returnerer hvor mange av soppene i plukket som står i giftige.
Samme sopp kan være plukket flere ganger og telles hver gang.

    assert tell_giftige(['fluesopp', 'hvit fluesopp'],
                        ['kantarell', 'fluesopp', 'steinsopp']) == 1

    assert tell_giftige(['fluesopp'],
                        ['fluesopp', 'fluesopp', 'kantarell']) == 2
"""


"""
3. FINN TRYGG SOPP

Skriv finn_trygg_sopp(giftige, plukket) som returnerer navnet på den
FØRSTE soppen i plukket som ikke er giftig. Er alle giftige, returner
None.

    assert finn_trygg_sopp(['fluesopp'],
                           ['fluesopp', 'kantarell', 'steinsopp']) == 'kantarell'

    assert finn_trygg_sopp(['fluesopp', 'kantarell'],
                           ['fluesopp', 'kantarell']) == None
"""


"""
4. JAGES

Skriv jages(dyreliste) som tar en liste der hvert element er 'mus',
'katt' eller 'hund'. En hund jager katt, en katt jager mus. Returner
True hvis noen i lista vil jage noen andre i lista.

    assert jages(['mus', 'katt']) == True
    assert jages(['mus', 'mus', 'hund']) == False
"""


"""
5. FLERTALL

Skriv flertall(dyreliste) som returnerer navnet på det dyret det
finnes flest av. Er det likt mellom to, returner 'uavgjort'.

    assert flertall(['ulv', 'sau', 'ulv']) == 'ulv'
    assert flertall(['ulv', 'sau', 'sau', 'ulv']) == 'uavgjort'
"""


"""
6. KATEGORISER SOPPER

Skriv kategoriser_sopper(kategorier, plukket).

kategorier er en ordbok der nøkkelen er et kategorinavn og verdien er
en liste med sopper i den kategorien. En sopp kan være i flere
kategorier. plukket er en liste med sopper fra turen.

Returner en ordbok der nøkkelen er kategorinavn og verdien er hvor
mange av de plukkede soppene som hører til der. Kategorier uten treff
skal IKKE være med.

Bruk tell_giftige fra oppgave 2 som en del av løsningen.

    assert kategoriser_sopper(
        {'giftige': ['fluesopp', 'spiss giftslørsopp'],
         'matsopper': ['kantarell', 'fluesopp']},
        ['kantarell', 'fluesopp', 'steinsopp']) == {'giftige': 1, 'matsopper': 2}

    assert kategoriser_sopper(
        {'giftige': ['fluesopp']},
        ['kantarell']) == {}
"""


"""
7. STIGESPILLET

Du starter på rute 0. For hvert terningkast flytter du fram så mange
ruter. Lander du på en rute der en stige begynner, følger du stigen
til ruten den ender på.

Skriv stigespill(terningkast, stiger) der terningkast er en liste med
heltall og stiger er en ordbok med startrute som nøkkel og sluttrute
som verdi. Returner posisjonen etter alle kastene.

    assert stigespill([5, 4, 2, 2], {5: 12, 18: 7}) == 9
    assert stigespill([3, 3], {3: 20}) == 23
"""


"""
8. FINN SOPP

En soppguide er en nøstet ordbok på to nivåer. Nøklene er egenskaper,
og innerst ligger soppnavnet.

Skriv finn_sopp(egenskaper1, egenskaper2, soppguide).

Finn først hvilke nøkler på FØRSTE nivå som står i egenskaper1. Er det
nøyaktig én, gå inn i den indre ordboka og finn hvilke nøkler der som
står i egenskaper2. Er det igjen nøyaktig én, returner soppnavnet.

Er det på noe nivå null eller flere enn én som passer, returner
strengen 'uklar'.

    assert finn_sopp(['rød', 'stor'], ['prikker'],
                     {'rød': {'prikker': 'fluesopp',
                              'brune lameller': 'rødskivesopp'},
                      'brun': {'prikker': 'sjampinjong'}}) == 'fluesopp'

    assert finn_sopp(['rød', 'brun'], ['prikker'],
                     {'rød': {'prikker': 'fluesopp'},
                      'brun': {'prikker': 'sjampinjong'}}) == 'uklar'
"""


"""
9. IDENTIFISER SOPP

Nå kan soppguiden være nøstet i hvor mange nivåer som helst.

Skriv identifiser_sopp(egenskaper, soppguide) som tar ÉN liste med
egenskaper og en ordbok som kan være nøstet vilkårlig dypt.

På hvert nivå: finn hvilke nøkler som står i egenskaper.
  - Er det nøyaktig én, se på verdien.
      Er verdien en ordbok, gå videre til neste nivå.
      Er verdien en streng, har du funnet soppen. Returner den.
  - Er det null eller flere enn én, returner 'uklar'.

Hint: type(verdi) == dict sjekker om noe er en ordbok,
type(verdi) == str sjekker om det er en streng.

    assert identifiser_sopp(['rød', 'prikker'],
                            {'rød': {'prikker': 'fluesopp'}}) == 'fluesopp'

    assert identifiser_sopp(['rød'],
                            {'rød': {'prikker': 'fluesopp',
                                     'brune lameller': 'rødskivesopp'}}) == 'uklar'
"""
