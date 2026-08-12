from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.reporter import Reporter


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "username" : (By.ID, "username"),
            "password" : (By.ID, "password"),
            "login_button" : (By.CLASS_NAME, "radius"),
            "alert" : (By.ID, "flash")
        }
 
    def successful_login(self, name, pas):
        from pages.secure_page import SecurePage
        with Reporter.step("Fill in the Username field"):
            self.type(self.locators["username"], name)
        with Reporter.step("Fill in the Password field"):
            self.type(self.locators["password"], pas)
        with Reporter.step("Click the Login button"):
            self.click(self.locators["login_button"])
        return SecurePage(self.driver)
    
    def unsuccessful_login(self, name, pas):
        with Reporter.step("Fill in the Username field"):
            if name != "":
                self.type(self.locators["username"], name)
        with Reporter.step("Fill in the Password field"):
            if pas != "":
                self.type(self.locators["password"], pas)
        with Reporter.step("Click the Login button"):
            self.click(self.locators["login_button"])   
        alert_msg = self.get_text(self.locators["alert"])
        return alert_msg
    
    def get_alert_message(self):
        alert_msg = self.get_text(self.locators["alert"])
        print(f"The alert message is '{alert_msg}' ")
        return alert_msg
    
    def is_login_button_displayed(self):
        result = self.is_visible(self.locators["login_button"])
        print(f"Is login button displayed = {result}")
        return result
    
    def is_password_hidden(self):
        password_el = self.find(self.locators["password"])
        password_input_type = password_el.get_attribute("type")
        print(f"The password input type is '{password_input_type}'")
        return password_input_type == "password"

    def is_masked_value_saved(self, pas):
        pas_element = self.find(self.locators["password"])
        pas_element.send_keys(pas)
        entered_value = pas_element.get_attribute("value")
        print(f"Here is the filled in password '{pas}' and the saved value '{entered_value}'")
        return entered_value == pas
