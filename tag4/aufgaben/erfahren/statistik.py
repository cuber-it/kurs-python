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

def min(*args):
    result = args[0]

    for x in args[1:]:
        if x < result:
            result = x
    return result

def max(*args):
    result = args[0]
    for x in args[1:]:
        if x > result:
            result = x
    return result

def sum(*args):
    result = 0
    for x in args:
        result += x
    return result

def mean(*args):
    if len(args) == 0:
        raise ValueError("Leere Werte")
    return sum(*args) / len(args)

if __name__ == "__main__":
    werte = [ -1, 0, 1, 2, 3, 4, 5]
    print(max(-1, 0, 1, 2, 3, 4, 5))
    print(min(*werte)) # * werte entpackt die Liste zu -1, 0, 1, 2, 3, 4, 5
    print(sum(*werte))
