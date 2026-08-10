import pytest
from tests.base_test import BaseTest
from pages.dropdown_page import DropdownPage
from pages.home_page import HomePage
from test_data.dropdown_data import DropdownData

class TestDropdown(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_dropdown_page(self, setup_test):
        self.dropdown_page = self.home_page.open_dropdown_page()

    def test_21_verify_default_state(self):
        assert self.driver.current_url == DropdownData.URL_DROPDOWN_PAGE, "the URL is wrong"
        self.dropdown_page.open_dropdown();
        assert self.dropdown_page.is_dropdown_visible(), "The dropdown is not visible"
        assert self.dropdown_page.get_selected_option_text() == DropdownData.OPTION_DEFAULT, "The default selected value is not right"

    def test_22_verify_all_available_options_are_displayed(self):
        expected_options = [
            DropdownData.OPTION_DEFAULT, DropdownData.OPTION_1, DropdownData.OPTION_2
            ]
        assert self.dropdown_page.are_expected_options_displayed(expected_options), "The expected options are not displayed"

    def test_23_select_option_1(self):
        self.dropdown_page.select_option(DropdownData.OPTION_1)
        assert self.dropdown_page.get_selected_option_text() == DropdownData.OPTION_1, f"The {DropdownData.OPTION_1} is not selected"

    def test_24_Verify_option_remains_selected_after_reopening_and_closing(self):
        self.dropdown_page.select_option(DropdownData.OPTION_2)
        assert self.dropdown_page.get_selected_option_text() == DropdownData.OPTION_2, f"The {DropdownData.OPTION_2} is not selected"
        self.dropdown_page.open_dropdown();
        assert self.dropdown_page.get_selected_option_text() == DropdownData.OPTION_2, f"The {DropdownData.OPTION_2} became not selected after opening dropdown again"
        self.dropdown_page.press_escape();
        assert self.dropdown_page.get_selected_option_text() == DropdownData.OPTION_2, f"The {DropdownData.OPTION_2} became not selected after closing dropdown"

    def test_25_change_selected_option_using_keyboard_arrow_keys(self):
        self.dropdown_page.focus_dropdown()
        assert self.dropdown_page.is_dropdown_focused(), 'The dropdown is not focused'
        self.dropdown_page.press_arrow_down()
        assert self.dropdown_page.get_selected_option_text() == DropdownData.OPTION_1, f"The ${DropdownData.OPTION_1} is not selected via keaboard key"     
        self.dropdown_page.press_arrow_down()
        assert self.dropdown_page.get_selected_option_text() == DropdownData.OPTION_2, f"The ${DropdownData.OPTION_2} is not became selected after pressing Arrow Down"
        self.dropdown_page.press_arrow_up()
        assert self.dropdown_page.get_selected_option_text() == DropdownData.OPTION_1, f"The ${DropdownData.OPTION_1} is not became selected after pressing Arrow Up"
        

