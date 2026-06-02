# Aufgabe (erfahren): Eigenes Modul schreiben und nutzen
#
# Zwei Dateien arbeiten zusammen:
#   - werkzeug.py     (dein MODUL – die Funktionen, leer vorgegeben)
#   - eigenes_modul.py (dieses Skript – importiert und NUTZT das Modul)
#
# AUFGABE in werkzeug.py:
#   Schreibe dort zwei Funktionen:
#     ist_palindrom(text)  -> True, wenn text vorwärts wie rückwärts gleich ist
#                             (Tipp: text == text[::-1], Groß/klein vorher angleichen)
#     vokale_zaehlen(text) -> Anzahl der Vokale (a,e,i,o,u) im Text
#   Ergänze in werkzeug.py einen if __name__ == "__main__"-Block mit
#   einem kleinen Selbsttest.
#
# AUFGABE hier (eigenes_modul.py):
#   Importiere werkzeug und rufe beide Funktionen mit Beispielen auf.
#   Probiere die drei Import-Varianten aus (import / from..import / as).

# E (Eingabe / Beispiele)
# woerter = ["anna", "otto", "python", "reliefpfeiler"]

# V (Verarbeitung)
# import werkzeug
# for w in woerter:
#     print(w, werkzeug.ist_palindrom(w), werkzeug.vokale_zaehlen(w))

# A (Ausgabe)
# ... pro Wort: Palindrom? und Anzahl Vokale
