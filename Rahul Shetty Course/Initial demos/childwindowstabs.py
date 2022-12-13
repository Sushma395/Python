from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://the-internet.herokuapp.com/windows')
# driver.find_element(By.XPATH, "//a[@href='/windows/new']").click()
# link_text can be used as it has anchor a tag ex: <a
driver.find_element(By.LINK_TEXT, "Click Here").click()
# switch to window
print(driver.title)
opened_windows = driver.window_handles # will be stored in list
driver.switch_to.window(opened_windows[1])
print(driver.title)
assert driver.find_element(By.TAG_NAME, 'h3').text == 'New Window'
driver.switch_to.window(opened_windows[0]) # parent window
print(driver.title)
driver.close()  # parent window closes, as control is in parent window
driver.quit()


