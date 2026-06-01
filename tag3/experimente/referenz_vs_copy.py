# KO durch Referenzen und ihre Effekte
adressen = [
             ["Willi", "Watz", "Watzplatz 1", "12345", "Watzingen"]
           ]


adr_1 = adressen[0]
adr_1[2] = "Watzplatz 2"
adressen.append(adr_1)

# Für diesen speziellen Fall eine gute Lösung
adressen = [
             ["Willi", "Watz", "Watzplatz 1", "12345", "Watzingen"]
           ]


adr_1 = adressen[0].copy() # Es ist eine "flache Kopie", d.h. wenn Listen in der Liste sind werden die nicht gedoppelt
adr_1[2] = "Watzplatz 2"
adressen.append(adr_1)
