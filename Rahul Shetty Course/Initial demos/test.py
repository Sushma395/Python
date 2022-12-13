from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service

# chrome chromedriver
# firefox geckodriver
# edge msedgedriver

# Hold the driver information & need to pass path of chrome driver
service_obj = Service("C:\\Users\\suba0816\\PycharmProjects\\SeleniumTestProject\\venv\\Scripts\\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.current_url) # this is a property, so () is not needed)
print(driver.title)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
print(driver.title)
driver.refresh()
driver.forward()
print(driver.title)
driver.close()
