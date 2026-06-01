# Tag 3 – Datenstrukturen: Listen, Tupel, Sets, Dictionaries

Aufbauend auf Tag 1 und 2: Wir verlassen die einzelnen Werte und arbeiten mit Sammlungen. Wann nimmt man eine Liste, wann ein Tupel, wann ein Set, wann ein Dictionary – und welche Arbeitstechniken machen den Code kurz und lesbar?

## Themen

1. **Listen – Grundlagen**
   - erstellen, indizieren, slicen (`[start:stop:step]`)
   - veränderbar (mutable), `in`, `len`, verschachteln
   - die Falle `b = a` (Referenz statt Kopie) und `.copy()`

2. **Listen – Methoden**
   - `append` / `extend` / `insert` / `remove` / `pop`
   - `sort` / `reverse` / `count` / `index` / `clear`
   - Fallen: `append([…])` verschachtelt, `sort()` liefert `None`

3. **Tupel** *(knapp)*
   - unveränderlich (immutable), Komma macht das Tupel
   - Packing / Unpacking, Werte-Swap, Mehrfach-Rückgabe

4. **Sets** *(etwas ausführlicher)*
   - Duplikate entfernen, schnelles `in`
   - `{}` ist ein dict – leeres Set nur mit `set()`
   - Mengenoperationen `| & - ^`, Teilmengen, `frozenset`

5. **Arbeitstechniken mit Listen**
   - List Comprehension (mit Filter / Umformung)
   - `enumerate`, `zip`, `sorted(key=)`
   - `sum` / `min` / `max`, `any` / `all`

6. **Dictionaries – Grundlagen**
   - Schlüssel → Wert, Zugriff `[]` vs. `get()` (mit Default)
   - hinzufügen / ändern / löschen, `in` prüft Schlüssel
   - verschachteln (Werte dürfen Listen / dicts sein)

7. **Dictionaries – Methoden & Iteration**
   - `keys` / `values` / `items`, über `.items()` iterieren
   - `setdefault`, `update`, `max(d, key=d.get)`

8. **Arbeitstechniken mit Dict**
   - Dict Comprehension, `dict(zip(...))`
   - zählen (von Hand und mit `Counter`)
   - gruppieren mit `defaultdict`, nach Wert sortieren

9. **Sonderkapitel: Verschachtelte Strukturen & Struktur-Wahl**
   - Liste von Dicts (der Klassiker für Datensätze)
   - auswerten mit den Techniken von oben
   - Spickzettel: welche Struktur wann?

## Lernziel

Du kannst die vier zentralen Sammlungstypen sicher unterscheiden und einsetzen, sie ineinander verschachteln und mit den gängigen Arbeitstechniken (Comprehensions, `enumerate`/`zip`/`sorted`, `Counter`/`defaultdict`) kompakt und lesbar auswerten.

## Ordnerinhalt

- Beispiele zum jeweiligen Thema (`01_…` bis `09_…`)
- `aufgaben/` – Übungen
- `experimente/` – Spielwiese
- Eigene Lösungen idealerweise unter `loesungen/` ablegen
