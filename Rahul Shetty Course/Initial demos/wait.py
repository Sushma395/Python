# explicit & implicit waits with greenkart application
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
# css selector with class name -> .class_name
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys('ber')
time.sleep(2)
expected_results = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
results = driver.find_elements(By.CSS_SELECTOR, "h4[class='product-name']")
# print(len(results))
observed_results = []
for result in results:
    observed_results.append(result.text)
# print(observed_results)
assert expected_results == observed_results

# adding to cart
products = driver.find_elements(By.CSS_SELECTOR, "div[class='product-action'] button")
for product in products:
    product.click()

# checkout
driver.find_element(By.CSS_SELECTOR, 'a[class="cart-icon"] img').click()
# driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# wait till textbox is available on screen
code = 'rahulshettyacademy'
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(code)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
if code == 'rahulshettyacademy':
    assert driver.find_element(By.XPATH, "//span[text()='Code applied ..!']").is_displayed()

# discount calculation & validation
total = driver.find_elements(By.CSS_SELECTOR,'tr td:nth-child(5) p')  # traverse to child using css
# total = driver.find_elements(By.XPATH, "//tbody/tr/td[5]")
s = 0  # sum
for i in total:
    s += float(i.text)
total_amount = float(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert s == total_amount
discount = float(driver.find_element(By.CSS_SELECTOR, ".discountPerc").text.replace('%',''))
total_after_discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
# print(total_amount * (discount/100))
assert (total_amount - (total_amount * (discount/100)) == total_after_discount)

# place order
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
driver.find_element(By.XPATH, "//select").click()
driver.find_element(By.XPATH, "//option[text()='India']").click()
driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
assert driver.find_element(By.CSS_SELECTOR, ".chkAgree").is_selected()
driver.find_element(By.CSS_SELECTOR, "button").click()
order_placed = driver.find_element(By.CSS_SELECTOR, ".wrapperTwo").text
assert 'Thank you' in order_placed

# redirect to home
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.title_is('GreenKart - veg and fruits kart'))
assert driver.title == 'GreenKart - veg and fruits kart'
driver.quit()
