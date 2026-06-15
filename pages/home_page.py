from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "login_link" : (By.LINK_TEXT, "Form Authentication")
        }
        

    def open_login_page(self):
        from pages.login_page import LoginPage
        login_page_element = self.driver.find_element(*self.locators["login_link"])
        login_page_element.click()
        return LoginPage(self.driver)