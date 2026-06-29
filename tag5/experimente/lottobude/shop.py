import tag5.experimente.lottobude.ausgabe as ausgabe
import tag5.experimente.lottobude.eingabe as eingabe
import tag5.experimente.lottobude.ziehung as ziehung
import tag5.experimente.lottobude.tippschein as tippschein


class Shop:
    def __init__(self, quelle, ziel):
        self._quelle = quelle
        self._ziel = ziel
        self._ergebnis = None
        self._ziehung = None
        self._tipp = None

    def _auswertung(self):
        t = set(self._tipp.get_tipp())
        z = set(self._ziehung.get_values())
        self._ergebnis = list(t.intersection(z))

    def tippschein_abgeben(self):
        self._tipp = tippschein.Tipp(self._quelle) # Check
        return self

    def ziehung(self):
        self._ziehung = ziehung.Spiel() # Check
        self._auswertung()
        return self

    def ergebnis_ausgeben(self):
        self._ziel.report(self._ergebnis) # Check
        return self

if __name__ == "__main__":
    s = Shop(eingabe.Tastatur(), ausgabe.DB())
    s.tippschein_abgeben().ziehung().ergebnis_ausgeben() # Method chaining
