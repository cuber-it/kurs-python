# Tag 1 – Variablen
#
# Eine Variable ist ein Name für einen Wert.
# Python ist dynamisch typisiert: derselbe Name darf
# später auf einen Wert eines anderen Typs zeigen.

# Zuweisung mit "="
name = "Ulrich"
alter = 42
groesse = 1.83
ist_dozent = True

# Mehrere Zuweisungen auf einmal
a, b, c = 1, 2, 3

# Werte ändern (auch der Typ darf wechseln)
zahl = 10
zahl = "jetzt ein Text"

# Mit type() lässt sich der aktuelle Typ prüfen
print(type(name))
print(type(alter))
print(type(zahl))

# Konvention: snake_case für Variablennamen
mein_lieblings_essen = "Pasta"
print(mein_lieblings_essen)
