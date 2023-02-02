# marker parametrize
# data should be passed as list of tuples
import pytest


@pytest.mark.parametrize("username,password",
                         [("Selenium","Webdriver"),("Python","Pytest"),("Suren","Bhanu")])
def test_login(username,password):
    print(username)
    print(password)


