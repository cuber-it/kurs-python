# Tag 5 – Klasse & Objekt
#
# OOP-Grundidee: Wir bündeln zusammengehörige DATEN und die FUNKTIONEN,
# die damit arbeiten, an einem Ort – in einer Klasse.
#
#   Klasse  = der BAUPLAN  (z. B. "Hund" allgemein)
#   Objekt  = ein konkretes DING nach dem Bauplan (z. B. "Rex")
#
# Ein Bauplan beschreibt nur. Erst aus dem Bauplan entstehen echte Objekte
# (man sagt: "Instanzen"). Aus EINEM Bauplan beliebig viele.

# --- Was wir schon kennen: ein dict als "Datenbündel" ---
hund1 = {"name": "Rex", "alter": 3}
hund2 = {"name": "Bella", "alter": 5}
print(hund1["name"])               # Rex

# Das funktioniert, aber: Die Funktionen, die mit so einem Hund arbeiten,
# liegen lose woanders. Eine Klasse holt Daten UND Verhalten zusammen.

# --- Die einfachste Klasse ---
class Hund:
    pass                           # noch leer (nur der Bauplan-Rahmen)

# --- Objekte (Instanzen) erzeugen: Klasse wie eine Funktion aufrufen ---
rex = Hund()
bella = Hund()

# Attribute lassen sich (vorerst) direkt von außen setzen:
rex.name = "Rex"
rex.alter = 3
bella.name = "Bella"
bella.alter = 5

print(rex.name)                    # Rex
print(bella.alter)                 # 5

# rex und bella sind ZWEI verschiedene Objekte – unabhängig voneinander:
print(rex is bella)                # False

# --- type() und isinstance(): Womit habe ich es zu tun? ---
print(type(rex))                   # <class '__main__.Hund'>
print(isinstance(rex, Hund))       # True
print(isinstance(rex, dict))       # False

# Merke: Auch alles Bekannte ist intern eine Klasse.
print(type("hallo"))               # <class 'str'>
print(type([1, 2, 3]))             # <class 'list'>
print(type(42))                    # <class 'int'>
# "abc".upper() ist ein Methodenaufruf auf einem str-Objekt – OOP nutzt ihr längst!

# --- Warum nicht einfach beim dict bleiben? ---
# Beim dict kann jeder Eintrag anders aussehen, Tippfehler in Schlüsseln fallen
# erst spät auf, und das Verhalten liegt getrennt herum. Eine Klasse gibt allen
# Objekten dieselbe Struktur und packt das passende Verhalten direkt dazu.
# Wie das sauber geht (Attribute schon beim Erzeugen), kommt in 02.
