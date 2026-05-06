# Aufgabe: Jahr einlesen, einen Boolean ausgeben, der angibt, ob es ein Schaltjahr ist — ohne if.
#  Regel: durch 4 teilbar und nicht durch 100, oder durch 400 teilbar.

# E
jahr = input("Jahr: ")

# V
jahr = int(jahr)

# A
ist_schaltjahr = (jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0
print(f"Ist Schaltjahr: {jahr} {ist_schaltjahr}")
