import time

from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

# find by element
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Sushi")
# link_text can be used for elemensts having a tag. Ex: <a href= "/windows/new" <Click Here</a>
# Click Here can be used as link text
# ID is most common
driver.find_element(By.ID, "exampleInputPassword1").send_keys("hello123")
# custom xpath  //tagname[@name=’xxx’]
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Bandaru")
# custom cssselector  tagname[name=’xxx’]
driver.find_element(By.CSS_SELECTOR, "input[name='email']").clear()
checkbox = driver.find_element(By.XPATH,"//input[@id='exampleCheck1']")
checkbox.click()
assert checkbox.is_selected()
# custom xpath with text //tagname[text()=’xxx’]
checkbox_text = driver.find_element(By.XPATH,"//label[text()='Check me out if you Love IceCreams!']").text
assert checkbox_text == 'Check me out if you Love IceCreams!'

# drop down
# select tagname means, it's static.
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(1)
dropdown.select_by_index("0")

# radio button
driver.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()
assert not driver.find_element(By.XPATH,"//input[@id='inlineRadio3']").is_enabled()
dob = driver.find_element(By.NAME,"bday")
dob.send_keys('2022-01-01')
dob.clear()
dob.send_keys('11-01-2022')

# button
driver.find_element(By.CLASS_NAME,"btn").click()
success = driver.find_element(By.CLASS_NAME,"alert")
if "Success!" in success.text:
    print("Submission successful")
driver.find_element(By.LINK_TEXT,"×").click()
driver.quit()

