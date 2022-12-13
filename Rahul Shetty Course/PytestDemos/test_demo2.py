import pytest


@pytest.mark.smoke
def test_equalProgram():
    a = 10
    b = 10
    assert a == b, "variables doesn't match"


def test_addProgram():
    c = 100
    d = 120
    print(c+d)


@pytest.mark.skip
def test_subtractProgram():
    a = 200
    b = 120
    print(a-b)


@pytest.mark.xfail
def test_xfailProgram():
    assert 1 == 2, "Test Failed"

