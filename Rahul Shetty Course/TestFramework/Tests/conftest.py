import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="class")
# request is an instance for fixture
# need to tie up this instance to class instance
# use request.cls.driver
def setup(request):
    service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    # assigning local driver of this fixture to class driver
    yield
    driver.close()

