# venv – virtuelle Umgebungen (Anleitung)

Ein **venv** (virtual environment) ist eine abgeschottete Python-Umgebung pro Projekt. Jedes Projekt bekommt seine eigenen Pakete – ohne sich mit anderen Projekten oder dem System in die Quere zu kommen.

## Warum überhaupt?

Ohne venv landen alle per `pip` installierten Pakete **systemweit**. Spätestens wenn Projekt A `requests 2.31` braucht und Projekt B `requests 2.20`, gibt es Konflikte. Unter Linux Mint / Ubuntu kommt dazu: das System nutzt Python selbst, und ein systemweites `pip install` kann es beschädigen (deshalb meckert pip dort über eine "externally-managed-environment").

**Faustregel: Pro Projekt ein venv. Immer.**

## Anlegen

Im Projektordner:

```
python3 -m venv .venv
```

Das erzeugt einen Ordner `.venv/` mit einer eigenen Python-Kopie. Der Name `.venv` ist Konvention (der Punkt versteckt ihn).

## Aktivieren

Linux / macOS (bash/zsh):

```
source .venv/bin/activate
```

Erkennbar am veränderten Prompt, der jetzt mit `(.venv)` beginnt. Ab jetzt meinen `python` und `pip` die Umgebung – nicht mehr das System.

Windows (PowerShell): `.venv\Scripts\Activate.ps1`

## Arbeiten

```
pip install requests          # landet NUR im venv
pip list                      # zeigt, was im venv ist
pip freeze > requirements.txt # Stand festhalten
```

## Deaktivieren

```
deactivate
```

## Wiederherstellen (z.B. auf anderem Rechner)

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## .gitignore

Der `.venv/`-Ordner gehört **nicht** ins Repository – er ist groß und rechnerspezifisch. Stattdessen versioniert man die `requirements.txt`. In die `.gitignore`:

```
.venv/
__pycache__/
```

## In VS Code

VS Code erkennt das `.venv` meist automatisch. Falls nicht: Kommandopalette (Strg+Shift+P) → "Python: Select Interpreter" → das `.venv` auswählen. Danach nutzen Terminal und "Run" automatisch die richtige Umgebung.
