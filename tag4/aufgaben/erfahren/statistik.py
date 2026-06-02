# Aufgabe (erfahren): Statistik-Funktion mit mehreren Rückgabewerten
#
# Schreibe eine Funktion statistik(*zahlen), die GLEICHZEITIG zurückgibt:
#   - das Minimum
#   - das Maximum
#   - den Durchschnitt (gerundet auf 2 Stellen)
#
# Anforderungen:
#   - Nimm beliebig viele Zahlen über *args entgegen.
#   - Gib die drei Werte als Tupel zurück (return a, b, c).
#   - Fange den Sonderfall "keine Zahlen" sinnvoll ab (z.B. (0, 0, 0)
#     oder eine Fehlermeldung – deine Entscheidung).
#
# Beim Aufruf das Ergebnis per Unpacking auffangen:
#   mini, maxi, schnitt = statistik(...)

# V (Verarbeitung – die Funktion)
# def statistik(*zahlen):
#     if not zahlen:
#         return ...            # Sonderfall
#     mini = min(zahlen)
#     maxi = max(zahlen)
#     schnitt = round(sum(zahlen) / len(zahlen), 2)
#     return mini, maxi, schnitt

# A (Ausgabe)
# mini, maxi, schnitt = statistik(7, 2, 9, 4)
# print(f"min={mini}, max={maxi}, schnitt={schnitt}")
# ...
