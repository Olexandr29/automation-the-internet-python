from tests.base_test import BaseTest, pytest
from pages.dynamic_controls_page import DynamicControlsPage

class TestDynamicControls(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_dynamic_controls(self, setup_test):
        self.dynamic_contols_page = self.home_page.open_dynamic_controls_page()

    def test_TC38_verify_page_content(self):
        assert self.driver.current_url == "https://the-internet.herokuapp.com/dynamic_controls"
        assert self.dynamic_contols_page.get_document_ready_state() == "complete"
        
        assert self.dynamic_contols_page.is_header_displayed() is True
        assert self.dynamic_contols_page.get_header_text() == "Dynamic Controls"

        assert self.dynamic_contols_page.is_paragraph_displayed() is True
        assert self.dynamic_contols_page.get_paragraph_text() == "This example demonstrates when elements (e.g., checkbox, input field, etc.) are changed asynchronously."

        assert self.dynamic_contols_page.is_subheader_remove_add_displayed() is True
        assert self.dynamic_contols_page.get_subheader_remove_add_text() == "Remove/add"

        assert self.dynamic_contols_page.get_amount_of_checkboxes() == 1
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        # assert self.dynamic_contols_page.get_checkbox_text() == "A checkbox"