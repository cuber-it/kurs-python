# Tag 3 – Arbeitstechniken mit Listen
#
# Hier kommen die "Tricks", die Python-Code kurz und lesbar machen.
# Diese Techniken trennen Anfänger von fortgeschrittenen Schreibern.

zahlen = [1, 2, 3, 4, 5, 6]

# --- List Comprehension ---
# Statt:
quadrate = []
for n in zahlen:
    quadrate.append(n ** 2)
print(quadrate)                # [1, 4, 9, 16, 25, 36]

# ... kürzer in EINER Zeile:
quadrate = [n ** 2 for n in zahlen]
print(quadrate)                # [1, 4, 9, 16, 25, 36]

# mit Bedingung (Filter):
gerade = [n for n in zahlen if n % 2 == 0]
print(gerade)                  # [2, 4, 6]

# mit Umformung + Filter:
namen = ["anna", "ben", "cem"]
gross = [name.upper() for name in namen if len(name) > 3]
print(gross)                   # ['ANNA']

# --- enumerate: Index UND Wert zugleich ---
for i, name in enumerate(namen):
    print(i, name)             # 0 anna / 1 ben / 2 cem

# Start-Index frei wählbar:
for nr, name in enumerate(namen, start=1):
    print(f"{nr}. {name}")     # 1. anna / 2. ben / ...

# --- zip: zwei Listen parallel durchlaufen ---
preise = [2.50, 1.20, 3.00]
for name, preis in zip(namen, preise):
    print(f"{name}: {preis:.2f} €")

# --- sorted(): liefert eine NEUE sortierte Liste (Original bleibt) ---
unsortiert = [3, 1, 2]
print(sorted(unsortiert))      # [1, 2, 3]
print(unsortiert)              # [3, 1, 2]   (unverändert!)

# nach eigenem Kriterium sortieren (key=):
worte = ["banane", "ei", "apfel"]
print(sorted(worte, key=len))             # ['ei', 'apfel', 'banane']  (nach Länge)
print(sorted(worte, key=len, reverse=True))

# --- nützliche Built-ins für Zahlenlisten ---
werte = [10, 5, 8, 3]
print(sum(werte))              # 26
print(min(werte), max(werte))  # 3 10
print(len(werte))              # 4
print(sum(werte) / len(werte)) # 6.5   (Durchschnitt)

# --- any / all: schnelle Wahrheitsprüfung ---
print(any(n > 8 for n in werte))   # True   (mind. einer > 8)
print(all(n > 0 for n in werte))   # True   (alle > 0)
