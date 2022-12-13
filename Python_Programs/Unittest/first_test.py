import pytest

import mathsush


def test_calc_addition():
    output = mathsush.calc_addition(2,4)
    assert output == 6

@pytest.mark.parametrize()
def test_calc_subtraction():
    output = mathsush.calc_subtraction(2, 4)
    assert output == -2


def test_calc_multiply():
    output = mathsush.calc_multiply(2,4)
    assert output == 8