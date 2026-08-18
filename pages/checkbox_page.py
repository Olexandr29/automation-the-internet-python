from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckboxPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.locators = {
            # "checkboxes": (By.ID, "checkboxes")
            "checkboxes": (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
        }

    def is_checkbox_visible(self, checkbox_number):
        checkboxes = self.driver.find_elements(*self.locators["checkboxes"])
        if checkbox_number > len(checkboxes):
            return False
    
        return checkboxes[checkbox_number - 1].is_displayed()