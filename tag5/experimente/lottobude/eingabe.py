class Tastatur:
    def input(self):
        eingabe = input("Werte komma getrennnt: ").replace(" ", "").split(",")
        tipp = []
        for v in eingabe:
            tipp.append(int(v))
        return tipp
