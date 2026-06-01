fname = r"/home/ucuber/Workspace/kurse/kurs-python/materialien/HistoricalQuotes.csv"
# Was folgt könnte man analog auch mit der CSV-Bibliothek bekommen, der Aufwand ist fast der gleiche
quotes = []

with open(fname) as fd:
    # HEADER lesen
    header = fd.readline().replace(" ", "").strip().split(",")

    # Ab der Folgezeile: ...
    for row in fd:
        # Zeile als string, Aufbereiten und Plsitten = liste
        row = row.replace(" ", "").replace("$", "").strip().split(",")
        # Header-Liste (keys) und die Werte (values) zu einer Listen von ITems zusammensetzen und in
        # ein Dict führen. Dieses Dict an das Ende der Liste quotes anhängen
        quotes.append(dict(zip(header, row)))

print(quotes) # Zeigt Liste ( Dict )
print(quotes[0]) # Zeigt das erste Dict

print(quotes[0]['Date'], quotes[0]['Volume']) # Zugriff auf Felder im ersten Dict.

# Zugriff aufdie harte Tour mit Fehler wenns den Key nicht gibt
# quotes[0]['Dingens']

# Freundlich mit Default
print(quotes[0].get('Dingens', 'Gibts wohl nicht!")'))

#----------------------------------
# Das Datum des Handelstages als Key
quotes_by_day = {} # Zielstruktur, Key ist das Datum
for values in quotes: # Über alle Tage hinweg
    new_values = values.copy() # Kopier die Tageswerte, um versehentliche Beschädigung zu verhindern
    date = new_values.pop('Date') # Entferne das Datum, merke dir aber welchen wert es hat
    quotes_by_day[date] = new_values # Trage das Datum ein als Key und die dazugehörigen werte

# Kontrolle
print(quotes[-1])
date = quotes[-1]['Date']
print(quotes_by_day.get(date))
