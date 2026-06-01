# Tag 3 – Listen (Grundlagen)
#
# Eine Liste ist eine geordnete, veränderbare (mutable) Sammlung.
# Sie darf gemischte Typen enthalten – in der Praxis sind sie aber
# meist gleichartig (alles Zahlen, alles Strings ...).

# --- Erstellen ---
zahlen = [1, 2, 3, 4, 5]
namen = ["Anna", "Ben", "Cem"]
gemischt = [1, "zwei", 3.0, True]
leer = []                      # leere Liste

# --- Länge ---
print(len(zahlen))             # 5

# --- Indizierung (0-basiert, wie bei Strings) ---
print(namen[0])                # 'Anna'
print(namen[-1])               # 'Cem'   (negativ = von hinten)

# --- Slicing  [start:stop:step]  stop ist exklusiv ---
print(zahlen[1:3])             # [2, 3]
print(zahlen[:2])              # [1, 2]
print(zahlen[::2])             # [1, 3, 5]   (jedes zweite)
print(zahlen[::-1])            # [5, 4, 3, 2, 1]   (umgedreht)

# --- mutable: Listen DARF man ändern (anders als Strings!) ---
namen[0] = "Antje"
print(namen)                   # ['Antje', 'Ben', 'Cem']

# --- Operator "in" ---
print("Ben" in namen)          # True
print("Xaver" in namen)        # False

# --- verschachteln ist erlaubt ---
matrix = [[1, 2, 3],
          [4, 5, 6]]
print(matrix[1][2])            # 6   (Zeile 1, Spalte 2)

# --- ACHTUNG: Zuweisung kopiert NICHT ---
a = [1, 2, 3]
b = a                          # b zeigt auf DIESELBE Liste
b.append(99)
print(a)                       # [1, 2, 3, 99]   <- a ändert sich mit!

# Eine echte Kopie macht man bewusst:
c = a.copy()                   # oder a[:]
c.append(0)
print(a)                       # unverändert
print(c)                       # mit 0 am Ende
