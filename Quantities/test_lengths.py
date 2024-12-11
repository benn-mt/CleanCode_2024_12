from lengths import Lengths

def test_examples_from_exercise_with_s_method():
    assert Lengths.INCH.s(12) == Lengths.FOOT.s(1)
    assert Lengths.FOOT.s(3) == Lengths.YARD.s(1)
    assert Lengths.YARD.s(220) == Lengths.FURLONG.s(1)
    assert Lengths.FURLONG.s(8) == Lengths.MILE.s(1)