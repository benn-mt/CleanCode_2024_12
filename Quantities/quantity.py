class Quantity:
    def __init__(self, amount, unit):
        self._amount = amount
        self._unit = unit

    # override == operator
    def __eq__(self, other):
        return self._unit.isCompatibleWith(other._unit) and self._amount == other._unit.amountInUnit(other._amount, self._unit)
    
    def __add__(self, other):
        return self.add(other)
    
    def add(self, other):
        if (not self._unit.isCompatibleWith(other._unit)):
            raise Exception("Incompatible Units")
        return Quantity(self._amount + other._unit.amountInUnit(other._amount, self._unit), self._unit)