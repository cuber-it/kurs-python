# Aufgabe (erfahren): Kursanmeldungen mit Mengen auswerten
#
# Drei Kurse, jeweils eine Liste angemeldeter Personen (mit Duplikaten/Tippfehlern
# musst du dich NICHT herumschlagen – nimm die Namen wie sie sind).
#
# Beantworte mit Mengen-Operationen:
#   1. Wer ist in MINDESTENS einem Kurs?            (Vereinigung)
#   2. Wer ist sowohl in Python ALS AUCH in SQL?    (Schnittmenge)
#   3. Wer ist NUR in Python (in keinem anderen)?   (Differenz)
#   4. Wer besucht GENAU einen der Kurse Python/SQL? (symmetrische Differenz)
#
# Techniken: set(...), | & - ^ bzw. union/intersection/difference.

# E (Eingabe / gegeben)
python_kurs = ["Anna", "Ben", "Cem", "Dora"]
sql_kurs    = ["Ben", "Dora", "Emil"]
web_kurs    = ["Anna", "Emil", "Frida"]

# V (Verarbeitung)
# - zuerst in Sets umwandeln: p = set(python_kurs) usw.
# - 1) p | s | w
# - 2) p & s
# - 3) p - s - w
# - 4) p ^ s
# ...

# A (Ausgabe)
# - jeweils mit erklärendem Text ausgeben
# - Tipp: sorted(menge) macht die Ausgabe stabil/lesbar
# ...
