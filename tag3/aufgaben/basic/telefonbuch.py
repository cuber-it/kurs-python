# Aufgabe (basic): Mini-Telefonbuch
#
# Verwalte Namen und Telefonnummern in einem Dictionary.
#
# Schritt 1: Lege ein dict mit ein paar Einträgen an (Name -> Nummer).
# Schritt 2: Frage einen Namen ab und gib die passende Nummer aus.
#            Wenn der Name nicht existiert: freundliche Meldung statt Absturz!
# Schritt 3: Erlaube das Hinzufügen eines neuen Eintrags.
#
# Tipp: .get(name) liefert None statt KeyError, wenn der Name fehlt.

# E (Eingabe)
telefonbuch = {
    "Anna": "0151-111",
    "Ben": "0151-222",
}
gesuchter_name = input("Wen suchst du? ")

# V (Verarbeitung)
# - mit .get(gesuchter_name) nachschlagen
# - Ergebnis prüfen: gefunden oder nicht?
# ...

# A (Ausgabe)
# - gefunden:  "Nummer von X: ..."
# - nicht da:  "X ist nicht im Telefonbuch."
# ...
