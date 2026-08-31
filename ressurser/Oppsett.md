# Sette opp VS Code til IT2

Følg stegene i rekkefølge. Det tar cirka et kvarter første gang, og så er du ferdig med det for resten av året.

Alt du trenger står på denne siden.

---

## Steg 1 — Installer utvidelser

Trykk `Ctrl + Shift + X` for å åpne Extensions-fanen. Søk opp ID-en, trykk **Install**.

| ID                       | Hva den gjør                          |
| ------------------------ | ------------------------------------- |
| `ms-python.python`       | Python-støtte og ordfullføring        |
| `charliermarsh.ruff`     | Rydder og formaterer Python-koden din |
| `esbenp.prettier-vscode` | Formaterer HTML, CSS og JavaScript    |
| `ritwickdey.LiveServer`  | «Go Live»-knappen for nettsider       |

---

## Steg 2 — Lim inn innstillingene

1. Trykk `Ctrl + ,` (Ctrl og komma)
2. Trykk ikonet øverst til høyre som heter **Open Settings (JSON)**
3. **Slett alt** som står i fila
4. Kopier blokka under og lim den inn
5. Lagre med `Ctrl + S`

<details>
<summary><b>Klikk her for å se innstillingene</b></summary>

```jsonc
{
  // === Formattering ved lagring ===
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "prettier.singleQuote": true,

  // === Forslag og ordfullføring ===
  "editor.quickSuggestions": {
    "other": "on",
    "comments": "off",
    "strings": "off",
  },
  "editor.suggestOnTriggerCharacters": true,
  "editor.parameterHints.enabled": true,
  "editor.wordBasedSuggestions": "matchingDocuments",
  "editor.tabCompletion": "on",
  "editor.suggest.preview": true,
  "editor.acceptSuggestionOnCommitCharacter": true,
  "editor.acceptSuggestionOnEnter": "smart",
  "editor.hover.enabled": "on",

  // === Parenteser ===
  "editor.autoClosingBrackets": "always",
  "editor.autoClosingQuotes": "always",
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",

  // === Lesbarhet ===
  "editor.stickyScroll.enabled": true,
  "editor.minimap.enabled": false,
  "editor.codeLens": false,
  "editor.inlayHints.enabled": "off",

  // === Python ===
  "python.defaultInterpreterPath": "${env:LOCALAPPDATA}\\miniconda3\\python.exe",
  "python.terminal.activateEnvironment": true,
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "python.analysis.completeFunctionParens": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.autoClosingBrackets": "always",
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports.ruff": "explicit",
    },
  },

  "chat.disableAIFeatures": true,

  // === Lagring ===
  "files.autoSave": "onFocusChange",
  "liveServer.settings.CustomBrowser": "microsoft-edge",

  // === Grensesnitt ===
  "workbench.startupEditor": "none",
  "workbench.activityBar.location": "default",
  "workbench.statusBar.visible": false,
  "explorer.confirmPasteNative": false,
  "explorer.confirmDragAndDrop": false,
  "claudeCode.preferredLocation": "panel",

  // === Git ===
  "git.path": "C:\\Program Files\\Git\\cmd\\git.exe",
  "git.openRepositoryInParentFolders": "never",
  "git.enableSmartCommit": true,
  "git.confirmSync": false,

  "prettier.jsxSingleQuote": true,
  "ruff.configuration": {
    "format": {
      "quote-style": "single",
    },
  },
  "python.createEnvironment.trigger": "off",
  "terminal.integrated.initialHint": false,

  // === Terminal: PATH for Python og git ===
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "icon": "terminal-powershell",
    },
    "Command Prompt": {
      "path": "C:\\Windows\\System32\\cmd.exe",
      "args": [
        "/k",
        "set PATH=%LOCALAPPDATA%\\miniconda3;%LOCALAPPDATA%\\miniconda3\\Scripts;%LOCALAPPDATA%\\miniconda3\\Library\\bin;C:\\Program Files\\Git\\cmd;%PATH%",
      ],
    },
    "Git Bash": {
      "source": "Git Bash",
      "icon": "terminal-git-bash",
    },
  },
  "terminal.integrated.defaultProfile.windows": "Command Prompt",
}
```

</details>

> **Får du røde streker i fila etter innliming?**
> Da har noe blitt borte i kopieringen, og VS Code ignorerer **alle** innstillingene uten å si fra. Prøv å lime inn på nytt. Virker det fortsatt ikke: si ifra til læreren.

---

## Steg 3 — Åpne en ny terminal

Innstillingene leses bare når en terminal starter. Den som allerede står åpen kan derfor ikke brukes.

1. Er det en terminal åpen: trykk **søppelbøtte-ikonet** for å lukke den. Det holder ikke å åpne en ny fane.
2. Åpne en ny med `Ctrl + Ø`
3. Ledeteksten skal se slik ut:

```
(base) C:\Users\ditt-brukernavn>
```

`(base)` betyr at Python er aktivert. Står det `PS` foran i stedet, er du i feil skall — se feilsøkingen nederst.

Test:

```
where python
git --version
```

`where python` skal gi en liste der **miniconda3 står øverst**.

---

## Navigere i mapper

Terminalen står alltid i én bestemt mappe. Ledeteksten viser hvilken:

```
(base) C:\Users\ditt-brukernavn\Prosjekter\IT2>
```

Disse kommandoene flytter deg rundt:

| Kommando      | Hva den gjør                 |
| ------------- | ---------------------------- |
| `dir`         | viser hva som ligger i mappa |
| `cd IT2`      | gå inn i mappa `IT2`         |
| `cd ..`       | gå ett nivå opp              |
| `cd \`        | helt til toppen av disken    |
| `cd`          | hvor står jeg?               |
| `cls`         | tøm skjermen                 |
| `type fil.py` | vis innholdet i en fil       |

**Trykk Tab.** Skriver du `cd Pro` og trykker Tab, fyller terminalen ut resten av mappenavnet selv. Det sparer deg for skrivefeil, og er den viktigste vanen å ta med seg herfra.

Tre ting som ofte biter:

- **Skråstreken går motsatt vei** av det du er vant til fra nettadresser: `cd Prosjekter\IT2`, ikke `cd Prosjekter/IT2`.
- **Mappenavn med mellomrom** må ha anførselstegn: `cd "Mine dokumenter"`.
- **`ls` og `clear` finnes ikke her.** De hører hjemme i Linux og macOS. I Windows heter de `dir` og `cls`.

---

## Hva er PATH, og hvorfor gjorde vi noe med den?

Når du skriver `python` i terminalen, vet ikke datamaskinen hva du mener. Den må lete etter et program som heter `python.exe`. **PATH** er lista over mapper den leter i.

Python og git er installert på skole-PC-en din gjennom Firmaportalen, men de ligger i mapper som ikke står på den lista. Derfor finner ikke terminalen dem, selv om de er der.

Innstillingene du limte inn legger mappene til i lista — men bare inni VS Code. Resten av Windows er urørt. Åpner du Ledetekst utenfor VS Code, virker `python` fortsatt ikke. Det er som det skal være.

To forskjellige innstillinger gjør hver sin del av jobben:

| Innstilling                            | Hva den fikser                                      |
| -------------------------------------- | --------------------------------------------------- |
| `terminal.integrated.profiles.windows` | at `python`, `pip` og `git` virker i **terminalen** |
| `python.defaultInterpreterPath`        | at **▶-knappen** finner Python                      |

Fordi de er uavhengige, kan det hende at ▶ virker mens terminalen ikke gjør det, eller omvendt.

---

## Om git

`git.path` forteller VS Code hvor git ligger. Uten den er git-fanen i venstremenyen død, selv om `git --version` virker fint i terminalen. Grunnen er at de to leter på hver sin måte.

Du trenger ikke git for de første kapitlene. Er `git --version` det eneste som ikke virker, gå videre og fiks det senere.

---

## Steg 4 — Installer biblioteker

Et **bibliotek** er ferdig kode andre har skrevet, som du henter inn i programmet ditt med `import`. `numpy` regner på tallrekker, `matplotlib` tegner grafer.

Skriv i terminalen:

```
python -m pip install numpy matplotlib
```

Det tar et par minutter og skal ende med «Successfully installed».

> **Skriv `python -m pip`, ikke bare `pip`.**
> Da er du sikker på at pakkene havner hos den Python-installasjonen du faktisk bruker. Dette er den klart vanligste feilen: du installerer noe, og programmet finner det likevel ikke.

Test at det gikk bra. Lag en fil `test.py`:

```python
import numpy
import matplotlib

print(numpy.__version__)
print(matplotlib.__version__)
print('Alt klart!')
```

Kjør den med ▶ øverst til høyre. Kommer det to versjonsnumre og «Alt klart!», er hele oppsettet ferdig.

Senere i året installerer du flere biblioteker på nøyaktig samme måte — bare bytt ut navnet på slutten av kommandoen.

---

## Når det ikke virker

| Symptom                                           | Hva du gjør                                                                                                                                                                                                   |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `where python` gir **ingenting i det hele tatt**  | Se på ledeteksten. Står det `PS` foran, er du i PowerShell, og der betyr `where` noe helt annet. Lukk terminalen med søppelbøtta og åpne en ny — den skal starte i Ledetekst. Eller skriv `where.exe python`. |
| `'python' is not recognized...`                   | Du har en gammel terminal åpen. Lukk den med søppelbøtta og åpne en ny med `Ctrl + Ø`.                                                                                                                        |
| Microsoft Store åpner seg når du skriver `python` | Windows har en snarvei som later som den er Python. Du har en gammel terminal åpen — lukk den og åpne en ny.                                                                                                  |
| `'pip' is not recognized...`                      | Skriv `python -m pip install ...` i stedet for `pip install ...`                                                                                                                                              |
| `'git' is not recognized...`                      | Ny terminal først. Virker det fortsatt ikke, hopp videre — du trenger ikke git ennå.                                                                                                                          |
| `ModuleNotFoundError: No module named 'numpy'`    | Pakken havnet hos feil Python. Se nederst i VS Code-vinduet hvilken tolker som er valgt, og kjør `python -m pip install numpy matplotlib` på nytt.                                                            |
| ▶-knappen gjør ingenting                          | `Ctrl + Shift + P` → skriv **Python: Select Interpreter** → velg den som har «miniconda» i navnet.                                                                                                            |
| `Could not install packages... Permission denied` | Prøv `python -m pip install --user numpy matplotlib`                                                                                                                                                          |
| Ledeteksten viser `(base)`                        | Det er riktig og bra. La den stå.                                                                                                                                                                             |

Får du noe helt annet: ta skjermbilde av **hele** feilmeldingen og vis det til læreren. Ikke bare siste linje.
