from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dropdown"
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.locators = {
            "dropdownLocator" : (By.ID, "dropdown") 
        }

    def open_Dropdown(self):
        self.click(self.locators["dropdownLocator"])

    def is_dropdown_visible(self):
        return self.is_visible(self.locators["dropdownLocator"])

    def get_selected_option_text(self):
        dropdown = Select(self.find(self.locators["dropdownLocator"]))
        return dropdown.first_selected_option.text

    
