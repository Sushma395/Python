import pytest


# @pytest.fixture() --> when class isn't used
@pytest.fixture(scope="class")
def setup():
    print('First step to be executed')
    yield
    # teardown
    print('Last step to be executed')


@pytest.fixture()
def dataLoad():
    print('User profile is being created')
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


# parametrization
# request is an instance that belongs to fixture
@pytest.fixture(params=[("chrome", "rahul", "Shetty"), ("Firefox", "Rahul"), "IE"])
def crossBrowser(request):
    # param in params will be sent ex: chrome will be sent first
    return request.param
