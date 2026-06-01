# Tag 3 – Dict (Methoden & Iteration)
#
# Wie man durch ein Dictionary läuft und mit seinen
# Schlüsseln, Werten und Paaren arbeitet.

lager = {"apfel": 50, "birne": 20, "kirsche": 120}

# --- Die drei Sichten ---
print(lager.keys())            # dict_keys(['apfel', 'birne', 'kirsche'])
print(lager.values())          # dict_values([50, 20, 120])
print(lager.items())           # dict_items([('apfel', 50), ...])

# --- Iterieren: Standard läuft über die SCHLÜSSEL ---
for produkt in lager:
    print(produkt)             # apfel / birne / kirsche

# --- Iterieren über Schlüssel UND Wert (der Normalfall!) ---
for produkt, menge in lager.items():
    print(f"{produkt}: {menge} Stück")

# --- Nur Werte ---
print(sum(lager.values()))     # 190   (Gesamtbestand)

# --- setdefault: Wert holen, oder Standard setzen falls fehlt ---
# Liefert vorhandenen Wert ODER legt den Default an und gibt ihn zurück.
print(lager.setdefault("apfel", 0))    # 50   (vorhanden -> unverändert)
print(lager.setdefault("mango", 0))    # 0    (neu angelegt)
print(lager)                           # mango: 0 ist jetzt drin

# --- update: mehrere Paare auf einmal setzen/überschreiben ---
lager.update({"birne": 25, "banane": 60})
print(lager)                   # birne aktualisiert, banane neu

# --- Schlüssel/Werte als Liste weiterverarbeiten ---
produkte = list(lager.keys())
print(produkte)                # ['apfel', 'birne', 'kirsche', 'mango', 'banane']

# --- praktischer Klassiker: größter Bestand ---
# max() mit key= sucht den Schlüssel mit dem höchsten Wert
top = max(lager, key=lager.get)
print(f"Größter Bestand: {top} ({lager[top]})")
