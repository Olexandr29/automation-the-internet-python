from tests.base_test import BaseTest, pytest
from pages.checkbox_page import CheckboxPage
from test_data.checkbox_data import CheckboxData
import allure
from utils.reporter import Reporter

@allure.feature("Checkbox")
@pytest.mark.regression
class TestCheckbox(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_checkbox_page(self, setup_test):
        with Reporter.step("Open checkbox page"):
            self.checkbox_page = self.home_page.open_checkbox_page()

    @pytest.mark.smoke
    def test_31_verify_checkboxes_visible(self):
        assert self.driver.current_url == CheckboxData.URL_CHECKBOX_PAGE, "The Checkboxes page is not opened"
        with Reporter.step("Observe checkboxes are visible"):
            assert self.checkbox_page.is_checkbox_visible(1) == True, f"The {CheckboxData.CHECKBOX_1} is not visible"
            assert self.checkbox_page.is_checkbox_visible(2) == True, f"The {CheckboxData.CHECKBOX_2} is not visible"

    def test_32_verify_checkboxes_initial_state(self):
        with Reporter.step("Observe checkboxes initial state"):
            assert self.checkbox_page.is_checkbox_checked(1) == False, f"The {CheckboxData.CHECKBOX_1} is not unchecked"
            assert self.checkbox_page.is_checkbox_checked(2) == True, f"The {CheckboxData.CHECKBOX_2} is not checked"

    @pytest.mark.smoke
    def test_33_verify_checkboxes_state_changes_correctly(self):
        self.checkbox_page.check_specific_checkbox(1)
        # verify screenshot on failure, change the expected result for next test from True to False
        assert self.checkbox_page.is_checkbox_checked(1) == False, f"The {CheckboxData.CHECKBOX_1} is not checked after first click"

        # assert self.checkbox_page.is_checkbox_checked(1) == True, f"The {CheckboxData.CHECKBOX_1} is not checked after first click"

        self.checkbox_page.check_specific_checkbox(1)
        assert self.checkbox_page.is_checkbox_checked(1) == False, f"The {CheckboxData.CHECKBOX_1} is not unchecked after second click"
        self.checkbox_page.check_specific_checkbox(2)
        assert self.checkbox_page.is_checkbox_checked(2) == False, f"The {CheckboxData.CHECKBOX_2} is not unchecked after first click"
        self.checkbox_page.check_specific_checkbox(2)
        assert self.checkbox_page.is_checkbox_checked(2) == True, f"The {CheckboxData.CHECKBOX_2} is checked after second click"

    def test_34_verify_checkboxes_state_after_refresh(self):
        self.checkbox_page.check_specific_checkbox(1)
        assert self.checkbox_page.is_checkbox_checked(1) == True, f"The {CheckboxData.CHECKBOX_1} is not checked"
        assert self.checkbox_page.is_checkbox_checked(2) == True, f"The {CheckboxData.CHECKBOX_2} is not checked"
        with Reporter.step("Refresh the page"):
            self.driver.refresh()
        assert self.checkbox_page.is_checkbox_checked(1) == False, f"The {CheckboxData.CHECKBOX_1} is checked"
        assert self.checkbox_page.is_checkbox_checked(2) == True, f"The {CheckboxData.CHECKBOX_2} is not checked"

    def test_35_verify_checkbox_state_chnges_using_keyboard(self):
        self.checkbox_page.focus_checkbox(1)
        assert self.checkbox_page.is_checkbox_focused(1) == True, f"The {CheckboxData.CHECKBOX_1} is not focused"
        self.checkbox_page.press_space(1)
        assert self.checkbox_page.is_checkbox_checked(1) == True, f"The {CheckboxData.CHECKBOX_1} state is not chaged via pressing space key"
        self.checkbox_page.focus_checkbox(2)
        assert self.checkbox_page.is_checkbox_focused(2) == True, f"The {CheckboxData.CHECKBOX_2} is not focused"
        self.checkbox_page.press_space(2)
        assert self.checkbox_page.is_checkbox_checked(2) == False, f"The {CheckboxData.CHECKBOX_2} state is not chaged via pressing space key"