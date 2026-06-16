from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "username" : (By.ID, "username"),
            "password" : (By.ID, "password"),
            "login_button" : (By.CLASS_NAME, "radius"),
            "alert" : (By.ID, "flash")
        }

    def successful_login(self, name, pas):
        from pages.secure_page import SecurePage
        username_el = self.driver.find_element(*self.locators["username"])
        password_el = self.driver.find_element(*self.locators["password"])
        login_btn_el = self.driver.find_element(*self.locators["login_button"])
        password_el.send_keys(pas)
        username_el.send_keys(name)
        login_btn_el.click()
        return SecurePage(self.driver)
    
    def unsuccessful_login(self, name, pas):
        username_el = self.driver.find_element(*self.locators["username"])
        password_el = self.driver.find_element(*self.locators["password"])
        login_btn_el = self.driver.find_element(*self.locators["login_button"])
        if name == "" and pas == "" :
            print("the username and password empty")
        elif name == "" :
            print("the username is empty")
            password_el.send_keys(pas)
        elif pas == "" :
            print("the password is empty")
            username_el.send_keys(name)
        else :
            print("niether username nor password is empty")
            username_el.send_keys(name)
            password_el.send_keys(pas)
        login_btn_el.click()
        alert_el = self.driver.find_element(*self.locators["alert"])
        alert_msg = alert_el.text
        print(f"the alert message is '{alert_msg}'")
        return alert_msg


