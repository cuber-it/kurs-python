# Tag 4 – Hilfsmodul (wird von 05_eigene_module.py importiert)
#
# Ein "Modul" ist einfach eine .py-Datei. Alles, was hier definiert wird
# (Funktionen, Variablen), kann eine andere Datei importieren und nutzen.

PI = 3.14159

def kreis_flaeche(radius):
    """Fläche eines Kreises."""
    return PI * radius * radius

def kreis_umfang(radius):
    """Umfang eines Kreises."""
    return 2 * PI * radius

# Dieser Block läuft NUR, wenn die Datei direkt gestartet wird
# (python3 geometrie.py), NICHT beim Import. Mehr dazu in 06.
if __name__ == "__main__":
    print("Selbsttest des Moduls geometrie:")
    print("Fläche r=2:", kreis_flaeche(2))
    print("Umfang r=2:", kreis_umfang(2))
