from unit import Unit

class Volumes: 
    TEASPOON = Unit()
    TABLESPOON = Unit(3, TEASPOON)
    OUNCE = Unit(2, TABLESPOON)
    CUP = Unit(8, OUNCE)
    PINT = Unit(2, CUP)
    QUART = Unit(2, PINT)
    GALLON = Unit(4, QUART)