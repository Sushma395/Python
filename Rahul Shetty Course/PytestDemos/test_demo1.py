import pytest


def test_firstProgram():
    print('First Output')


@pytest.mark.smoke
def test_secondProgram():
    msg = 'Second Ouput'
    assert msg == 'Second Output', "Test Failed as strings doesn't match"

