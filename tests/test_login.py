from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

class TestLogin:
    valid_username = "tomsmith"
    valid_password = "SuperSecretPassword!"
    expected_alert_username_msg = "Your username is invalid!"
    expected_alert_password_msg = "Your password is invalid!"
    expected_logout_msg = "You logged out of the secure area!"

    
    def setup_method(self, method):
        test_name = method.__name__
        print(f"==========-=========The {test_name} is started==========-=========")
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.driver.get(self.home_page.URL)
        self.login_page = self.home_page.open_login_page()

    def teardown_method(self):    
        self.driver.quit()

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
        actual_result = self.login_page.unsuccessful_login("", "")
        assert self.expected_alert_username_msg in actual_result, \
        "the alert message is wrong for login with BOTH empty credentials"
        assert self.driver.current_url == self.login_page.URL, \
        f"the current page should be Login page without navigation on Secure page but now the page is {self.driver.current_url} "
        
    def test_3_Unsuccessful_login_with_empty_Password(self):
        actual_result = self.login_page.unsuccessful_login(self.valid_username, "")
        assert self.expected_alert_password_msg in actual_result, \
        "the alert message is wrong for login with empty password"
        assert self.driver.current_url == self.login_page.URL, \
        f"the current page should be Login page without navigation on Secure page but now the page is {self.driver.current_url} "

    def test_4_Unsuccessful_login_with_empty_Username(self):
        actual_result = self.login_page.unsuccessful_login("", self.valid_password)
        assert self.expected_alert_username_msg in actual_result, \
        "the alert message is wrong for login with empty Username"
        assert self.driver.current_url == self.login_page.URL, \
        f"the current page should be Login page without navigation on Secure page but now the page is {self.driver.current_url} "

    def test_5_Unsuccessful_login_with_invalid_Password(self):
        actual_result = self.login_page.unsuccessful_login(self.valid_username, "111")
        assert self.expected_alert_password_msg in actual_result, \
        "the alert message is wrong for login with invalid Password"
        assert self.driver.current_url == self.login_page.URL, \
        f"the current page should be Login page without navigation on Secure page but now the page is {self.driver.current_url} "

    def test_6_Unsuccessful_login_with_invalid_Username(self):
        actual_result = self.login_page.unsuccessful_login("1", self.valid_password)
        assert self.expected_alert_username_msg in actual_result, \
        "the alert message is wrong for login with invalid Username"
        assert self.driver.current_url == self.login_page.URL, \
        f"the current page should be Login page without navigation on Secure page but now the page is {self.driver.current_url} "

    def test_7_Unsuccessful_login_with_both_Invalid_Username_and_Password(self):
        actual_result = self.login_page.unsuccessful_login("invalidName", "invalidPassword")
        assert self.expected_alert_username_msg in actual_result, \
        f"the alert message is wrong during {self.test_name} and now the page is {self.driver.current_url}"

    def test_8_Logout(self):
        secure_page = self.login_page.successful_login(self.valid_username, self.valid_password)
        print(f"we are now on {self.driver.current_url}")
        secure_page.logout_method()
        print(f"we are now on {self.driver.current_url}")
        assert self.driver.current_url == self.login_page.URL, \
        f"User should be redirected to the Login page but now on {self.driver.current_url} "
        actual_alert_msg = self.login_page.get_alert_message()
        assert self.expected_logout_msg in actual_alert_msg, \
        "The alert message should be 'You logged out of the secure area!' but now '{actual_alert_msg}'"      
        assert self.login_page.is_login_button_displayed() == True, \
        "The Login button is not displayed"
    
    def test_9_User_cannot_access_the_Secure_Area_after_logout(self):
        secure_page = self.login_page.successful_login(self.valid_username, self.valid_password)
        print(f"we are now on {self.driver.current_url}")
        secure_page.logout_method()
        print(f"we are logout now and on {self.driver.current_url}")
        assert self.driver.current_url == self.login_page.URL, \
        f"User should be redirected to the Login page but now on {self.driver.current_url} "
        actual_alert_msg = self.login_page.get_alert_message()
        assert self.expected_logout_msg in actual_alert_msg, \
        "The alert message should be 'You logged out of the secure area!' but now '{actual_alert_msg}'"      
        print(f"we are now on {self.driver.current_url}")
        self.driver.back()
        print(f"The browser Back button was clicked and we are now on {self.driver.current_url}")
        assert self.driver.current_url == self.login_page.URL, \
        f"User should remains on the Login page and should not be able to access to the Secure Area page but now the page is {self.driver.current_url}"
        assert self.login_page.is_login_button_displayed == True, \
        "The Login button should be displayed"

    def test_10_Login_with_a_Username_that_has_leading_spaces(self):
        actual_result = self.login_page.unsuccessful_login(" tomsmith", self.valid_password)
        assert self.expected_alert_username_msg in actual_result, \
        "The alert 'Your username is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_11_Login_with_a_password_that_has_leading_spaces(self):
        actual_result = self.login_page.unsuccessful_login(self.valid_username, "  SuperSecretPassword!")
        assert self.expected_alert_password_msg in actual_result, \
        "The alert 'Your password is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_12_Login_with_a_Username_that_has_trailing_spaces(self):
        actual_result = self.login_page.unsuccessful_login("tomsmith ", self.valid_password)
        assert self.expected_alert_username_msg in actual_result, \
        "The alert 'Your username is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_13_Login_with_a_Password_that_has_trailing_spaces(self):
        actual_result = self.login_page.unsuccessful_login(self.valid_username, "SuperSecretPassword! ")
        assert self.expected_alert_password_msg in actual_result, \
        "The alert 'Your password is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_14_Login_with_a_Username_that_has_a_different_case(self):
        actual_result = self.login_page.unsuccessful_login("TOMSMITH", self.valid_password)
        assert self.expected_alert_username_msg in actual_result, \
         "The alert 'Your username is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_15_Login_with_a_Password_that_has_a_different_case(self):
        actual_result = self.login_page.unsuccessful_login(self.valid_username, "SUPERSECRETPASSWORD!")
        assert self.expected_alert_password_msg in actual_result, \
         "The alert 'Your password is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_16_Login_with_SQL_Injection_in_Username(self):
        actual_result = self.login_page.unsuccessful_login("' OR '1'='1", "anything")
        assert self.expected_alert_username_msg in actual_result, \
         "The alert 'Your username is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_17_Login_with_SQL_Injection_in_Password(self):
        actual_result = self.login_page.unsuccessful_login(self.valid_username, "' OR '1'='1")
        assert self.expected_alert_password_msg in actual_result, \
         "The alert 'Your password is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_18_Login_with_XSS_in_Username(self):
        actual_result = self.login_page.unsuccessful_login("<script>alert('xss')</script>", self.valid_password)
        assert self.expected_alert_username_msg in actual_result, \
         "The alert 'Your username is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"

    def test_19_Login_with_XSS_in_Password(self):
        actual_result = self.login_page.unsuccessful_login(self.valid_username, "<script>alert('xss')</script>")
        assert self.expected_alert_password_msg in actual_result, \
         "The alert 'Your password is invalid!' should be displayed"
        assert self.driver.current_url == self.login_page.URL, \
        f"The Login page should be opened but now {self.driver.current_url}"


