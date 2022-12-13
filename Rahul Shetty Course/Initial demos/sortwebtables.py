import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[href='#/offers']").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggies = driver.find_elements(By.XPATH, "//tr/td[1]")
# names = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
browser_sorted_veggies = []
for veggy in veggies:
    print(veggy.text)
    browser_sorted_veggies.append(veggy.text)

original_sorted_veggies = browser_sorted_veggies.copy()

browser_sorted_veggies.sort()

assert browser_sorted_veggies == original_sorted_veggies

driver.quit()