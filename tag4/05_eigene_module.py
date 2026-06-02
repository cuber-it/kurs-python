# Tag 4 – Eigene Module
#
# Code in mehrere Dateien aufzuteilen hält Projekte übersichtlich.
# Hier nutzen wir das selbstgeschriebene Modul "geometrie.py" (liegt daneben).

# --- Variante 1: ganzes Modul importieren ---
import geometrie

print(geometrie.kreis_flaeche(2))      # 12.56636
print(geometrie.kreis_umfang(2))       # 12.56636
print(geometrie.PI)                    # 3.14159   (auch Variablen sind nutzbar)

# Der Modulname ist wie ein "Nachname": funktion gehört zum Modul.
# geometrie.kreis_flaeche(...)  =  "die kreis_flaeche AUS geometrie"

# --- Variante 2: nur Bestimmtes importieren (from ... import ...) ---
from geometrie import kreis_flaeche

print(kreis_flaeche(3))                # 28.27431   (jetzt ohne Modul-Präfix)

# --- Variante 3: mit eigenem Kurznamen (as) ---
import geometrie as geo

print(geo.kreis_umfang(1))             # 6.28318

# Merke:
# - import modul          -> modul.funktion()      (klar, woher es kommt)
# - from modul import f   -> f()                    (kürzer, aber weniger eindeutig)
# - import modul as kurz  -> kurz.funktion()        (bei langen Namen praktisch)
#
# Tipp: Wo geometrie.py liegen muss, damit der Import klappt? Im selben
# Ordner wie diese Datei (oder im Suchpfad). Mehr zum Suchpfad in 06.
