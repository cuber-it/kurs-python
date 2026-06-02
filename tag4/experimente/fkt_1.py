

def create_address_dict(keys, values):
    """
    Erstellt ein Dictionary aus zwei Listen.

    Parameter:
        keys: Liste der Schlüssel.
        values: Liste der Werte.

    Rückgabe:
        Dictionary aus Schlüsseln und Werten.

    Exceptions:
        ValueError: Wenn die Listen unterschiedlich lang sind.
    """
    if len(values) != len(keys):
        raise ValueError(
            f"Länge key und value stimmen nicht überein: {keys} {values}"
        )

    return dict(zip(keys, values))

if __name__ == "__main__": # Folgender Code wird ausgeführt wenn nicht via import geladen wurde
    keys = [ "Name", "Vorname", "Strasse", "PLZ", "Ort" ]
    adresse = create_address_dict(keys, ["Watz", "Willi", "Watzplatz 1", "12345", "Watzingen"])
    print(adresse)
