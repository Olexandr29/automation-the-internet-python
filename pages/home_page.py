from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "login_link" : (By.LINK_TEXT, "Form Authentication"),
            "dropdown_link" : (By.LINK_TEXT, "Dropdown")
        }
        
    def open_login_page(self):
        from pages.login_page import LoginPage
        self.click(self.locators["login_link"])
        return LoginPage(self.driver)

    def open_dropdown_page(self):
        from pages.dropdown_page import DropdownPage
        self.click(self.locators["dropdown_link"])
        return DropdownPage(self.driver)