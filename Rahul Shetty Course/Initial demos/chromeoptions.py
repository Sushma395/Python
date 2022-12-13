import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# used to add any options via arguments
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
# refer https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
print(driver.title)
driver.close()