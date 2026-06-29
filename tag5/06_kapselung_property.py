# Tag 5 – Kapselung & @property
#
# Kapselung = das Innenleben eines Objekts schützen und nur über klare Wege
# ändern lassen. Python kennt KEINE echten "private" Attribute wie Java –
# es arbeitet mit Konventionen und einem kleinen Trick.

# --- Konvention: ein Unterstrich = "bitte von außen nicht anfassen" ---
class Konto:
    def __init__(self, inhaber, stand=0.0):
        self.inhaber = inhaber
        self._stand = stand        # _stand: "intern", nur ein höflicher Hinweis

    def einzahlen(self, betrag):
        if betrag <= 0:
            raise ValueError("Betrag muss positiv sein")
        self._stand += betrag

    def stand(self):
        return self._stand

k = Konto("Anna")
k.einzahlen(50.0)
print(k.stand())                   # 50.0
# k._stand = -999  ginge technisch trotzdem – der _ sagt nur "lass es".

# --- Name-Mangling: zwei Unterstriche erschweren den Zugriff ---
class Tresor:
    def __init__(self, pin):
        self.__pin = pin           # wird intern zu _Tresor__pin umbenannt

    def pruefe(self, eingabe):
        return eingabe == self.__pin

t = Tresor("1234")
print(t.pruefe("1234"))            # True
# print(t.__pin)                   # -> AttributeError
print(t._Tresor__pin)             # 1234   (geht doch – also kein echter Schutz,
                                   #          eher Schutz vor VERSEHENTLICHEM Zugriff)

# --- @property: Methode mit Attribut-Syntax ---
# Manchmal will man wie auf ein Attribut zugreifen (obj.x), aber im Hintergrund
# soll Code laufen (Berechnung oder Prüfung). Genau dafür ist @property da.
class Kreis:
    def __init__(self, radius):
        self.radius = radius

    @property
    def flaeche(self):
        # Aufruf OHNE Klammern: k.flaeche, nicht k.flaeche()
        return round(3.14159 * self.radius ** 2, 2)

kr = Kreis(2)
print(kr.flaeche)                  # 12.57   (wie ein Attribut, aber berechnet)
kr.radius = 3
print(kr.flaeche)                  # 28.27   (rechnet bei jedem Zugriff neu)

# --- Getter UND Setter: Wert beim Setzen prüfen ---
class Temperatur:
    def __init__(self, celsius=0.0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, wert):
        if wert < -273.15:
            raise ValueError("Unter dem absoluten Nullpunkt!")
        self._celsius = wert

    @property
    def fahrenheit(self):
        return round(self._celsius * 9 / 5 + 32, 1)

temp = Temperatur(20)
print(temp.celsius)                # 20      (Getter)
temp.celsius = 25                  # Setter (mit Prüfung)
print(temp.fahrenheit)             # 77.0    (abgeleiteter, nur lesbarer Wert)
# temp.celsius = -300              # -> ValueError

# Merke: @property hält die einfache obj.x-Schreibweise, lässt aber bei Bedarf
# Logik dahinter laufen. Nicht jedes Attribut braucht das – nur dort einsetzen,
# wo Berechnung oder Validierung wirklich sinnvoll ist.
