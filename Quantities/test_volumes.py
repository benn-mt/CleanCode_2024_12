from volumes import Volumes

def test_examples_from_exercise_with_s_method():
    assert Volumes.TABLESPOON.s(1) == Volumes.TEASPOON.s(3)
    assert Volumes.OUNCE.s(1) == Volumes.TABLESPOON.s(2)
    assert Volumes.CUP.s(1) == Volumes.OUNCE.s(8)
    assert Volumes.PINT.s(1) == Volumes.CUP.s(2)
    assert Volumes.QUART.s(1) == Volumes.PINT.s(2)
    assert Volumes.GALLON.s(1) == Volumes.QUART.s(4)

def test_random_examples():
    assert Volumes.TABLESPOON.s(2) == Volumes.TEASPOON.s(6)
    assert Volumes.TABLESPOON.s(0.5) == Volumes.TEASPOON.s(1.5)
    assert Volumes.GALLON.s(1) == Volumes.TEASPOON.s(4*2*2*8*2*3)