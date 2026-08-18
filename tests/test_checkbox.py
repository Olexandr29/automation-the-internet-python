import pytest
from tests.base_test import BaseTest
from pages.checkbox_page import CheckboxPage
from test_data.checkbox_data import CheckboxData

class TestCheckbox(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_checkbox_page(self, setup_test):
        self.checkbox_page = self.home_page.open_checkbox_page()

    def test_31_verify_Checkboxes_visible(self):
        assert self.driver.current_url == CheckboxData.URL_CHECKBOX_PAGE
        assert self.checkbox_page.is_checkbox_visible(1) == True
        assert self.checkbox_page.is_checkbox_visible(2) == True

