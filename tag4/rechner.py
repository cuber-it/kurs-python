# Tag 4 – Modul mit Funktionen, die in 09 getestet werden.
#
# Kleine, klar definierte Funktionen lassen sich gut automatisch testen.

def addiere(a, b):
    """Summe zweier Zahlen."""
    return a + b

def teile(a, b):
    """Division. Wirft ValueError bei Division durch 0."""
    if b == 0:
        raise ValueError("Division durch 0 ist nicht erlaubt")
    return a / b

def ist_gerade(n):
    """True, wenn n gerade ist."""
    return n % 2 == 0
