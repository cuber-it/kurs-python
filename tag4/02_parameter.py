# Tag 4 – Parameter & Argumente
#
# Begriffe sauber trennen:
#   Parameter = der Platzhalter in der DEFINITION   def f(name): ...
#   Argument  = der konkrete Wert beim AUFRUF        f("Anna")

# --- Mehrere Parameter ---
def rechteck_flaeche(breite, hoehe):
    return breite * hoehe

print(rechteck_flaeche(3, 4))          # 12

# --- Positions-Argumente: Reihenfolge zählt ---
def vorstellen(vorname, nachname):
    print(f"{vorname} {nachname}")

vorstellen("Anna", "Müller")           # Anna Müller
vorstellen("Müller", "Anna")           # Müller Anna   (Reihenfolge vertauscht!)

# --- Keyword-Argumente: Reihenfolge egal, dafür benannt ---
vorstellen(nachname="Müller", vorname="Anna")   # Anna Müller

# --- Default-Werte: Parameter mit Vorgabe ---
def begruesse(name, gruss="Hallo"):
    print(f"{gruss} {name}!")

begruesse("Anna")                      # Hallo Anna!     (Default greift)
begruesse("Ben", "Moin")               # Moin Ben!       (überschrieben)
begruesse("Cem", gruss="Servus")       # Servus Cem!     (per Keyword)

# --- Mischen: erst Positions-, dann Keyword-Argumente ---
def bestellung(artikel, menge=1, express=False):
    print(f"{menge}x {artikel}, express={express}")

bestellung("Kaffee")                   # 1x Kaffee, express=False
bestellung("Tee", 3)                   # 3x Tee, express=False
bestellung("Saft", express=True)       # 1x Saft, express=True   (menge bleibt Default)

# --- ACHTUNG: häufige Falle – KEINE veränderlichen Defaults! ---
# Eine Liste als Default wird nur EINMAL angelegt und bleibt erhalten:
def schlecht(element, liste=[]):       # NICHT so machen!
    liste.append(element)
    return liste

print(schlecht(1))                     # [1]
print(schlecht(2))                     # [1, 2]   <- die alte Liste lebt weiter!

# Richtig: None als Default, Liste innen anlegen
def gut(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

print(gut(1))                          # [1]
print(gut(2))                          # [2]      (jedes Mal frisch)
