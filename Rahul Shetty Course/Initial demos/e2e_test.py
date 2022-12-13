from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(4)
# regular expressions, but not recommended, only in exceptional cases(preference to css here)
# can also use CSS --> a[href*='shop'] or a[href='/angularpractice/shop']
# can also use xpath --> //a[contains(@href*='shop')]
driver.find_element(By.LINK_TEXT, "Shop").click()
mobiles = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for mobile in mobiles:
    model = mobile.find_element(By.XPATH,"div/h4/a")
    if model.text == 'iphone X':
        mobile.find_element(By.XPATH,"div[@class='card-footer']").click()
        break

#click on checkout
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

#checkout
assert driver.find_element(By.XPATH, '//h4[@class="media-heading"]').text == 'iphone X'
driver.find_element(By.CLASS_NAME, "btn-success").click()

# auto suggestive dropdowns
driver.find_element(By.ID, 'country').send_keys('ind')
# explicit wait till India is located
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))  # locator in additional ()
driver.find_element(By.LINK_TEXT, "India").click()
#driver.find_element(By.XPATH, "//a[contains(text(),'India')]").click()

# checkbox
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
assert driver.find_element(By.ID, "checkbox2").is_selected()

# purchase
driver.find_element(By.CLASS_NAME, "btn-success").click()

# success
success_text = driver.find_element(By.CLASS_NAME, "alert").text
assert 'Success! Thank you!' in success_text

driver.quit()