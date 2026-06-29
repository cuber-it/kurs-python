# Tag 5 – Objektorientierung (Grundlagen)

Aufbauend auf Tag 4: Funktionen bündeln Code, Module bündeln Funktionen. Jetzt bündeln wir **Daten + die dazu passenden Funktionen** an einem Ort – in einer Klasse. Statt lose Dicts durch viele Funktionen zu reichen, bekommt jedes Ding seinen eigenen Bauplan: Attribute (was es *hat*) und Methoden (was es *kann*).

## Themen

1. **Klasse & Objekt**
   - Klasse = Bauplan, Objekt (Instanz) = konkretes Ding
   - Brücke vom bekannten `dict` zur Klasse
   - `class`, Instanz erzeugen, `type()` / `isinstance()`

2. **`__init__` & Attribute**
   - der Konstruktor `__init__`, die Rolle von `self`
   - Instanzattribute setzen und lesen
   - mehrere Objekte sind voneinander unabhängig

3. **Methoden**
   - Funktionen *in* der Klasse, `self` als erstes Argument
   - Attribute lesen und verändern
   - return vs. Zustand ändern

4. **`__str__` & `__repr__`**
   - lesbare Ausgabe für Menschen (`__str__`) und Entwickler (`__repr__`)
   - warum `print(obj)` sonst nur `<… object at 0x…>` zeigt

5. **Klassen- vs. Instanzattribute**
   - was allen Objekten gemeinsam ist (Klassenattribut)
   - der klassische Instanzzähler
   - typische Falle: Klassenattribut versehentlich „überschreiben“

6. **Kapselung & `@property`** *(sanft)*
   - Konvention `_privat`, Namens-Mangling `__sehr_privat`
   - `@property`: Attribut-Syntax mit Funktion dahinter (Getter/Setter)

7. **Vererbung**
   - Basisklasse / Unterklasse, gemeinsamer Code an einer Stelle
   - `super().__init__(...)`, Methoden überschreiben

8. **Polymorphie**
   - gleiche Methode, verschiedene Klassen
   - „duck typing“: es zählt, was ein Objekt *kann*, nicht was es *ist*

9. **`@dataclass`** *(moderne Abkürzung)*
   - `__init__`, `__repr__`, `__eq__` automatisch
   - wann Dataclass, wann normale Klasse

## Zusätzlich

- **`kursreihe.py`** – fertige, lauffähige Klasse `Kursreihe` auf der `quotes.db`.
  Das OOP-Pendant zu Tag 4 `data_source.py`: gleiche Daten, gleiche Kennzahlen,
  aber als Objekt statt als Funktionssammlung. Direkter Vorher/Nachher-Vergleich.

## Lernziel

Du kannst eigene Klassen mit `__init__`, Attributen und Methoden schreiben, den
Unterschied zwischen Klasse und Objekt sowie zwischen Klassen- und Instanzattribut
erklären, Objekte lesbar ausgeben, einfache Vererbung einsetzen und einschätzen,
wann sich OOP gegenüber einem funktionalen Stil lohnt – und wann nicht.

## Ordnerinhalt

- Themendateien `01_…` bis `09_…`
- `kursreihe.py` – Vorführmodul auf der `quotes.db`
- `aufgaben/` – Übungen (`basic/`, `erfahren/`)
- `experimente/` – Spielwiese

## Datenbank

Die `erfahren`-Aufgaben nutzen `materialien/quotes.db` (Tabelle `quotes` mit
`date`, `close`, `volume`) – dieselbe Datenquelle wie an Tag 4.
