import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Login done")

@pytest.mark.skipif(sys.version_info<(3,10), reason="Python verison not supported")
def test_addpayment():
    print("Payment added")

@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout done")

def test_closeApplication():
    assert True
    print("closed application")