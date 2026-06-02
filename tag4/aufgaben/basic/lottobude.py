# Lottobude:
#
# E: Valide Zahlen 6 aus 1-49, keine Doppelten
# V: Berechnung der Ziehung
#    Ergebnis <- Vergleich mit den eingegeben Zahlen aka Tipp
# A: Tipp - Ziehung- Ergebnis
#
#
# Mit Hilfe von Funktionen für:
# Validierung der Eingabe
# Ziehung der Zahlen
# Auswertung des Spielsergebnisses
# Ausgbabe für den Benutzer
import random

def erzeuge_tipp(zahlen):
    """ Prüft auf Korrektheit - wirft Exception wenn nicht korrekt -gibt liste mit TIpp zurück
    """

    if len(zahlen) != 6:
        raise ValueError("Keine 6 Zahlen")
    tipp = []
    for zahl in zahlen:
        zahl = int(zahl)
        if zahl in tipp:
            raise ValueError("Doppelter Wert")
        if zahl < 1 or zahl > 49:
            raise ValueError("Ungültiger Wert")
        tipp.append(zahl)
    return tipp


def get_input(trenner=","):
    return input(f"Ihr Tipp, Trennzeichen {trenner}: ").split(trenner)

def get_ziehung():
    return random.sample(range(1,50), 6)

def werte_aus(tipp,ziehung):
    return set(tipp).intersection(set(ziehung))

def _to_str(values): # Per Konvention "versteckt"/privat
    rvalue = []
    for x in values:
        rvalue.append(str(x))
    return rvalue

def report(tipp, ziehung, ergebnis):
    print("SPIEL LOTTO 6 aus 49")
    print("="*40)
    print("Tipp:    ", ",".join(_to_str(tipp)))
    print("Ziehung :", ",".join(_to_str(ziehung)))
    print("Ergebnis:", ",".join(_to_str(ergebnis)))
    print("Treffer: ", len(ergebnis))


if __name__ == "__main__":
    eingabe = get_input()
    tipp = erzeuge_tipp(eingabe)
    anzahl_spiele = int(input("Anzahl Spiele: "))
    for _ in range(anzahl_spiele): # _ heisst hier muss zwar was stehen, aber es interessiert mich nicht
        ziehung = get_ziehung()
        ergebnis = werte_aus(tipp,ziehung)
        report(tipp, ziehung, ergebnis)
