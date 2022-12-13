from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(4)
driver.maximize_window()

driver.get(r"https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME, "blinkingText").click()
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])

sentance = driver.find_element(By.XPATH,"//div/p[2]").text
email = sentance.split("at")[1].strip().split(" ")[0]
driver.close()

driver.switch_to.window(windowOpened[0])

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID,"password").send_keys(email)
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']")))

print(driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text)
driver.close()