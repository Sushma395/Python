from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://the-internet.herokuapp.com/frames')

# check for iframe tag if not known of frames in web page
# iFrame
driver.find_element(By.CSS_SELECTOR, "a[href='/iframe']").click()
driver.switch_to.frame("mce_0_ifr")  # frame id
driver.find_element(By.TAG_NAME, 'p').clear()
driver.find_element(By.TAG_NAME, 'p').send_keys('Automating Frame')

# switch back to default
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, 'h3').text)

driver.back()

# Nested Frames
driver.find_element(By.CSS_SELECTOR, "a[href='/nested_frames']").click()
driver.switch_to.frame("frame-top")  # frame name
driver.switch_to.frame("frame-left")
print(driver.find_element(By.TAG_NAME, "body").text)
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-right")
print(driver.find_element(By.TAG_NAME, "body").text)
driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
print(driver.find_element(By.TAG_NAME, "body").text)
driver.back()
print(driver.title)
driver.quit()




