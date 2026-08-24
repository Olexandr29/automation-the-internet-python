from pages.base_page import BasePage, Reporter
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CheckboxPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.locators = {
            "checkboxes": (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
        }

    def is_checkbox_visible(self, checkbox_number):
        checkbox = self.find_element_by_number(self.locators["checkboxes"], checkbox_number)
        return checkbox.is_displayed()

    def is_checkbox_checked(self, checkbox_number):
        checkbox = self.find_element_by_number(self.locators["checkboxes"], checkbox_number)
        return checkbox.is_selected()

    def check_specific_checkbox(self, checkbox_number):
        with Reporter.step(f"Check/uncheck the checkbox {checkbox_number}"):
            checkbox = self.find_element_by_number(self.locators["checkboxes"], checkbox_number)
        return checkbox.click()

    def focus_checkbox(self, checkbox_number):  
        with Reporter.step(f"Focus the checkbox {checkbox_number}"):
            checkbox = self.find_element_by_number(self.locators["checkboxes"], checkbox_number)
        return self.focus_element(checkbox)
    
    def is_checkbox_focused(self, checkbox_number):
        checkbox = self.find_element_by_number(self.locators["checkboxes"], checkbox_number)
        return self.is_element_focused(checkbox)

    def press_space(self, checkbox_number):
        checkbox = self.find_element_by_number(self.locators["checkboxes"], checkbox_number)
        return self.press_key_on_element(checkbox, Keys.SPACE)

        
       