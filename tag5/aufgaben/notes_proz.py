# Eine Notizzettel-Anwendung schreiben
#
# Notizzettel-Speicherungsformat für die Datei
# Datei-Leser
# Datei-Schreiber(überschreibend - immer der gesamte Inhalt)
# Benutzereingabe
# Notizen-Ausgabe
#
# Lösungidee:
# a - klassisch prozedural
# b - mit Klassen und Objekten
#
# Hinweis: alles in eine Datei

# Lösung A:

# Notizzettel – prozedural (alles in einer Datei)
# Speicherformat: eine Notiz pro Zeile, Felder per Tab:  zeit \t tag \t text
# Notizzettel – prozedural (alles in einer Datei)
# Speicherformat: eine Notiz pro Zeile, Felder per Tab:  zeit \t tag \t text
from datetime import datetime

DATEI = "notizen.txt"

def lesen():
    notizen = []
    try:
        with open(DATEI, encoding="utf-8") as f:
            for z in f:
                z = z.rstrip("\n")
                if not z:
                    continue
                zeit, tag, text = z.split("\t", 2)
                notizen.append({"zeit": zeit, "tag": tag, "text": text})
    except FileNotFoundError:
        pass                           # erster Start: noch keine Datei
    return notizen

def schreiben(notizen):
    with open(DATEI, "w", encoding="utf-8") as f:     # ueberschreibt komplett
        for n in notizen:
            f.write(f"{n['zeit']}\t{n['tag']}\t{n['text']}\n")

def anzeigen(notizen):
    if not notizen:
        print("(keine Notizen)")
        return
    for i, n in enumerate(notizen, start=1):
        print(f"{i}. [{n['zeit'].replace('T', ' ')}] ({n['tag']}) {n['text']}")

# --- Aktionen der Menue-Schleife: je eine Funktion ---

def neu(notizen):
    text = input("Notiz: ").strip()
    if not text:
        return
    tag = input("Tag: ").strip()
    notizen.append({
        "zeit": datetime.now().isoformat(timespec="seconds"),
        "tag": tag,
        "text": text,
    })                                 # nur anhaengen, NICHT speichern

def filter(notizen):
    tag = input("Welcher Tag? ").strip()
    anzeigen([n for n in notizen if n["tag"] == tag])

def speichern(notizen):
    schreiben(notizen)
    print(f"{len(notizen)} Notizen gespeichert.")

def main():
    dirty = False
    notizen = lesen()
    while True:
        wahl = input("\n[n]eu  [a]nzeigen  [f]ilter  [s]peichern  [q]uit: ").strip().lower()
        if wahl == "q":
            if dirty:
                choice = input("Änderungen verwerfen (J/N)")
                if choice.lower() == "j":
                    break
            else:
                break
        elif wahl == "n":
            neu(notizen)
            dirty = True
        elif wahl == "a":
            anzeigen(notizen)
        elif wahl == "f":
            filter(notizen)
        elif wahl == "s":
            speichern(notizen)
            dirty = False
        else:
            print("Unbekannte Eingabe.")

if __name__ == "__main__":
    main()
