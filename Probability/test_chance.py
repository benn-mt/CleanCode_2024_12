from chance import Chance

CERTAIN = Chance(1)
IMPOSSIBLE = Chance(0)
FIFTY_FIFTY = Chance(0.5)

def test_chances_are_equal_if_created_with_equal_likelihoods():
    assert Chance(1) == Chance(1)
    assert Chance(1) != Chance(0)

def test_not_is_inverse_of_probablility():
    assert FIFTY_FIFTY == FIFTY_FIFTY.not_()
    assert CERTAIN == IMPOSSIBLE.not_()
    assert IMPOSSIBLE == IMPOSSIBLE.not_().not_()
    assert Chance(0.4).not_() == Chance(0.6)
    assert Chance(1.0 / 3.0).not_() == Chance(2.0 / 3.0)

def test_can_be_combined():
    assert CERTAIN.and_(CERTAIN) == CERTAIN
    assert CERTAIN.and_(IMPOSSIBLE) == IMPOSSIBLE
    assert CERTAIN.and_(FIFTY_FIFTY) == FIFTY_FIFTY
    assert FIFTY_FIFTY.and_(FIFTY_FIFTY) == Chance(0.25)

