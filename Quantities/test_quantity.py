from quantity import Quantity
from volumes import Volumes

def test_quantities_of_same_unit_and_amount_are_equal():
    assert Quantity(1, Volumes.TEASPOON) == Quantity(1, Volumes.TEASPOON) 
    assert Quantity(2, Volumes.TEASPOON) != Quantity(1, Volumes.TEASPOON) 
    assert Quantity(3, Volumes.TEASPOON) != Quantity(5, Volumes.TEASPOON) 
    assert Quantity(4, Volumes.TABLESPOON) != Quantity(4, Volumes.TEASPOON)
    assert Quantity(4, Volumes.TEASPOON) != Quantity(4, Volumes.TABLESPOON) 

def test_quantities_with_same_base_unit_amount_are_equal():
    assert Quantity(3, Volumes.TEASPOON) == Quantity(1, Volumes.TABLESPOON) 
    assert Quantity(1, Volumes.TABLESPOON) == Quantity(3, Volumes.TEASPOON) 

def test_example_from_exercise():
    assert Quantity(1, Volumes.TABLESPOON) == Quantity(3, Volumes.TEASPOON)
    assert Quantity(1, Volumes.OUNCE) == Quantity(2, Volumes.TABLESPOON)
    assert Quantity(1, Volumes.CUP) == Quantity(8, Volumes.OUNCE)
    assert Quantity(1, Volumes.PINT) == Quantity(2, Volumes.CUP)
    assert Quantity(1, Volumes.QUART) == Quantity(2, Volumes.PINT)
    assert Quantity(1, Volumes.GALLON) == Quantity(4, Volumes.QUART)

def test_examples_from_exercise_with_s_method():
    assert Volumes.TABLESPOON.s(1) == Volumes.TEASPOON.s(3)
    assert Volumes.OUNCE.s(1) == Volumes.TABLESPOON.s(2)
    assert Volumes.CUP.s(1) == Volumes.OUNCE.s(8)
    assert Volumes.PINT.s(1) == Volumes.CUP.s(2)
    assert Volumes.QUART.s(1) == Volumes.PINT.s(2)
    assert Volumes.GALLON.s(1) == Volumes.QUART.s(4)