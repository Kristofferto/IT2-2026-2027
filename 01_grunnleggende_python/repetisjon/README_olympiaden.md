# IT-olympiaden — Soppløpet

Repetisjonsøkt i IT2, 90 minutter. Elevene jobber i grupper på tre med én maskin, og løser ni programmeringsoppgaver som blir vanskeligere. Framgangen vises som et hesteløp på projektoren.

**Løpsbanen:** https://claude.ai/artifact/VZ8GiBKUzZwcsKqjdAMnS3

---

## Filer

| Fil | Til hvem |
|---|---|
| `assert_gjennomgang.py` | storskjerm, første del av økta |
| `olympiade_oppgaver.py` | elevene |
| `olympiade_tester.py` | elevene |
| `olympiade_losning.py` | læreren — deles ikke ut |

---

## Slik går det

**Første del, rundt tjue minutter.** Gjennomgang av `assert`. Kjernen ligger i seksjon 4: en funksjon som består eksempelet fra oppgaveteksten og likevel er feil. Poenget å lande er at ett eksempel aldri er nok.

**Resten av økta.** Gruppene koder i `mine_svar.py` og kjører `olympiade_tester.py`. Testene går i rekkefølge og stopper ved første oppgave som ikke er godkjent — de kommer ikke videre før den er grønn.

Én person koder av gangen. De andre to kan snakke, men ikke røre tastaturet. Bytt etter hver godkjente oppgave.

Hver godkjent oppgave gir en kode. Gruppa skriver den inn på sin egen side, og roper startnummeret sitt til læreren, som flytter hesten på tavla med tastene 1–9.

---

## Oppgavene

Hentet og tilpasset fra eksamen i IN1000 ved Universitetet i Oslo.

| Nr | Funksjon | Tema |
|---|---|---|
| 1 | `samme_sopp` | sammenligning |
| 2 | `tell_giftige` | løkke og telling |
| 3 | `finn_trygg_sopp` | tidlig return, `None` |
| 4 | `jages` | nøstet løkke |
| 5 | `flertall` | ordbok, uavgjort |
| 6 | `kategoriser_sopper` | ordbok med lister, gjenbruk av nr. 2 |
| 7 | `stigespill` | ordbok som oppslag i løkke |
| 8 | `finn_sopp` | nøstet ordbok, to nivåer |
| 9 | `identifiser_sopp` | nøstet ordbok, ukjent dybde |

Oppgave 8 og 9 er paret med vilje. Åtte løses med to omganger etter hverandre, og det er fristende å gjøre det samme i ni — men det går ikke når ingen vet hvor dypt det går.

---

## Løpsbanen

Åpne lenken, velg **Jeg styrer tavla**, legg inn lagene. Hvert lag får et startnummer.

- Tastene **1–9** flytter laget med det nummeret én post fram
- **Backspace** angrer
- Kodene er skjult. *Vis kodene* viser dem et øyeblikk — hold dem skjult på projektor

Elevene åpner samme lenke og velger **Vi er et lag**.

Sidene snakker ikke sammen. Alt lagres i nettleseren på hver maskin, så tavla oppdateres ved at du trykker en tast.

---

## Til neste gang

- Test løpsbanen i forkant. Den husker forrige valg, så trykk *Bytt modus* nederst for å starte på nytt
- Kodene står i klartekst i `olympiade_tester.py`. Bytt dem hvis noen fant dem i fjor — da må også lenkens kodeliste oppdateres
- Kommer et lag gjennom alle ni: be dem skrive egne `assert`-tester med kanttilfeller testfila ikke har
