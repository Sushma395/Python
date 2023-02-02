import pytest

@pytest.mark.smoke
def test_login():
    print("Login done")

@pytest.mark.regression
@pytest.mark.smoke
def test_addpayment():
    print("Payment added")

@pytest.mark.smoke
def test_logout():
    print("Logout done")