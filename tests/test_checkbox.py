import pytest
from tests.base_test import BaseTest
from pages.checkbox_page import CheckboxPage
from test_data.checkbox_data import CheckboxData

class TestCheckbox(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_checkbox_page(self, setup_test):
        self.checkbox_page = self.home_page.open_checkbox_page()

    def test_31_verify_checkboxes_visible(self):
        assert self.driver.current_url == CheckboxData.URL_CHECKBOX_PAGE, "The Checkboxes page is not opened"
        assert self.checkbox_page.is_checkbox_visible(1) == True, f"The {CheckboxData.CHECKBOX_1} is not visible"
        assert self.checkbox_page.is_checkbox_visible(2) == True, f"The {CheckboxData.CHECKBOX_2} is not visible"

    def test_32_verify_checkboxes_initial_state(self):
        assert self.checkbox_page.is_checkbox_checked(1) == False, f"The {CheckboxData.CHECKBOX_1} is not unchecked"
        assert self.checkbox_page.is_checkbox_checked(2) == True, f"The {CheckboxData.CHECKBOX_2} is not checked"

    def test_33_verify_checkboxes_state_changes_correctly(self):
        self.checkbox_page.check_specific_checkbox(1)
        assert self.checkbox_page.is_checkbox_checked(1) == True, f"The {CheckboxData.CHECKBOX_1} is not checked after first click"
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