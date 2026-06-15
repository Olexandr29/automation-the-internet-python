from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

class TestLogin:

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.driver.get(self.home_page.URL)
        print(f"The Home page {self.home_page.URL} is opened")
        self.login_page = self.home_page.open_login_page()
        assert self.driver.current_url == self.login_page.URL
        print(f"The Login page {self.login_page.URL} is opened")
        self.secure_page = self.login_page.successful_login("tomsmith", "SuperSecretPassword!")
        assert self.driver.current_url == self.secure_page.URL
        print(f"The Secure page {self.secure_page.URL} is opened")
        expected_alert_msg = "You logged into a secure area!"
        assert expected_alert_msg in self.secure_page.get_alert_message(), \
        "the alert message is wrong"
        expected_welcome_msg = "Welcome to the Secure Area. When you are done click logout below."
        assert expected_welcome_msg in self.secure_page.get_welcome_message(), \
        "the welcome message is wrong"
        assert self.secure_page.is_logout_button_displayed() == True, \
        "the logout button is not displayed"
        self.driver.quit()

        