# Tag 4 – Funktionen, Module, Imports, venv

Aufbauend auf Tag 3: Wir bündeln Code in Funktionen, teilen Programme auf mehrere Dateien (Module) auf, holen uns fremden Code per `import` und lernen mit venv, wie man Projekte und ihre Pakete sauber trennt. Zum Abschluss: automatische Tests mit `unittest`.

## Themen

1. **Funktionen – Grundlagen**
   - `def`, Aufruf, Parameter
   - `return` vs. `print` (und warum eine Funktion ohne `return` `None` liefert)
   - Docstrings

2. **Parameter & Argumente**
   - Positions- vs. Keyword-Argumente
   - Default-Werte
   - Falle: veränderliche Defaults (`liste=[]`)

3. **`*args` & `**kwargs`**
   - beliebig viele Argumente sammeln (Tupel / Dict)
   - Sammlungen beim Aufruf entpacken (`*liste`, `**dict`)

4. **Rückgabewerte & Scope**
   - mehrere Rückgaben (Tupel), frühes `return`
   - lokal vs. global, `UnboundLocalError`, `global` (sparsam!)
   - sauberer Stil: rein per Parameter, raus per `return`

5. **Eigene Module**
   - eine `.py`-Datei als Modul (`geometrie.py`)
   - importieren und nutzen

6. **Import-Varianten & `__name__`**
   - `import` / `from … import` / `as`, warum `import *` vermeiden
   - der Suchpfad (`sys.path`)
   - `if __name__ == "__main__"`

7. **Tour durch die Standardbibliothek**
   - `math`, `random`, `datetime`, `collections`, `os`/`pathlib`, `json`

8. **pip & externe Pakete** *(Erläuterung)*
   - PyPI, `pip install`, `pip list/show/freeze`
   - `requirements.txt`

9. **Unittests**
   - `unittest`, `TestCase`, `test_`-Methoden
   - `assertEqual` / `assertTrue` / `assertRaises` u.a.
   - Tests für `rechner.py`

## Zusätzlich

- **`VENV.md`** – komplette Anleitung zu virtuellen Umgebungen (anlegen, aktivieren, `requirements.txt`, `.gitignore`, VS Code, Mint-Besonderheiten)
- **`geometrie.py`** – Beispielmodul für Kapitel 5/6
- **`rechner.py`** – zu testendes Modul für Kapitel 9

## Lernziel

Du kannst eigene Funktionen mit Parametern und Rückgabewerten schreiben, Code sinnvoll in Module aufteilen und importieren, den Unterschied zwischen lokalem und globalem Scope erklären, mit venv und pip Projekt-Umgebungen sauber verwalten und einfache automatische Tests schreiben.

## Ordnerinhalt

- Themendateien `01_…` bis `09_…`
- `geometrie.py`, `rechner.py` – Beispielmodule
- `VENV.md` – venv-Anleitung
- `aufgaben/` – Übungen (`basic/`, `erfahren/`)
- `experimente/` – Spielwiese
