# Eine kleine Übung  mit 3 Klassen
#
# Klasse 1: Kunde
# Klasse 2: Konto
# Klasse 3: Bank
#
# Bank verwaltet Kunden und Konten
#
class Bank:
    def __init__(self):
        self._kunden = []

    def add_kunde(self, kunde):
        self._kunden.append(kunde)

    def einzahlen(self, name, betrag):
        for kunde in self._kunden:
            if name in kunde.info():
                kunde.einzahlen(betrag)

    def kunden_report(self):
        for kunde in self._kunden:
            print(kunde.info())

class Kunde:
    def __init__(self, name, konto):
        self._name = name
        self._konto = konto

    def einzahlen(self, betrag):
        self._konto.einzahlen(betrag)
        return self

    def info(self):
        return self._name, self._konto.saldo()

class Konto:
    def __init__(self, init = 0.0, dispo = 0.0):
        self._dispo = dispo # In der Realität: Decimal!!!
        self._stand = init # hier auch!

    def einzahlen(self, valuta):
        self._stand += valuta
        return self._stand

    def saldo(self):
        return self._stand

if __name__ == "__main__":
    bank = Bank()
    bank.add_kunde(Kunde("Willi", Konto()))
    bank.add_kunde(Kunde("Heinz", Konto()))

    bank.einzahlen("Willi", 10000)

    bank.kunden_report()
