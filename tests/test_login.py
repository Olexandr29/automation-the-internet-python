import pytest
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from test_data.login_data import LoginData
import allure
from utils.reporter import Reporter

@allure.feature("Login")
@pytest.mark.regression
class TestLogin(BaseTest):
      
    @pytest.fixture(autouse=True)
    def setup_login_page(self, setup_test):
        with Reporter.step("Open login page"):
            self.login_page = self.home_page.open_login_page()

    @pytest.mark.smoke
    def test_1_Successful_login(self):
        assert self.driver.current_url == LoginData.URL_LOGIN_PAGE
        secure_page = self.login_page.successful_login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)
        expected_alert_msg = "You logged into a secure area!"
        assert expected_alert_msg in secure_page.get_alert_message(), \
        "the alert message is wrong"
        expected_welcome_msg = "Welcome to the Secure Area. When you are done click logout below."
        assert expected_welcome_msg in secure_page.get_welcome_message(), \
        "the welcome message is wrong"
        assert self.driver.current_url == LoginData.URL_SECURE_PAGE
        assert secure_page.is_logout_button_displayed() == True, \
        "the logout button is not displayed"

    @pytest.mark.parametrize("username, password_type, expected_msg", [
            pytest.param("", "empty", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_2_empty_credentials"),
            pytest.param(LoginData.VALID_USERNAME, "empty", LoginData.EXPECTED_ALERT_PASSWORD_MSG, id="test_3_empty_Password"),
            pytest.param("", "valid", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_4_Unsuccessful_login_with_empty_Username"),
            pytest.param(LoginData.VALID_USERNAME, "invalid", LoginData.EXPECTED_ALERT_PASSWORD_MSG, id="test_5_Unsuccessful_login_with_invalid_Password"),
            pytest.param(LoginData.INVALID_USERNAME, "valid", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_6_Unsuccessful_login_with_invalid_Username"),
            pytest.param(LoginData.INVALID_USERNAME, "invalid", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_7_Unsuccessful_login_with_both_Invalid_Username_and_Password"),
            pytest.param(" " + LoginData.VALID_USERNAME, "valid", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_10_Login_with_a_Username_that_has_leading_spaces"),
            pytest.param(LoginData.VALID_USERNAME,  "leading_spaces", LoginData.EXPECTED_ALERT_PASSWORD_MSG, id="test_11_Login_with_a_password_that_has_leading_spaces"),
            pytest.param(LoginData.VALID_USERNAME + " ", "valid", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_12_Login_with_a_Username_that_has_trailing_spaces"),
            pytest.param(LoginData.VALID_USERNAME, "trailing_spaces", LoginData.EXPECTED_ALERT_PASSWORD_MSG, id="test_13_Login_with_a_Password_that_has_trailing_spaces"),
            pytest.param(LoginData.VALID_USERNAME.upper(), "valid", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_14_Login_with_a_Username_that_has_a_different_case"),
            pytest.param(LoginData.VALID_USERNAME, "uppercase", LoginData.EXPECTED_ALERT_PASSWORD_MSG, id="test_15_Login_with_a_Password_that_has_a_different_case"),
            pytest.param(LoginData.SQL_INJECTION, "invalid", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_16_Login_with_SQL_Injection_in_Username"),
            pytest.param(LoginData.VALID_USERNAME, "sql_injection", LoginData.EXPECTED_ALERT_PASSWORD_MSG, id="test_17_Login_with_SQL_Injection_in_Password"),
            pytest.param(LoginData.XSS_CROSS_SITE_SCRIPT, "valid", LoginData.EXPECTED_ALERT_USERNAME_MSG, id="test_18_Login_with_XSS_in_Username"),
            pytest.param(LoginData.VALID_USERNAME, "xss", LoginData.EXPECTED_ALERT_PASSWORD_MSG, id="test_19_Login_with_XSS_in_Password")
        ])

    def test_unsuccessful_login(self, username, password_type, expected_msg):
        passwords = {
            "empty": "",
            "valid": LoginData.VALID_PASSWORD,
            "invalid": LoginData.INVALID_PASSWORD,
            "leading_spaces": " " + LoginData.VALID_PASSWORD,
            "trailing_spaces": LoginData.VALID_PASSWORD + " ",
            "uppercase": LoginData.VALID_PASSWORD.upper(),
            "sql_injection": LoginData.SQL_INJECTION,
            "xss": LoginData.XSS_CROSS_SITE_SCRIPT
        }
        password = passwords[password_type]
        actual_result = self.login_page.unsuccessful_login(username, password)
        assert expected_msg in actual_result
        assert self.driver.current_url == LoginData.URL_LOGIN_PAGE

    @pytest.mark.smoke
    def test_8_Logout(self):
        secure_page = self.login_page.successful_login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)
        secure_page.logout_method()
        assert self.driver.current_url == LoginData.URL_LOGIN_PAGE, \
        f"User should be redirected to the Login page but now on {self.driver.current_url} "
        actual_alert_msg = self.login_page.get_alert_message()
        assert LoginData.EXPECTED_LOGOUT_MSG in actual_alert_msg, \
        "The alert message should be 'You logged out of the secure area!' but now '{actual_alert_msg}'"      
        assert self.login_page.is_login_button_displayed() == True, \
        "The Login button is not displayed"
    
    @pytest.mark.smoke
    def test_9_User_cannot_access_the_Secure_Area_after_logout(self):
        secure_page = self.login_page.successful_login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD)
        secure_page.logout_method()
        assert self.driver.current_url == LoginData.URL_LOGIN_PAGE, \
        f"User should be redirected to the Login page but now on {self.driver.current_url} "
        actual_alert_msg = self.login_page.get_alert_message()
        assert LoginData.EXPECTED_LOGOUT_MSG in actual_alert_msg, \
        "The alert message should be 'You logged out of the secure area!' but now '{actual_alert_msg}'"      
        self.driver.back()
        self.driver.refresh()
        login_page = LoginPage(self.driver)
        assert self.driver.current_url == LoginData.URL_LOGIN_PAGE, \
        f"User should remains on the Login page and should not be able to access to the Secure Area page but now the page is {self.driver.current_url}"
        assert login_page.is_login_button_displayed() == True, \
        "The Login button is not displayed, but should be!"
    
    @pytest.mark.smoke
    def test_20_Password_is_masked(self):
        assert self.login_page.is_password_hidden() == True, \
        f"The input type should be password, if True, then Password characters is hidden, but now it's {self.login_page.is_password_hidden()} "
        assert self.login_page.is_masked_value_saved("thisPas10") == True, \
        f"The entered value is wrong"
