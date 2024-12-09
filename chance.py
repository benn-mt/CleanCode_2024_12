class Chance:
    __CERTAIN_LIKELIHOOD = 1.0

    def __init__(self, likelihood):
        self._likelihood = likelihood

    # override == operator
    def __eq__(self, other):
        return self._likelihood == other._likelihood

    def Not(self):
        return Chance(self.__CERTAIN_LIKELIHOOD - self._likelihood)