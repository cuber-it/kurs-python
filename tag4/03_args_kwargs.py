# Tag 4 – *args und **kwargs
#
# Manchmal weiß man vorher nicht, WIE VIELE Argumente kommen.
#   *args     sammelt zusätzliche Positions-Argumente in ein TUPEL
#   **kwargs  sammelt zusätzliche Keyword-Argumente in ein DICT

# --- *args: beliebig viele Positions-Argumente ---
def summe(*zahlen):
    print(zahlen)                      # zahlen ist ein Tupel
    return sum(zahlen)

print(summe(1, 2))                     # (1, 2)    -> 3
print(summe(1, 2, 3, 4, 5))            # (1,2,3,4,5)-> 15
print(summe())                         # ()        -> 0

# Der Name "args" ist Konvention – der * macht die Magie:
def maximum(*werte):
    return max(werte)

print(maximum(7, 2, 9, 4))             # 9

# --- **kwargs: beliebig viele Keyword-Argumente ---
def steckbrief(**daten):
    print(daten)                       # daten ist ein Dict
    for schluessel, wert in daten.items():
        print(f"  {schluessel}: {wert}")

steckbrief(name="Anna", alter=30, stadt="Hamburg")
# {'name': 'Anna', 'alter': 30, 'stadt': 'Hamburg'}
#   name: Anna
#   alter: 30
#   stadt: Hamburg

# --- Alles kombiniert (feste Parameter zuerst, dann *args, dann **kwargs) ---
def report(titel, *posten, **optionen):
    print("Titel:", titel)
    print("Posten:", posten)
    print("Optionen:", optionen)

report("Einkauf", "Milch", "Brot", express=True, rabatt=10)
# Titel: Einkauf
# Posten: ('Milch', 'Brot')
# Optionen: {'express': True, 'rabatt': 10}

# --- Andersherum: Sammlungen BEIM AUFRUF entpacken ---
# *  entpackt eine Liste/ein Tupel in einzelne Positions-Argumente
# ** entpackt ein Dict in einzelne Keyword-Argumente
zahlen = [1, 2, 3]
print(summe(*zahlen))                  # wie summe(1, 2, 3) -> 6

def begruesse(vorname, nachname):
    print(f"Hallo {vorname} {nachname}")

person = {"vorname": "Anna", "nachname": "Müller"}
begruesse(**person)                    # wie begruesse(vorname="Anna", nachname="Müller")
