from tests.base_test import BaseTest, pytest
from pages.dynamic_controls_page import DynamicControlsPage

@pytest.mark.regression
class TestDynamicControls(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_dynamic_controls(self, setup_test):
        self.dynamic_contols_page = self.home_page.open_dynamic_controls_page()

    @pytest.mark.smoke
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
        assert self.dynamic_contols_page.get_checkbox_text() == "A checkbox"

        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == "Remove"

        assert self.dynamic_contols_page.is_subheader_enabel_disable_displayed() is True
        assert self.dynamic_contols_page.get_subheader_enabel_disable_text() == "Enable/disable"

        assert self.dynamic_contols_page.is_input_displayed() is True

        assert self.dynamic_contols_page.is_enable_btn_displayed() is True
        assert self.dynamic_contols_page.get_enable_btn_text() == "Enable"

        assert self.dynamic_contols_page.is_footer_displayed() is True
        assert self.dynamic_contols_page.get_footer_text() == "Powered by Elemental Selenium and Sauce Labs"
        assert self.dynamic_contols_page.is_elemental_selenium_link_displayed() is True
        assert self.dynamic_contols_page.is_sauce_labs_link_displayed() is True

    @pytest.mark.smoke
    def test_TC39_verify_checkbox_initial_state_and_changes(self):
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is False

    def test_TC40_remove_and_add_checkbox(self):
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_checkbox_absent()
        assert self.dynamic_contols_page.is_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_add_btn_displayed() is True
        assert self.dynamic_contols_page.get_add_btn_text() == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == '''It's gone!'''

        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == "Remove"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != "It's gone!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's back!"

    @pytest.mark.smoke
    def test_TC41_remove_and_add_checked_checkbox(self):
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
# step 3
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_checkbox_absent()
        assert self.dynamic_contols_page.is_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_add_btn_displayed() is True
        assert self.dynamic_contols_page.get_add_btn_text() == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == '''It's gone!'''
# step 4
        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == "Remove"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != "It's gone!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's back!"
# step 5
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_checkbox_absent()
        assert self.dynamic_contols_page.is_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == "A checkbox"
        assert self.dynamic_contols_page.is_remove_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_add_btn_displayed() is True
        assert self.dynamic_contols_page.get_add_btn_text() == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == '''It's gone!'''
# step 6
        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == "A checkbox"      
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == "Remove"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != "It's gone!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's back!"
# step 7
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_checkbox_absent()
        assert self.dynamic_contols_page.is_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == "A checkbox"
        assert self.dynamic_contols_page.get_amount_of_text_without_checkboxes() == 2
        assert self.dynamic_contols_page.is_remove_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_add_btn_displayed() is True
        assert self.dynamic_contols_page.get_add_btn_text() == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == '''It's gone!'''        
# step 8
        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == "A checkbox"  
        assert self.dynamic_contols_page.get_amount_of_text_without_checkboxes() == 3    
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == "Remove"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != "It's gone!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's back!"


    @pytest.mark.smoke
    def test_TC42_enable_and_disable_the_Input_field(self):
        assert self.dynamic_contols_page.is_input_field_enabeled() is False
        
        self.dynamic_contols_page.click_on_enable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_clickable()
        assert self.dynamic_contols_page.is_input_field_enabeled() is True
        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) != "Enable"
        assert self.dynamic_contols_page.get_btn_text(2) == "Disable"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's enabled!"

        self.dynamic_contols_page.enter_to_input_field("Hello")
        assert self.dynamic_contols_page.get_inputed_text() == "Hello"

        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) == "Disable"
        self.dynamic_contols_page.click_on_btn(2)
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_disabled()
        assert self.dynamic_contols_page.get_inputed_text() == "Hello"
        assert self.dynamic_contols_page.get_btn_text(2) != "Disable"
        assert self.dynamic_contols_page.get_btn_text(2) == "Enable"
        assert self.dynamic_contols_page.get_text_under_btn() != "It's enabled!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's disabled!"

    def test_TC43_verify_checkbox_section_state_after_refresh(self):
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_checkbox_absent()
        assert self.dynamic_contols_page.is_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.get_btn_text(1) != "Remove"
        assert self.dynamic_contols_page.get_btn_text(1) == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == "It's gone!"

        self.driver.refresh()
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        assert self.dynamic_contols_page.is_btn_displayed(1) is True
        assert self.dynamic_contols_page.get_btn_text(1) == "Remove"

        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True

        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_checkbox_absent()
        assert self.dynamic_contols_page.is_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.get_btn_text(1) != "Remove"
        assert self.dynamic_contols_page.get_btn_text(1) == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == "It's gone!"
        
        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        assert self.dynamic_contols_page.is_btn_displayed(1) is True
        assert self.dynamic_contols_page.get_btn_text(1) != "Add"
        assert self.dynamic_contols_page.get_btn_text(1) == "Remove"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != "It's gone!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's back!"

        self.driver.refresh()
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        assert self.dynamic_contols_page.is_btn_displayed(1) is True
        assert self.dynamic_contols_page.get_btn_text(1) == "Remove"


    def test_TC44_verify_Iput_field_section_state_after_refresh(self):
        self.dynamic_contols_page.click_on_enable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_clickable()
        assert self.dynamic_contols_page.is_input_field_enabeled() is True
        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) != "Enable"
        assert self.dynamic_contols_page.get_btn_text(2) == "Disable"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's enabled!"

        self.driver.refresh()
        assert self.dynamic_contols_page.is_input_field_enabeled() is False
        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) == "Enable"

        self.dynamic_contols_page.click_on_enable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_clickable()
        assert self.dynamic_contols_page.is_input_field_enabeled() is True
        self.dynamic_contols_page.enter_to_input_field("Input123$")
        assert self.dynamic_contols_page.get_inputed_text() == "Input123$"

        self.dynamic_contols_page.click_on_btn(2)
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_disabled()
        assert self.dynamic_contols_page.get_inputed_text() == "Input123$"
        assert self.dynamic_contols_page.get_btn_text(2) != "Disable"
        assert self.dynamic_contols_page.get_btn_text(2) == "Enable"
        assert self.dynamic_contols_page.get_text_under_btn() != "It's enabled!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's disabled!"    

        self.driver.refresh()
        assert self.dynamic_contols_page.is_input_field_enabeled() is False
        assert self.dynamic_contols_page.get_btn_text(2) == "Enable"

    def test_TC45_navigate_select_and_change_checkbox_section_state_using_keyboard(self):
# step 1
        self.dynamic_contols_page.focus_checkbox()
        assert self.dynamic_contols_page.is_checkbox_focused() is True
# step 2        
        self.dynamic_contols_page.press_space()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
# step 3
        self.dynamic_contols_page.focus_remove_btn()
        assert self.dynamic_contols_page.is_remove_btn_focused() is True
# step 4
        self.dynamic_contols_page.press_enter()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_checkbox_absent()
        assert self.dynamic_contols_page.is_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.get_btn_text(1) != "Remove"
        assert self.dynamic_contols_page.get_btn_text(1) == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == "It's gone!"
# step 5
        self.dynamic_contols_page.focus_add_btn()
        assert self.dynamic_contols_page.is_add_btn_focused() is True
# step 6
        self.dynamic_contols_page.press_enter_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is False
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == "Remove"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != "It's gone!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's back!"
# step 7
        self.dynamic_contols_page.focus_checkbox()
        assert self.dynamic_contols_page.is_checkbox_focused() is True
        self.dynamic_contols_page.press_space()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
# step 8
        self.dynamic_contols_page.focus_remove_btn()
        assert self.dynamic_contols_page.is_remove_btn_focused() is True

        self.dynamic_contols_page.press_enter()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_checkbox_absent()
        assert self.dynamic_contols_page.is_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.get_btn_text(1) != "Remove"
        assert self.dynamic_contols_page.get_btn_text(1) == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == "It's gone!"
# step 9
        self.dynamic_contols_page.focus_add_btn()
        assert self.dynamic_contols_page.is_add_btn_focused() is True

        self.dynamic_contols_page.press_enter_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is False

        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == "A checkbox"
        assert self.dynamic_contols_page.get_amount_of_text_without_checkboxes() == 2   

        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == "Remove"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != "It's gone!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's back!"

    def test_TC46_navigate_select_and_change_input_field_section_state_using_keyboard(self):
# step 1
        self.dynamic_contols_page.focus_enale_btn()
        assert self.dynamic_contols_page.is_enable_btn_focused() is True
# step 2
        self.dynamic_contols_page.press_enter_on_enable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_clickable()
        assert self.dynamic_contols_page.is_input_field_enabeled() is True
        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) != "Enable"
        assert self.dynamic_contols_page.get_btn_text(2) == "Disable"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's enabled!"
# step 3
        self.dynamic_contols_page.focus_input_field()
        assert self.dynamic_contols_page.is_input_filed_focused()
# step 4
        self.dynamic_contols_page.enter_to_input_field("$And40")
        assert self.dynamic_contols_page.get_inputed_text() == "$And40"
# step 5
        self.dynamic_contols_page.focus_disable_btn()
        assert self.dynamic_contols_page.is_disable_btn_focused() is True
# step 6
        self.dynamic_contols_page.press_enter_on_disable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == "Wait for it..."
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_disabled()
        assert self.dynamic_contols_page.get_inputed_text() == "$And40"
        assert self.dynamic_contols_page.get_btn_text(2) != "Disable"
        assert self.dynamic_contols_page.get_btn_text(2) == "Enable"
        assert self.dynamic_contols_page.get_text_under_btn() != "It's enabled!"
        assert self.dynamic_contols_page.get_text_under_btn() == "It's disabled!"


