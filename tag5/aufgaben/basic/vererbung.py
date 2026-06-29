# Tag 5 – shapes.py  (Vererbungs-Showcase, lauffähig)
#
# Hierarchie (zweistufig):
#
#     Shape
#     ├─ Rectangle
#     ├─ Triangle
#     └─ Ellipse
#        └─ Circle          (ein Kreis IST EINE Ellipse mit a == b)
#
# Zeigt auf einmal: Vererbung, super(), Polymorphie und überschreiben vs. erben.

import math


class Shape:
    """Basisklasse: legt nur die SCHNITTSTELLE fest, rechnet selbst nichts.
    Wer flaeche()/umfang() nicht definiert, fliegt mit einem klaren Fehler auf."""

    def flaeche(self):
        raise NotImplementedError("Unterklasse muss flaeche() definieren")

    def umfang(self):
        raise NotImplementedError("Unterklasse muss umfang() definieren")

    def __str__(self):
        # type(self).__name__ liefert den Klassennamen des konkreten Objekts –
        # so funktioniert dieselbe Methode für alle Unterklassen (Polymorphie).
        return f"{type(self).__name__}: Flaeche={self.flaeche():.2f}, Umfang={self.umfang():.2f}"


class Rectangle(Shape):
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self):
        return self.breite * self.hoehe

    def umfang(self):
        return 2 * (self.breite + self.hoehe)


class Triangle(Shape):
    """Der Einfachheit halber ein rechtwinkliges Dreieck mit Katheten a und b."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def flaeche(self):
        return self.a * self.b / 2

    def umfang(self):
        hypotenuse = math.hypot(self.a, self.b)   # sqrt(a**2 + b**2)
        return self.a + self.b + hypotenuse


class Ellipse(Shape):
    def __init__(self, a, b):
        self.a = a          # grosse Halbachse
        self.b = b          # kleine Halbachse

    def flaeche(self):
        return math.pi * self.a * self.b

    def umfang(self):
        # Der exakte Ellipsenumfang braucht ein Integral – hier Ramanujans
        # sehr genaue Naeherung. (Genau das vereinfacht sich beim Kreis, s. u.)
        a, b = self.a, self.b
        h = ((a - b) / (a + b)) ** 2
        return math.pi * (a + b) * (1 + 3 * h / (10 + math.sqrt(4 - 3 * h)))


class Circle(Ellipse):
    """Ein Kreis IST EINE Ellipse mit a == b == radius."""

    def __init__(self, radius):
        super().__init__(radius, radius)   # beide Halbachsen = radius
        self.radius = radius

    # flaeche() wird von Ellipse GEERBT: pi * a * b -> pi * r * r  (korrekt!)

    def umfang(self):
        # umfang() wird ÜBERSCHRIEBEN: beim Kreis exakt 2*pi*r, keine Naeherung.
        return 2 * math.pi * self.radius


# ===========================================================================
# Selbsttest – nur bei direktem Start (python3 shapes.py)
# ===========================================================================
if __name__ == "__main__":
    formen = [
        Rectangle(4, 3),
        Triangle(3, 4),
        Ellipse(5, 3),
        Circle(2),
    ]

    # Polymorphie: dieselbe Schleife, jede Form rechnet auf ihre Art:
    for form in formen:
        print(form)

    print("-" * 40)

    # Vererbung sichtbar machen:
    c = Circle(2)
    print("Circle ist eine Ellipse?", isinstance(c, Ellipse))   # True
    print("Circle ist eine Shape?  ", isinstance(c, Shape))     # True
    print("Fläche (geerbt):        ", round(c.flaeche(), 4))    # 12.5664
    print("Umfang (überschrieben): ", round(c.umfang(), 4))     # 12.5664

    # NotImplementedError zeigen: eine nackte Shape kann nichts rechnen.
    try:
        Shape().flaeche()
    except NotImplementedError as e:
        print("Shape direkt:           ", e)
