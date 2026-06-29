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

# Lösung B:

# Notizzettel – einfachstes OOP (alles in einer Datei)
# Speicherformat: eine Notiz pro Zeile, Felder per Tab:  zeit \t tag \t text
from datetime import datetime

class Notiz:
    pass # TBD :-D

class Notizbuch:
    def __init__(self, datei="notizen.txt"):
        self.datei = datei
        self.notizen = self.lesen()

    def lesen(self):
        notizen = []
        try:
            with open(self.datei, encoding="utf-8") as f:
                for z in f:
                    z = z.rstrip("\n")
                    if not z:
                        continue
                    zeit, tag, text = z.split("\t", 2)
                    notizen.append({"zeit": zeit, "tag": tag, "text": text})
        except FileNotFoundError:
            pass                       # erster Start: noch keine Datei
        return notizen

    def schreiben(self):
        with open(self.datei, "w", encoding="utf-8") as f:   # ueberschreibt komplett
            for n in self.notizen:
                f.write(f"{n['zeit']}\t{n['tag']}\t{n['text']}\n")

    def hinzufuegen(self, text, tag):
        self.notizen.append({
            "zeit": datetime.now().isoformat(timespec="seconds"),
            "tag": tag,
            "text": text,
        })                             # nur anhaengen, NICHT speichern

    def filtern(self, tag):
        return [n for n in self.notizen if n["tag"] == tag]

    def anzeigen(self, notizen):
        if not notizen:
            print("(keine Notizen)")
            return
        for i, n in enumerate(notizen, start=1):
            print(f"{i}. [{n['zeit'].replace('T', ' ')}] ({n['tag']}) {n['text']}")

class MyNotesApp:
    def __init__(self, notes):
        self.buch = notes

    def run(self):
        while True:
            wahl = input("\n[n]eu  [a]nzeigen  [f]ilter  [s]peichern  [q]uit: ").strip().lower()
            if wahl == "q":
                break
            elif wahl == "n":
                text = input("Notiz: ").strip()
                if text:
                    tag = input("Tag: ").strip()
                    self.buch.hinzufuegen(text, tag)
            elif wahl == "a":
                self.buch.anzeigen(self.buch.notizen)
            elif wahl == "f":
                tag = input("Welcher Tag? ").strip()
                self.buch.anzeigen(self.buch.filtern(tag))
            elif wahl == "s":
                self.buch.schreiben()
                print(f"{len(self.buch.notizen)} Notizen gespeichert.")
            else:
                print("Unbekannte Eingabe.")

if __name__ == "__main__":
    MyNotesApp(Notizbuch()).run()
