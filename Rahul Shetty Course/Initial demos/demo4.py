import time

from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# text box show/hide
assert driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(1)
# click on hide
driver.find_element(By.ID, "hide-textbox").click()
# text box will not be displayed now
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

name = 'Raman'
# Alert popups using javascript
# popups will be written in javascript, so html can't be used to do operations on popups
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
time.sleep(1)
print(alert.text)
assert name in alert.text
alert.accept()
#alert.dismiss()

driver.quit()