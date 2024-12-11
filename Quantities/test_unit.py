from unit import Unit

myBaseUnit = Unit()
myNextUnit = Unit(2,myBaseUnit)

def test_can_calculate_amount_in_base_unit():
    assert myBaseUnit.amountInBaseUnit(5) == 5
    assert myNextUnit.amountInBaseUnit(1) == 2
    assert myNextUnit.amountInBaseUnit(2) == 4
