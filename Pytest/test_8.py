import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None
@pytest.fixture
def setup():
    print("start browser")
    global driver
    service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\PytestProject\\venv\\Scripts\\chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    yield
    driver.quit()
    print("close browser")


def test_1(setup):
    driver.get("http://facebook.com")
    print("test 1 executed")

def test_2(setup):
    driver.get("http://google.com")
    print("test 2 executed")

def test_3(setup):
    driver.get("http://bing.com")
    print("test 3 executed")
