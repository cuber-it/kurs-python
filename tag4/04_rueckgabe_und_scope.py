# Tag 4 – Rückgabewerte & Gültigkeitsbereich (Scope)
#
# Wie kommt etwas aus einer Funktion heraus – und welche Variablen
# "sieht" eine Funktion überhaupt?

# --- Mehrere Werte zurückgeben (= ein Tupel, vgl. Tag 3) ---
def min_max(werte):
    return min(werte), max(werte)

kleinste, groesste = min_max([7, 2, 9, 4])   # direkt entpacken
print(kleinste, groesste)                    # 2 9

paar = min_max([5, 1, 8])                     # oder als Tupel auffangen
print(paar)                                   # (1, 8)

# --- return beendet die Funktion sofort ---
def vorzeichen(n):
    if n > 0:
        return "positiv"
    if n < 0:
        return "negativ"
    return "null"                             # alles danach wird nicht erreicht

print(vorzeichen(-3))                          # negativ

# --- Lokaler Scope: Variablen IN der Funktion existieren nur dort ---
def f():
    x = 42                                     # lokal
    print("innen:", x)

f()                                            # innen: 42
# print(x)   -> NameError: x ist außerhalb nicht bekannt!

# --- Globale Variablen kann man LESEN ---
basis = 10
def addiere_basis(n):
    return n + basis                           # basis wird von außen gelesen

print(addiere_basis(5))                        # 15

# --- ... aber ZUWEISEN macht eine NEUE lokale Variable ---
zaehler = 0
def hochzaehlen_falsch():
    zaehler = zaehler + 1                       # Python denkt: zaehler ist lokal
    return zaehler
# hochzaehlen_falsch()  -> UnboundLocalError!

# Wenn man die globale wirklich ändern will: global (sparsam einsetzen!)
def hochzaehlen():
    global zaehler
    zaehler = zaehler + 1
    return zaehler

print(hochzaehlen())                           # 1
print(hochzaehlen())                           # 2

# --- Sauberer Stil: Werte rein per Parameter, raus per return ---
# Statt globalem Zustand lieber:
def hochzaehlen_sauber(stand):
    return stand + 1

stand = 0
stand = hochzaehlen_sauber(stand)
stand = hochzaehlen_sauber(stand)
print(stand)                                   # 2   (nachvollziehbar, kein global)
