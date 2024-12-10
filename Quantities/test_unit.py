from volumes import Volumes

def test_can_calculate_amount_in_base_unit():
    assert Volumes.TEASPOON.amountInBaseUnit(5) == 5
    assert Volumes.TABLESPOON.amountInBaseUnit(1) == 3
