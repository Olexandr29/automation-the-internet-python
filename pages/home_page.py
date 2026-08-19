from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "login_link" : (By.LINK_TEXT, "Form Authentication"),
            "dropdown_link" : (By.LINK_TEXT, "Dropdown"),
            "checkbox_link" : (By.LINK_TEXT, "Checkboxes")
        }
        
    def open_login_page(self):
        from pages.login_page import LoginPage
        self.click(self.locators["login_link"])
        return LoginPage(self.driver)

    def open_dropdown_page(self):
        from pages.dropdown_page import DropdownPage
        self.click(self.locators["dropdown_link"])
        return DropdownPage(self.driver)

    def is_dropdown_link_visible(self):
        return self.is_visible(self.locators["dropdown_link"])

    def open_checkbox_page(self):
        from pages.checkbox_page import CheckboxPage
        self.click(self.locators["checkbox_link"])
        return CheckboxPage(self.driver)