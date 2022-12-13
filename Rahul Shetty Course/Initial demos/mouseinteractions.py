import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# ActionChains class
action = ActionChains(driver)
# for mouse hover
# perform is needed so that sequence of actions is executed
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.click(driver.find_element(By.LINK_TEXT, 'Top')).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, 'Top')).perform()
# for right click action.context_click()
# for double click action.double_click()
# for long press action.click_and_hold()
# for drag and drop action.drag_and_drop()

driver.get('https://demoqa.com/droppable')
time.sleep(1)
action.drag_and_drop(driver.find_element(By.ID, "draggable"), driver.find_element(By.ID, "droppable"))
