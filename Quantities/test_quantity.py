import pytest
from quantity import Quantity
from volumes import Volumes
from lengths import Lengths

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

def test_measurements_with_same_unit_can_be_added_together():
    assert Quantity(1, Volumes.TEASPOON).add(Quantity(0, Volumes.TEASPOON)) == Quantity(1, Volumes.TEASPOON)
    assert Quantity(1, Volumes.TEASPOON) + (Quantity(0, Volumes.TEASPOON)) == Quantity(1, Volumes.TEASPOON)
    assert Quantity(1, Volumes.TEASPOON) + (Quantity(1, Volumes.TEASPOON)) == Quantity(2, Volumes.TEASPOON)
    assert Quantity(3, Volumes.TABLESPOON) + (Quantity(2, Volumes.TABLESPOON)) == Quantity(5, Volumes.TABLESPOON)

def test_measurements_with_different_unit_can_be_added_together():
    assert Quantity(1, Volumes.TEASPOON).add(Quantity(0, Volumes.TABLESPOON)) == Quantity(1, Volumes.TEASPOON)
    assert Quantity(1, Volumes.TEASPOON).add(Quantity(1, Volumes.TABLESPOON)) == Quantity(4, Volumes.TEASPOON)

def test_measurements_with_incompatible_units_can_not_be_added_together():
    with pytest.raises(Exception) as e_info:
        Quantity(1, Volumes.TEASPOON).add(Quantity(1, Volumes.INCH))

def test_measurements_with_incompatible_units_are_not_equal():
    assert Quantity(1, Volumes.TEASPOON) != Quantity(1, Lengths.INCH)