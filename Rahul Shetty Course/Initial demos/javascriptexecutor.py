# javascript
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.implicitly_wait(2)
# print(driver.timeouts.page_load)
# got to console in inspect, to execute javascript or find javascript commands
time.sleep(1)
driver.execute_script('window.scrollTo(0,1500);')
print(driver.timeouts.implicit_wait)
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(1)
driver.execute_script('window.scrollTo(document.body.scrollHeight,0);')
time.sleep(1)
driver.execute_script('window.scrollBy(0,document.body.scrollHeight);')

driver.close()
