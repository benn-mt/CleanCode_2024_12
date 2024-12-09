class Chance:
    __CERTAIN_LIKELIHOOD = 1.0
    __THRESHOLD = 0.000001

    def __init__(self, likelihood):
        self._likelihood = likelihood

    # override == operator
    def __eq__(self, other):
        return abs(self._likelihood - other._likelihood) < self.__THRESHOLD

    def not_(self):
        return Chance(self.__CERTAIN_LIKELIHOOD - self._likelihood)