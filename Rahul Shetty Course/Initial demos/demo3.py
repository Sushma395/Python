import time

from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

# auto suggestive drop downs
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
# select on india & inspect elements, all 3 countries with ind can be viewed in elements
# better to find elements with name instead of index, as index can be changes
# find elements can be used. If element is used, only first one from top left is picked
# find elements can be used to pick all
# custom css selector used
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
for country in countries:
    if country.text == 'India':
        country.click()
        break

# Get attribute of values to validate dynamic texts on the browser
# will not work as particular country not be prefilled when website is built
# Family and Friends etc can be returned with below line
# print(driver.find_element(By.ID,"autosuggest").text)
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == 'India'

# checkbox
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# (//input[@type='checkbox'])[2] can be used as custom xpath to pick Option2

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == 'option2':
        checkbox.click()
        # to check if check box is selected
        assert checkbox.is_selected()
        break

# radio button
# xpath can be used
time.sleep(2)
radios = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
# select 3rd radio button
radios[2].click()
time.sleep(1)
assert radios[2].is_selected()


driver.quit()
