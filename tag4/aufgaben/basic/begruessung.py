# Aufgabe (basic): Begrüßung mit Default-Parameter
#
# Schreibe eine Funktion begruesse(name, gruss="Hallo"), die einen Satz
# ausgibt, z.B. "Hallo Anna!".
#
# Schritt 1: Funktion mit zwei Parametern – der zweite hat einen Default.
# Schritt 2: Rufe sie auf drei Arten auf:
#            a) nur mit Namen        -> Default-Gruß greift
#            b) mit eigenem Gruß     -> als Positions-Argument
#            c) mit gruss=...        -> als Keyword-Argument
#
# Ziel: den Unterschied zwischen Default-, Positions- und Keyword-Argument
#       am eigenen Beispiel sehen.

# V (Verarbeitung – die Funktion)
# def begruesse(name, gruss="Hallo"):
#     ...

# A (Ausgabe – die drei Aufrufe)
# begruesse("Anna")
# begruesse("Ben", "Moin")
# begruesse("Cem", gruss="Servus")
# ...
