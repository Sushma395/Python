import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestOne:

    # to access setup
    def test_e2e(self, setup):

        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        mobiles = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for mobile in mobiles:
            model = mobile.find_element(By.XPATH, "div/h4/a")
            if model.text == 'iphone X':
                mobile.find_element(By.XPATH, "div[@class='card-footer']").click()
                break

        # click on checkout
        self.driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

        # checkout
        assert self.driver.find_element(By.XPATH, '//h4[@class="media-heading"]').text == 'iphone X'
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()

        # auto suggestive dropdowns
        self.driver.find_element(By.ID, 'country').send_keys('ind')
        # explicit wait till India is located
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))  # locator in additional ()
        self.driver.find_element(By.LINK_TEXT, "India").click()

        # checkbox
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        assert self.driver.find_element(By.ID, "checkbox2").is_selected()

        # purchase
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()

        # success
        success_text = self.driver.find_element(By.CLASS_NAME, "alert").text
        assert 'Success! Thank you!' in success_text


