# Rolodex - Adresssammlung - Interaktiv
#
# Es gibt eine Datenstruktur - ....
#
# Der Benutzer kann:
#
# einen Eintrag anlegen. Eintrag => Name, Vorname, Tel, Adresse
# einen Eintrag löschen. Kriterium => Tel - mit Bestätigung!
# eine Eintrag suchen. KRiterium => Name oder Tel - alle Treffer werden gezeigt
#
# Erweiterung: Speichern auf Datei / Lesen von Datei
#
#
while True:
    print("ROLO 1.0")
    print("l - Load rolo from file")
    print("s - save rolo to file")
    print("x - quit and save")
    print("n - new entry")
    print("d - delete entry")
    print("f - find by name or phone")

    eingabe = input("Eingabe: ")

    if eingabe.upper() == "X":
        # save!
        print("Bye!")
        exit(0)
