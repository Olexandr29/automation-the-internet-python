from selenium.webdriver.common.by import By
from pages.base_page import BasePage


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
        self.type(self.locators["username"], name)
        self.type(self.locators["password"], pas)
        self.click(self.locators["login_button"])
        return SecurePage(self.driver)
    
    def unsuccessful_login(self, name, pas):
        if name == "" and pas == "" :
            print("the username and password empty")
        elif name == "" :
            print("the username is empty")
            self.type(self.locators["password"], pas)
        elif pas == "" :
            print("the password is empty")
            self.type(self.locators["username"], name)
        else :
            print("niether username nor password is empty")
            self.type(self.locators["username"], name)
            self.type(self.locators["password"], pas)

        self.click(self.locators["login_button"])   
        alert_msg = self.get_text(self.locators["alert"])
        print(f"the alert message is '{alert_msg}'")
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
