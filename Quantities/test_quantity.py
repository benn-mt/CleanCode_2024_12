from quantity import Quantity
from unit import Unit

def test_quantities_of_same_unit_and_amount_are_equal():
    assert Quantity(1, Unit.TEASPOON) == Quantity(1, Unit.TEASPOON) 
    assert Quantity(2, Unit.TEASPOON) != Quantity(1, Unit.TEASPOON) 
    assert Quantity(3, Unit.TEASPOON) != Quantity(5, Unit.TEASPOON) 
    assert Quantity(4, Unit.TABLESPOON) != Quantity(4, Unit.TEASPOON)
    assert Quantity(4, Unit.TEASPOON) != Quantity(4, Unit.TABLESPOON) 
