werte = []

while True:
    eingabe = input("Eingabe - keine doppelte erlaubt/exit beendet: ")
    if eingabe == 'exit':
        break

    if eingabe in werte:
        print("Doppelt: ", eingabe)
    else:
        werte.append(eingabe)

print(" ".join(werte))
