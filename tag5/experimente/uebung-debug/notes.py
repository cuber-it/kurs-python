from datetime import datetime
from pathlib import Path

DATEN_DATEI = Path(__file__).with_name("notizen.txt")
#r"/home/ucuber/Workspace/kurse/kurs-python/tag5/experimente/uebung-debug/notizen.txt"
DATEI_KOPFZEILE = "Added;Schlagwort"


def sortiere_notizen_chronologisch(notizen: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(notizen, key=lambda eintrag: eintrag.get("Added", ""))



def lade_notizen() -> list[dict[str, str]]:
    if not DATEN_DATEI.exists():
        return []

    try:
        with DATEN_DATEI.open("r", encoding="utf-8-sig") as datei:
            zeilen = datei.read().splitlines()
    except OSError:
        return []

    if not zeilen:
        return []

    notizen = []

    for zeile in zeilen:
        print(zeile)

        if zeile.lower() == "added;schlagwort":
            continue
        if ";" not in zeile:
            continue
        zeitpunkt, schlagwort = zeile.split(";")

        zeitpunkt = zeitpunkt.strip()
        schlagwort = schlagwort.strip()
        if not zeitpunkt or not schlagwort:
            continue
        notizen.append({"Added": zeitpunkt, "Schlagwort": schlagwort})

    return sortiere_notizen_chronologisch(notizen)


def speichere_notizen(notizen: list[dict[str, str]]) -> None:
    sortiert = sortiere_notizen_chronologisch(notizen)
    with DATEN_DATEI.open("w", encoding="utf-8") as datei:
        datei.write(f"{DATEI_KOPFZEILE}\n")
        for eintrag in sortiert:
            zeitpunkt = eintrag.get("Added", "")
            schlagwort = eintrag.get("Schlagwort", "").replace("\n", " ").strip()
            if zeitpunkt and schlagwort:
                datei.write(f"{zeitpunkt};{schlagwort}\n")


def notiz_hinzufuegen(notizen: list[dict[str, str]]) -> None:
    schlagwort = input("Schlagwort eingeben: ").strip()
    if not schlagwort:
        print("Leere Notiz wurde nicht gespeichert.")
        return

    notizen.append(
        {
            "Added": datetime.now().isoformat(timespec="seconds"),
            "Schlagwort": schlagwort,
        }
    )
    speichere_notizen(notizen)
    print("Notiz gespeichert.")


def notizen_anzeigen(notizen: list[dict[str, str]]) -> None:
    if not notizen:
        print("Keine Notizen vorhanden.")
        return

    print("\nNotizen (chronologisch):")
    sortiert = sortiere_notizen_chronologisch(notizen)
    for index, eintrag in enumerate(sortiert, start=1):
        zeitpunkt = eintrag.get("Added", "unbekannt")
        schlagwort = eintrag.get("Schlagwort", "")
        print(f"{index}. [{zeitpunkt}] Schlagwort: {schlagwort}")

def menue() -> None:
    notizen = lade_notizen()

    while True:
        print("\n--- Notizzettel ---")
        print("1 - Notiz hinzufuegen")
        print("2 - Notizen anzeigen")
        print("3 - Beenden")

        auswahl = input("Auswahl: ").strip()

        if auswahl == "1":
            notiz_hinzufuegen(notizen)
        elif auswahl == "2":
            notizen_anzeigen(notizen)
        elif auswahl == "3":
            print("Programm beendet.")
            break
        else:
            print("Ungueltige Auswahl. Bitte 1, 2 oder 3 eingeben.")


if __name__ == "__main__":
    menue()
