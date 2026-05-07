# Aufgabe: Ein einfaches Rechner-Programm
#
# Schritt 1:
#
# Benutzer gibt 2 Zahlen ein -> float, egl. und dt. Schreibweise erlaubt
# Benutzer gibt einen Operator ein (+ - * /)
# Die Rechenoperation wird ausgeführt, das Ergebnis ausgegeben
#
# Schritt 2: Der Benutzer kann das so lange laufen lassen, bis er exit eingibt,
# Es werden immer Einzelberechnungen ausgeführt
#
# Und wenn der Benutzer Mist eingibt? -> dann passiert eben eine Exception, na und!

while True:
    # E
    zahl_1 = float(input("Zahl 1: ").replace(",", "."))
    zahl_2 = float(input("Zahl 2: ").replace(",", "."))
    operator = input("+ - * /:")

    # V
    ergebnis = None

    if operator == '+':
        ergebnis = zahl_1 + zahl_2
    elif operator == '-':
        ergebnis = zahl_1 - zahl_2
    elif operator == '*':
        ergebnis = zahl_1 * zahl_2
    elif operator == '/':
        ergebnis = zahl_1 / zahl_2
    else:
        print("Kenn ich nicht:", operator)
        continue

    # A
    print(f"{zahl_1} {operator} {zahl_2} = {ergebnis}")

    if input("Weiter/Ende?").lower() == "ende":
        break

print("Auf Wiedersehen")
