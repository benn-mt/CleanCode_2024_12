from unit import Unit

myBaseUnit = Unit()
myNextUnit = Unit(2,myBaseUnit)
myThirdUnit = Unit(3, myNextUnit)

myOtherBaseUnit = Unit()

def test_can_calculate_amount_in_relative_unit():
    assert myBaseUnit.amountInUnit(1, myBaseUnit) == 1
    assert myBaseUnit.amountInUnit(2, myNextUnit) == 1
    assert myBaseUnit.amountInUnit(4, myNextUnit) == 2
    assert myNextUnit.amountInUnit(3, myBaseUnit) == 6
    assert myThirdUnit.amountInUnit(1, myBaseUnit) == 6
    assert myThirdUnit.amountInUnit(1, myNextUnit) == 3

def test_units_with_same_base_unit_are_compatible():
    assert myBaseUnit.isCompatibleWith(myBaseUnit) == True
    assert myNextUnit.isCompatibleWith(myBaseUnit) == True
    assert myThirdUnit.isCompatibleWith(myBaseUnit) == True
    assert myNextUnit.isCompatibleWith(myThirdUnit) == True

def test_units_of_different_scales_are_not_compatible():
    assert myBaseUnit.isCompatibleWith(myOtherBaseUnit) == False
    assert myOtherBaseUnit.isCompatibleWith(myBaseUnit) == False
    assert myThirdUnit.isCompatibleWith(myOtherBaseUnit) == False
    assert myOtherBaseUnit.isCompatibleWith(myThirdUnit) == False