import random

class Spiel:
    def __init__(self):
        self._spiel = random.sample(range(1,50), 6)

    def get_values(self):
        return self._spiel
