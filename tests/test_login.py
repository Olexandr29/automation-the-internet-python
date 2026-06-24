from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
import pytest


class TestLogin:
    valid_username = "tomsmith"
    valid_password = "SuperSecretPassword!"
    invalid_urername = "just_name"
    invalid_password = "1p5T61"
    sql_injection = "' OR '1'='1"
    xss_cross_site_script = "<script>alert('xss')</script>"
    expected_alert_username_msg = "Your username is invalid!"
    expected_alert_password_msg = "Your password is invalid!"
    expected_logout_msg = "You logged out of the secure area!"

    @pytest.fixture(autouse=True)    
    def setup_method(self, request):
        print(f"==========-=========The {request.node.nodeid} is started==========-=========")
        options = Options()
        options.add_argument("--incognito")
        if os.environ.get("GITHUB_ACTIONS") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
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

    @pytest.mark.parametrize("username, password, expected_msg", [
        pytest.param("", "", expected_alert_username_msg, id="test_2_empty_credentials"),
        pytest.param(valid_username, "", expected_alert_password_msg, id="test_3_empty_Password"),
        pytest.param("", valid_password, expected_alert_username_msg, id="test_4_Unsuccessful_login_with_empty_Username"),
        pytest.param(valid_username, invalid_password, expected_alert_password_msg, id="test_5_Unsuccessful_login_with_invalid_Password"),
        pytest.param(invalid_urername, valid_password, expected_alert_username_msg, id="test_6_Unsuccessful_login_with_invalid_Username"),
        pytest.param(invalid_urername, invalid_password, expected_alert_username_msg, id="test_7_Unsuccessful_login_with_both_Invalid_Username_and_Password"),
        pytest.param(" " + valid_username, valid_password, expected_alert_username_msg, id="test_10_Login_with_a_Username_that_has_leading_spaces"),
        pytest.param(valid_username, " " + valid_password, expected_alert_password_msg, id="test_11_Login_with_a_password_that_has_leading_spaces"),
        pytest.param(valid_username + " ", valid_password, expected_alert_username_msg, id="test_12_Login_with_a_Username_that_has_trailing_spaces"),
        pytest.param(valid_username, valid_password + " ", expected_alert_password_msg, id="test_13_Login_with_a_Password_that_has_trailing_spaces"),
        pytest.param(valid_username.upper(), valid_password, expected_alert_username_msg, id="test_14_Login_with_a_Username_that_has_a_different_case"),
        pytest.param(valid_username, valid_password.upper(), expected_alert_password_msg, id="test_15_Login_with_a_Password_that_has_a_different_case"),
        pytest.param(sql_injection, invalid_password, expected_alert_username_msg, id="test_16_Login_with_SQL_Injection_in_Username"),
        pytest.param(valid_username, sql_injection, expected_alert_password_msg, id="test_17_Login_with_SQL_Injection_in_Password"),
        pytest.param(xss_cross_site_script, valid_password, expected_alert_username_msg, id="test_18_Login_with_XSS_in_Username"),
        pytest.param(valid_username, xss_cross_site_script, expected_alert_password_msg, id="test_19_Login_with_XSS_in_Password")
    ])

    def test_unsuccessful_login(self, username, password, expected_msg):
        actual_result = self.login_page.unsuccessful_login(username, password)
        assert expected_msg in actual_result
        assert self.driver.current_url == self.login_page.URL

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
        self.driver.refresh()
        print(f"The browser REFRESHED and we are now on {self.driver.current_url}")
        login_page = LoginPage(self.driver)
        assert self.driver.current_url == login_page.URL, \
        f"User should remains on the Login page and should not be able to access to the Secure Area page but now the page is {self.driver.current_url}"
        assert login_page.is_login_button_displayed() == True, \
        "The Login button is not displayed, but should be!"
    
    def test_20_Password_is_masked(self):
        assert self.login_page.is_password_hidden() == True, \
        f"The input type should be password, if True, then Password characters is hidden, but now it's {self.login_page.is_password_hidden()} "
        assert self.login_page.is_masked_value_saved("thisPas10") == True, \
        f"The entered value is wrong"
