# Tag 2 – Strings, Kontrollstrukturen, Imports, Dateien, Fehlerbehandlung

Aufbauend auf Tag 1: Texte verarbeiten, Programme verzweigen und wiederholen, Module nutzen, Dateien einlesen und Fehler abfangen.

## Themen

1. **Strings (Schwerpunkt)**
   - Slicing
   - Methoden: `.upper`, `.lower`, `.strip`, `.split`, `.replace`, `.find`, `.startswith`
   - `len()` und der `in`-Operator
   - Immutability (Strings sind unveränderlich)

2. **`if` / `elif` / `else`**
   - klassische Verzweigung
   - **Einzeiler** (ternärer Ausdruck): `wert = a if bedingung else b`
   - Wahrheitswerte und Truthiness
   - Einrückung als Syntaxelement

3. **`while`-Schleife** – inkl. `break`, `continue`

4. **`for`-Schleife** – mit `range()` und über Strings / Dateizeilen

5. **Sonderkapitel: Moderne Kontrollstrukturen**
   - `match` / `case` (seit Python 3.10) – Anriss

6. **Import-Grundlagen**
   - `import modul`, `from modul import name`, `as`
   - kurzer Streifzug durch die Standardbibliothek (`math`, `random`, …)

7. **Datei-Input**
   - `with open(...) as f:`
   - zeilenweise lesen

8. **Fehlerbehandlung**
   - `try` / `except` / `else` / `finally`
   - typische Exceptions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`)
   - bewusst Fehler werfen mit `raise`

## Lernziel

Du kannst Programme schreiben, die Texte gezielt verarbeiten, auf Eingaben unterschiedlich reagieren, vorhandene Module nutzen, Dateien einlesen und mit Fehlern sauber umgehen.

## Ordnerinhalt

- Beispiele und Übungen zum jeweiligen Thema
- Eigene Lösungen idealerweise unter `loesungen/` ablegen
