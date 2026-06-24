from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "login_link" : (By.LINK_TEXT, "Form Authentication")
        }
        
    def open_login_page(self):
        from pages.login_page import LoginPage
        self.click(self.locators["login_link"])
        return LoginPage(self.driver)
    