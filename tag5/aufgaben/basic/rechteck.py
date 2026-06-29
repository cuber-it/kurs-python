# Aufgabe (basic): Eine Klasse Rechteck
#
# Ziel: Übe Methoden, die aus Attributen etwas BERECHNEN (statt nur Zustand
# zu ändern) – und lerne den Unterschied zur @property kennen.
#
# Anforderungen:
#   - __init__(self, breite, hoehe): speichert beide Seiten
#   - flaeche(self): gibt breite * hoehe zurück
#   - umfang(self): gibt 2 * (breite + hoehe) zurück
#   - ist_quadrat(self): gibt True/False zurück
#   - __str__(self): z. B. "Rechteck 4x3"
#
# Schritt 1: class Rechteck: und __init__ mit breite und hoehe.
# Schritt 2: flaeche und umfang als Methoden mit return.
# Schritt 3: ist_quadrat – Vergleich breite == hoehe direkt zurückgeben.
# Schritt 4: __str__ mit f-String.
#
# Bonus: Mache flaeche zu einer @property, sodass du r.flaeche (OHNE Klammern)
#        schreiben kannst. Überlege: Wann ist @property sinnvoll, wann Methode?

# class Rechteck:
#     def __init__(self, breite, hoehe):
#         ...
#
#     def flaeche(self):
#         ...
#
#     def umfang(self):
#         ...
#
#     def ist_quadrat(self):
#         ...
#
#     def __str__(self):
#         return ...

# --- Test (einkommentieren, wenn die Klasse steht) ---
# r = Rechteck(4, 3)
# print(r)                 # Rechteck 4x3
# print(r.flaeche())       # 12
# print(r.umfang())        # 14
# print(r.ist_quadrat())   # False
# print(Rechteck(5, 5).ist_quadrat())   # True
