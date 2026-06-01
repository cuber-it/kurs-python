keys = [ "Name", "Vorname", "Strasse", "PLZ", "Ort" ]
values = ["Watz", "Willi", "Watzplatz 1", "1234", "Watzingen" ]

key = "PLZ"
plz = values[keys.index(key)]


print(plz)
#------------------------------------------------

addr = { "Name":"Watz", "Vorname":"Willi", "Strasse":"Watzplatz 1", "PLZ":"12345", "Ort":"Watzingen"}
print(addr.keys())
print(addr.values())
print(addr.items())

key = "PLZ"
plz = addr[key]

print(plz)

#-- ein Trick um dict aus Lsiten  wie oben zu erzeugen:
itemslist = list(zip(keys, values))
print(itemslist)

addr_2 = dict(itemslist)
print(addr_2)
