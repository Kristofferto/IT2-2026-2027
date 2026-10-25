# Hent koden med git

## Første gang

Skriv dette i terminalen i VS Code:

```
mkdir %USERPROFILE%\Prosjekter
cd /d %USERPROFILE%\Prosjekter
git clone https://github.com/Kristofferto/IT2-2026-2027.git
```

Da ligger hele repoet i `Prosjekter\IT2-2026-2027`.

## Når det er lagt ut noe nytt

```
git -C %USERPROFILE%\Prosjekter\IT2-2026-2027 pull
```

## Ikke endre noe i `IT2-2026-2027`

Mappa er bare til å lese og kopiere fra. Din egen kode legger du i din egen mappe ved siden av, for eksempel `Prosjekter\IT2`, med den mappestrukturen du vil. Trenger du en fil fra timen, kopierer du den dit, og husk `data/`-mappa hvis koden leser en fil.

Endrer du noe i `IT2-2026-2027`, kan `git pull` stoppe.
