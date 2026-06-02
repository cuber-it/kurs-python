# werkzeug.py – MODUL für die Aufgabe eigenes_modul.py
#
# Hier kommen DEINE Funktionen hinein. Das Gerüst ist vorgegeben,
# die Logik schreibst du selbst.

def ist_palindrom(text):
    """True, wenn text vorwärts wie rückwärts gleich ist."""
    # Tipp: Groß-/Kleinschreibung angleichen, dann mit text[::-1] vergleichen
    pass

def vokale_zaehlen(text):
    """Anzahl der Vokale (a, e, i, o, u) im Text."""
    # Tipp: über die Zeichen laufen und zählen, oder mit "in 'aeiou'"
    pass

# Selbsttest – läuft nur bei direktem Start (python3 werkzeug.py)
if __name__ == "__main__":
    print("Selbsttest werkzeug:")
    # print("anna ->", ist_palindrom("anna"))      # erwartet True
    # print("python ->", ist_palindrom("python"))  # erwartet False
    # print("Vokale in 'python':", vokale_zaehlen("python"))  # erwartet 1
