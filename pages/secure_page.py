from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SecurePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "alert" : (By.ID, "flash"),
            "welcome_message" : (By.CLASS_NAME, "subheader"),
            "logout_button" : (By.XPATH, "//a[@class='button secondary radius']")
        }

    def get_alert_message(self):
        alert_msg = self.get_text(self.locators["alert"])
        return alert_msg
    
    def get_welcome_message(self):
        message = self.get_text(self.locators["welcome_message"])
        return message
    
    def is_logout_button_displayed(self):
        result = self.is_visible(self.locators["logout_button"])
        return result
    
    def logout_method(self):
        from pages.login_page import LoginPage
        self.click(self.locators["logout_button"])
        return LoginPage(self.driver)