class Quantity:
    def __init__(self, amount, unit):
        self._amount = amount
        self._unit = unit

    # override == operator
    def __eq__(self, other):
        return self._amount == other._amount and self._unit == other._unit