# Aufgabe (basic): Einkaufsliste verwalten
#
# Schreibe ein Programm, das eine Einkaufsliste verwaltet.
#
# Schritt 1: Lege eine Liste mit ein paar Artikeln an.
# Schritt 2: Frage den Benutzer nach einem neuen Artikel und füge ihn hinzu.
# Schritt 3: Prüfe vor dem Hinzufügen, ob der Artikel schon drin ist
#            (dann nicht doppelt aufnehmen).
# Schritt 4: Gib die Liste alphabetisch sortiert und durchnummeriert aus.
#
# Bonus: Lass den Benutzer einen Artikel auch wieder entfernen.

# E (Eingabe)
einkaufsliste = ["Milch", "Brot", "Eier"]
neuer_artikel = input("Welcher Artikel soll dazu? ")

# V (Verarbeitung)
# - prüfen mit "in", ob neuer_artikel schon vorhanden ist
# - sonst mit .append() hinzufügen
# - mit sorted(...) eine sortierte Fassung erzeugen
# ...

# A (Ausgabe)
# - Tipp: for nr, artikel in enumerate(..., start=1): print(f"{nr}. {artikel}")
# ...
