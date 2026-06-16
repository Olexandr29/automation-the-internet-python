from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

class TestLogin:

    def setup_method(self, method):
        test_name = method.__name__
        print(f"==========-=========The {test_name} is started==========-=========")
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.driver.get(self.home_page.URL)
        self.login_page = self.home_page.open_login_page()

    def test_1_Successful_login(self):
        assert self.driver.current_url == self.login_page.URL
        secure_page = self.login_page.successful_login("tomsmith", "SuperSecretPassword!")
        expected_alert_msg = "You logged into a secure area!"
        assert expected_alert_msg in secure_page.get_alert_message(), \
        "the alert message is wrong"
        expected_welcome_msg = "Welcome to the Secure Area. When you are done click logout below."
        assert expected_welcome_msg in secure_page.get_welcome_message(), \
        "the welcome message is wrong"
        assert self.driver.current_url == secure_page.URL
        assert secure_page.is_logout_button_displayed() == True, \
        "the logout button is not displayed"

    def test_2_Unsuccessful_login_with_empty_credentials(self):
        expected_alert_msg = "Your username is invalid!"
        actual_alert_msg = self.login_page.unsuccessful_login("", "")
        assert expected_alert_msg in actual_alert_msg
        assert self.driver.current_url == self.login_page.URL
        

    def teardown_method(self):    
        self.driver.quit() 
    

        