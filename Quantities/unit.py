from quantity import Quantity

class Unit:
    def __init__(self, ratioToRelativeUnit = 1, relativeUnit = None):
        self._ratioToBaseUnit = ratioToRelativeUnit
        if (relativeUnit):
            self._ratioToBaseUnit = self._ratioToBaseUnit * relativeUnit._ratioToBaseUnit

    def amountInBaseUnit(self, amountInThisUnit):
        return amountInThisUnit * self._ratioToBaseUnit
    
    def s(self, amount):
        return Quantity(amount, self)