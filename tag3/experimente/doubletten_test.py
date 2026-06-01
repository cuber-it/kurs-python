eingabe = input("Zahlen Werte: keine doubletten").split(" ")
werte = []
for wert in eingabe:
    werte.append(int(wert))

print("Werteliste: ", werte)

if len(set(werte)) != len(werte): # set lässt als Menge keine Doppelten zu und filtert sie raus
    print("Es gab Doubletten")
else:
    print("Eingabe ist ok")
