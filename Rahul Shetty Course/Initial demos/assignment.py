from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# path having chrome driver to be given
service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, 'blinkingText').click()
opened_windows = driver.window_handles
driver.switch_to.window(opened_windows[1])
mail_id = driver.find_element(By.CSS_SELECTOR, "a[href='mailto:mentor@rahulshettyacademy.com']").text
driver.switch_to.window(opened_windows[0])
driver.find_element(By.ID, 'username').send_keys(mail_id)
driver.find_element(By.ID, 'password').send_keys('sushi')
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.ID, "signInBtn").click()
# to grab hidden elements with display='None' using javascript executor
# get_text = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
# driver.execute_script("arguments[0].style.display='block';", get_text)
# print(get_text.text)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
driver.quit()
