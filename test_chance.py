from chance import Chance

def test_chances_are_equal_if_created_with_equal_likelihoods():
    assert Chance(1) == Chance(1)
    assert not Chance(1) == Chance(0)