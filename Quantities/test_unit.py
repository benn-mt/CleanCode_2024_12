from unit import Unit

myBaseUnit = Unit()
myNextUnit = Unit(2,myBaseUnit)
myThirdUnit = Unit(3, myNextUnit)

def test_can_calculate_amount_in_base_unit():
    assert myBaseUnit.amountInBaseUnit(5) == 5
    assert myNextUnit.amountInBaseUnit(1) == 2
    assert myNextUnit.amountInBaseUnit(2) == 4

def test_can_calculate_amount_in_relative_unit():
    assert myBaseUnit.amountInUnit(1, myBaseUnit) == 1
    assert myBaseUnit.amountInUnit(2, myNextUnit) == 1
    assert myBaseUnit.amountInUnit(4, myNextUnit) == 2
    assert myNextUnit.amountInUnit(3, myBaseUnit) == 6
    assert myThirdUnit.amountInUnit(1, myBaseUnit) == 6
    assert myThirdUnit.amountInUnit(1, myNextUnit) == 3