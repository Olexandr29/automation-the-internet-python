from selenium.webdriver.common.by import By

class SecurePage:
    URL = "https://the-internet.herokuapp.com/secure"

    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "alert" : (By.ID, "flash"),
            "welcome_message" : (By.CLASS_NAME, "subheader"),
            "logout_button" : (By.XPATH, "//a[@class='button secondary radius']")
        }

    def get_alert_message(self):
        alert_el = self.driver.find_element(*self.locators["alert"])
        alert_msg = alert_el.text
        print(f"The alert message is '{alert_msg}' ")
        return alert_msg
    
    def get_welcome_message(self):
        subheader_el = self.driver.find_element(*self.locators["welcome_message"])
        message = subheader_el.text
        print(f"the welcome message is '{message}'")
        return message
    
    def is_logout_button_displayed(self):
        logout_btn_el = self.driver.find_element(*self.locators["logout_button"])
        result = logout_btn_el.is_displayed()
        print(f"Is logout button displayed = {result}")
        return result
    
    def logout_method(self):
        from pages.login_page import LoginPage
        logout_btn_el = self.driver.find_element(*self.locators["logout_button"])
        logout_btn_el.click()
        return LoginPage(self.driver)