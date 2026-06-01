# Aufgabe (basic): Eindeutige Wörter zählen
#
# Gegeben ist ein Text. Finde heraus:
#   1. Wie viele Wörter enthält der Text insgesamt?
#   2. Wie viele VERSCHIEDENE Wörter sind es?
#
# Tipps:
#   - text.lower() macht Groß-/Kleinschreibung egal
#   - text.split() zerlegt an Leerzeichen in eine Liste von Wörtern
#   - ein set(...) wirft Duplikate automatisch raus
#
# Bonus: Gib die eindeutigen Wörter alphabetisch sortiert aus.

# E (Eingabe)
text = "die Katze sieht die Maus und die Maus sieht die Katze"

# V (Verarbeitung)
# - in Kleinbuchstaben wandeln und in Wörter zerlegen
# - Gesamtzahl mit len(...) auf die Wortliste
# - Anzahl verschiedener Wörter mit len(set(...))
# ...

# A (Ausgabe)
# - "Wörter gesamt: X"
# - "Verschiedene Wörter: Y"
# ...
