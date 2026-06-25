
class LoginData:
    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    INVALID_URERNAME = "just_name"
    INVALID_PASSWORD = "1p5T61"
    SQL_INJECTION = "' OR '1'='1"
    XSS_CROSS_SITE_SCRIPT = "<script>alert('xss')</script>"
    EXPECTED_ALERT_USERNAME_MSG = "Your username is invalid!"
    EXPECTED_ALERT_PASSWORD_MSG = "Your password is invalid!"
    EXPECTED_LOGOUT_MSG = "You logged out of the secure area!"