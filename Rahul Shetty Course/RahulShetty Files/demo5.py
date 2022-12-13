# chromeoptions, screenshot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chromeoptions
chrome_options = webdriver.ChromeOptions()
# to run in headless mode
chrome_options.add_argument("headless")
# to ignore cert errors like page not secure
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
# pass argument
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# screenshot
driver.get_screenshot_as_file('demo5.png')

driver.close()