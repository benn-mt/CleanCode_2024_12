from quantity import Quantity

class Unit:
    def __init__(self, ratioToRelativeUnit = 1, relativeUnit = None):
        self._ratioToBaseUnit = ratioToRelativeUnit
        self._baseUnit = self
        if (relativeUnit):
            self._ratioToBaseUnit = self._ratioToBaseUnit * relativeUnit._ratioToBaseUnit
            self._baseUnit = relativeUnit._baseUnit

    def amountInBaseUnit(self, amountInThisUnit):
        return amountInThisUnit * self._ratioToBaseUnit
    
    def amountInUnit(self, amountInThisUnit, otherUnit):
        return amountInThisUnit / otherUnit._ratioToBaseUnit * self._ratioToBaseUnit
    
    def isCompatibleWith(self, other):
        return self._baseUnit == other._baseUnit
    
    def s(self, amount):
        return Quantity(amount, self)