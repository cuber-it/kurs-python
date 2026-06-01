# Tag 3 – Listen (Methoden)
#
# Listen bringen viele eingebaute Methoden mit. Wichtig:
# Die meisten verändern die Liste "in place" und geben None zurück!

zahlen = [3, 1, 2]

# --- Hinzufügen ---
zahlen.append(4)               # ein Element ans Ende
print(zahlen)                  # [3, 1, 2, 4]

zahlen.extend([5, 6])          # mehrere Elemente anhängen
print(zahlen)                  # [3, 1, 2, 4, 5, 6]

zahlen.insert(0, 99)           # an Position 0 einfügen
print(zahlen)                  # [99, 3, 1, 2, 4, 5, 6]

# Vorsicht – häufige Falle:
# append([5, 6]) hängt die LISTE als EIN Element an:
test = [1, 2]
test.append([5, 6])
print(test)                    # [1, 2, [5, 6]]   (verschachtelt!)

# --- Entfernen ---
zahlen.remove(99)              # erstes Vorkommen des WERTES 99
print(zahlen)                  # [3, 1, 2, 4, 5, 6]

letztes = zahlen.pop()         # letztes Element entnehmen UND zurückgeben
print(letztes)                 # 6
print(zahlen)                  # [3, 1, 2, 4, 5]

erstes = zahlen.pop(0)         # nach Index entnehmen
print(erstes)                  # 3

# --- Sortieren / Umdrehen (in place!) ---
zahlen.sort()                  # aufsteigend
print(zahlen)                  # [1, 2, 4, 5]

zahlen.sort(reverse=True)      # absteigend
print(zahlen)                  # [5, 4, 2, 1]

zahlen.reverse()               # nur umdrehen (nicht sortieren)
print(zahlen)                  # [1, 2, 4, 5]

# Merke: sort() gibt None zurück!
# x = [3,1,2].sort()  -> x ist None.  Für eine NEUE Liste: sorted(...) (kommt in 05)

# --- Suchen / Zählen ---
werte = [10, 20, 20, 30]
print(werte.count(20))         # 2   (wie oft kommt 20 vor)
print(werte.index(30))         # 3   (an welcher Position)

# --- Komplett leeren ---
werte.clear()
print(werte)                   # []
