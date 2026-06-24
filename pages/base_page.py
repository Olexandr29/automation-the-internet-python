from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find(locator)
        element.click()
        return element
    
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find(locator)
        return element.text
    
    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False
                