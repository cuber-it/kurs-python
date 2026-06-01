# Rolodex - Adresssammlung - Interaktiv
#
# Es gibt eine Datenstruktur - ....
#
# Liste(Dict)
#
# Rolo = {
#   Willi_PLZ: { Tel:12345, Name: Willi, Vorname:, PLZ:, Strasse:, Ort:}
#   Heinz_PLZ: { Tel:34567, Name: Heinz, ...}
#   ...
# }
# oder:
# Rolo = [
#   { Tel:12345, Name: Willi, Vorname:, PLZ:, Strasse:, Ort:}
#   { Tel:34567, Name: Heinz, ...}
#   ...
# ]
#
# Der Benutzer kann:
#
# einen Eintrag anlegen. Eintrag => Name, Vorname, Tel, Adresse (Pflichtwerte!)
# einen Eintrag löschen. Kriterium => Tel - mit Bestätigung!
# eine Eintrag suchen. KRiterium => Name und PLZ - alle Treffer werden gezeigt
#
# Erweiterung: Speichern auf Datei / Lesen von Datei
#
#
rolo = []

while True:
    print("ROLO 1.0")
    print("l - Load rolo from file")
    print("s - save rolo to file")
    print("x - quit and save")
    print("n - new entry")
    print("d - delete entry")
    print("f - find by name or phone")
    print("p - alles ausgeben")
    eingabe = input("Eingabe: ").upper()

    if eingabe == "X":
        # save!
        print("Bye!")
        exit(0)
    elif eingabe == "N":
        daten = input("Name,Vorname,Tel,PLZ,Ort,Strasse: ").split(",")
        if len(daten) != 6:
            print("Daten unvollständig! Keine Übernahme")
        else:
            # Ohne Doublettenprüfung im Rolo, daher:
            rolo.append({
                "Name":    daten[0],
                "Vorname": daten[1],
                "Tel":     daten[2],
                "PLZ":     daten[3],
                "Ort":     daten[4],
                "Strasse": daten[5]
            })
            print("check!")
    elif eingabe == "F":
        daten = input("Feldname, Suchwert: ").split(",")
        if len(daten) != 2:
            print("Suche nciht möglich, Feld und Wert angeben")
        else:
            feld, wert = daten
            for row in rolo:
                if row.get(feld, None) == wert:
                    print(row)
    elif eingabe == "P":
        for row in rolo:
            print(row)
    elif eingabe == "S":
        if len(rolo) == 0:
            print("Nichts zu speichern. Abbruch!")
        else:
            header = ",".join(list(rolo[0].keys()))
            with open("rolo.csv", "w") as fd:
                print(header, file=fd)
                for row in rolo:
                    row = ",".join(list(row.values()))
                    print(row, file=fd)
            print("check")

    else:
        print("Kommando noch nicht gebaut oder unbekannt")
