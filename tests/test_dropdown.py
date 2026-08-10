import pytest
from tests.base_test import BaseTest
from pages.dropdown_page import DropdownPage
from pages.home_page import HomePage

class TestDropdown(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_dropdown_page(self, setup_test):
        self.dropdown_page = self.home_page.open_dropdown_page()

    def test_21_Verify_default_state(self):
        assert self.driver.current_url == self.dropdown_page.URL, "the URL is wrong"
        self.dropdown_page.open_Dropdown();
        assert self.dropdown_page.is_dropdown_visible() == True, "The dropdown is not visible"
        assert self.dropdown_page.get_selected_option_text() == "Please select an option", "The default selected value is not right"
