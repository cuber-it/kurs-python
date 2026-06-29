class Tipp:
    def __init__(self, quelle):
        self._quelle = quelle

    def get_tipp(self):
        return self._quelle.input()
