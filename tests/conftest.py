import allure
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        test_instance = getattr(item, "instance", None)
        if test_instance and hasattr(test_instance, "driver"):
            driver = test_instance.driver
            screenshot = driver.get_screenshot_as_png()

            allure.attach(
                screenshot,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )
