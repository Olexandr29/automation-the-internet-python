from tests.base_test import BaseTest, pytest
from pages.dynamic_controls_page import DynamicControlsPage
from test_data.dynamic_controls_data import DynamicControlsData
import allure
from utils.reporter import Reporter

@allure.feature("Dynamic Controls")
@pytest.mark.regression
class TestDynamicControls(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_dynamic_controls(self, setup_test):
        self.dynamic_contols_page = self.home_page.open_dynamic_controls_page()

    @pytest.mark.smoke
    def test_TC38_verify_page_content(self):
        with Reporter.step("Open Dynamic Controls page"):
                assert self.driver.current_url == DynamicControlsData.URL
        assert self.dynamic_contols_page.get_document_ready_state() == "complete"
        
        assert self.dynamic_contols_page.is_header_displayed() is True
        assert self.dynamic_contols_page.get_header_text() == DynamicControlsData.HEADER

        assert self.dynamic_contols_page.is_paragraph_displayed() is True
        assert self.dynamic_contols_page.get_paragraph_text() == DynamicControlsData.PARAGRAPH
        assert self.dynamic_contols_page.is_subheader_remove_add_displayed() is True
        assert self.dynamic_contols_page.get_subheader_remove_add_text() == DynamicControlsData.TITLE_OF_CHECKBOX_SECTION

        assert self.dynamic_contols_page.get_amount_of_checkboxes() == DynamicControlsData.INITIAL_CHECKBOX_AMOUNT
        with Reporter.step("Observe the Checkbox 'A checkbox' visibillity"):
                assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_checkbox_text() == DynamicControlsData.CHECKBOX_TITLE
        with Reporter.step("Observe the 'Remove' button visibillity"):
                assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == DynamicControlsData.REMOVE_BUTTON_TITLE

        assert self.dynamic_contols_page.is_subheader_enabel_disable_displayed() is True
        assert self.dynamic_contols_page.get_subheader_enabel_disable_text() == DynamicControlsData.TITLE_OF_INPUT_SECTION
        with Reporter.step("Observe the Input field visibillity"):
                assert self.dynamic_contols_page.is_input_displayed() is True
        
        with Reporter.step("Observe the 'Enable' button visibillity"):
                assert self.dynamic_contols_page.is_enable_btn_displayed() is True
        assert self.dynamic_contols_page.get_enable_btn_text() == DynamicControlsData.ENABLE_BUTTON_TITLE

        assert self.dynamic_contols_page.is_footer_displayed() is True
        assert self.dynamic_contols_page.get_footer_text() == DynamicControlsData.FOOTER
        with Reporter.step("Observe the Footer links visibillity"):
                assert self.dynamic_contols_page.is_elemental_selenium_link_displayed() is True
                assert self.dynamic_contols_page.is_sauce_labs_link_displayed() is True

    @pytest.mark.smoke
    def test_TC39_verify_checkbox_initial_state_and_changes(self):
        with Reporter.step("Observe the Checkbox initial state"):
                assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is False

    def test_TC40_remove_and_add_checkbox(self):
        with Reporter.step("Observe the Checkbox initial state"):
                assert self.dynamic_contols_page.is_checkbox_checked() is False
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_add_btn_displayed() is True
        assert self.dynamic_contols_page.get_add_btn_text() == DynamicControlsData.ADD_BUTTON_TITLE
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_REMOVE

        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == DynamicControlsData.REMOVE_BUTTON_TITLE
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_REMOVE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ADD 

    @pytest.mark.smoke
    def test_TC41_remove_and_add_checked_checkbox(self):
        with Reporter.step("Observe the Checkbox initial state"):
                assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
# step 3
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_add_btn_displayed() is True
        assert self.dynamic_contols_page.get_add_btn_text() == DynamicControlsData.ADD_BUTTON_TITLE
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_REMOVE
# step 4
        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == DynamicControlsData.REMOVE_BUTTON_TITLE
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_REMOVE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ADD
# step 5
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == DynamicControlsData.TEXT_FROM_PLACE_WHERE_WAS_CHECKBOX
        assert self.dynamic_contols_page.is_remove_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_add_btn_displayed() is True
        assert self.dynamic_contols_page.get_add_btn_text() ==  DynamicControlsData.ADD_BUTTON_TITLE
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() ==  DynamicControlsData.TEXT_AFTER_REMOVE
# step 6
        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == DynamicControlsData.TEXT_FROM_PLACE_WHERE_WAS_CHECKBOX      
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == DynamicControlsData.REMOVE_BUTTON_TITLE
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_REMOVE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ADD
# step 7
        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == DynamicControlsData.TEXT_FROM_PLACE_WHERE_WAS_CHECKBOX
        assert self.dynamic_contols_page.get_amount_of_text_without_checkboxes() == 2
        assert self.dynamic_contols_page.is_remove_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_add_btn_displayed() is True
        assert self.dynamic_contols_page.get_add_btn_text() == DynamicControlsData.ADD_BUTTON_TITLE 
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_REMOVE        
# step 8
        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == DynamicControlsData.TEXT_FROM_PLACE_WHERE_WAS_CHECKBOX  
        assert self.dynamic_contols_page.get_amount_of_text_without_checkboxes() == 3    
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == DynamicControlsData.REMOVE_BUTTON_TITLE        
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_REMOVE 
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ADD 


    @pytest.mark.smoke
    def test_TC42_enable_and_disable_the_Input_field(self):
        with Reporter.step("Observe the Input field initial state"):
                assert self.dynamic_contols_page.is_input_field_enabeled() is DynamicControlsData.INITIAL_INPUT_STATE
        self.dynamic_contols_page.click_on_enable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT 
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_input_is_enabled() is True
        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) != DynamicControlsData.ENABLE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.DISABLE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ENABLE

        self.dynamic_contols_page.enter_to_input_field(DynamicControlsData.INPUT_TEXT_MIXED_CASE)
        assert self.dynamic_contols_page.get_inputed_text() == DynamicControlsData.INPUT_TEXT_MIXED_CASE

        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.DISABLE_BUTTON_TITLE
        self.dynamic_contols_page.click_on_btn(2)
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_disabled()
        assert self.dynamic_contols_page.get_inputed_text() == DynamicControlsData.INPUT_TEXT_MIXED_CASE
        assert self.dynamic_contols_page.get_btn_text(2) != DynamicControlsData.DISABLE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.ENABLE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_text_under_btn() !=  DynamicControlsData.TEXT_AFTER_ENABLE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_DISABLE

    def test_TC43_verify_checkbox_section_state_after_refresh(self):
        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.get_btn_text(1) != DynamicControlsData.REMOVE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_btn_text(1) == DynamicControlsData.ADD_BUTTON_TITLE
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_REMOVE
        
        with Reporter.step("Click the browser Refresh button"):
                self.driver.refresh()
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        assert self.dynamic_contols_page.is_btn_displayed(1) is True
        assert self.dynamic_contols_page.get_btn_text(1) == DynamicControlsData.REMOVE_BUTTON_TITLE 

        self.dynamic_contols_page.click_on_checkbox()
        assert self.dynamic_contols_page.is_checkbox_checked() is True

        self.dynamic_contols_page.click_on_remove_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.get_btn_text(1) != DynamicControlsData.REMOVE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_btn_text(1) == DynamicControlsData.ADD_BUTTON_TITLE 
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_REMOVE
        
        self.dynamic_contols_page.click_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        assert self.dynamic_contols_page.is_btn_displayed(1) is True
        assert self.dynamic_contols_page.get_btn_text(1) != DynamicControlsData.ADD_BUTTON_TITLE
        assert self.dynamic_contols_page.get_btn_text(1) == DynamicControlsData.REMOVE_BUTTON_TITLE
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_REMOVE 
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ADD 

        with Reporter.step("Click the browser Refresh button"):
                self.driver.refresh()
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        assert self.dynamic_contols_page.is_btn_displayed(1) is True
        assert self.dynamic_contols_page.get_btn_text(1) == DynamicControlsData.REMOVE_BUTTON_TITLE


    def test_TC44_verify_Iput_field_section_state_after_refresh(self):
        self.dynamic_contols_page.click_on_enable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_input_is_enabled() is True
        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) != DynamicControlsData.ENABLE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.DISABLE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ENABLE

        with Reporter.step("Click the browser Refresh button"):
                self.driver.refresh()
        assert self.dynamic_contols_page.is_input_field_enabeled() is DynamicControlsData.INITIAL_INPUT_STATE         
        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.ENABLE_BUTTON_TITLE 

        self.dynamic_contols_page.click_on_enable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_input_is_enabled() is True
        self.dynamic_contols_page.enter_to_input_field(DynamicControlsData.INPUT_TEXT_ALPHANUMERIC_SPECIAL_CHARS)
        assert self.dynamic_contols_page.get_inputed_text() == DynamicControlsData.INPUT_TEXT_ALPHANUMERIC_SPECIAL_CHARS

        self.dynamic_contols_page.click_on_btn(2)
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_disabled()
        assert self.dynamic_contols_page.get_inputed_text() == DynamicControlsData.INPUT_TEXT_ALPHANUMERIC_SPECIAL_CHARS
        assert self.dynamic_contols_page.get_btn_text(2) != DynamicControlsData.DISABLE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.ENABLE_BUTTON_TITLE 
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_ENABLE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_DISABLE    

        with Reporter.step("Click the browser Refresh button"):
                self.driver.refresh()
        assert self.dynamic_contols_page.is_input_field_enabeled() is DynamicControlsData.INITIAL_INPUT_STATE
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.ENABLE_BUTTON_TITLE

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
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.get_btn_text(1) != DynamicControlsData.REMOVE_BUTTON_TITLE 
        assert self.dynamic_contols_page.get_btn_text(1) == DynamicControlsData.ADD_BUTTON_TITLE        
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_REMOVE
# step 5
        self.dynamic_contols_page.focus_add_btn()
        assert self.dynamic_contols_page.is_add_btn_focused() is True
# step 6
        self.dynamic_contols_page.press_enter_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE
        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == DynamicControlsData.REMOVE_BUTTON_TITLE 
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_REMOVE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ADD
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
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_checkbox_absent_or_hidden() is True
        assert self.dynamic_contols_page.get_btn_text(1) != DynamicControlsData.REMOVE_BUTTON_TITLE         
        assert self.dynamic_contols_page.get_btn_text(1) == "Add"
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_REMOVE 
# step 9
        self.dynamic_contols_page.focus_add_btn()
        assert self.dynamic_contols_page.is_add_btn_focused() is True

        self.dynamic_contols_page.press_enter_on_add_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT 
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_displayed() is True
        assert self.dynamic_contols_page.is_checkbox_checked() is DynamicControlsData.INITIAL_CHECKBOX_STATE

        assert self.dynamic_contols_page.is_text_from_checkbox_displayed() is True
        assert self.dynamic_contols_page.get_text_from_place_where_was_checkbox() == DynamicControlsData.TEXT_FROM_PLACE_WHERE_WAS_CHECKBOX 
        assert self.dynamic_contols_page.get_amount_of_text_without_checkboxes() == 2   

        self.dynamic_contols_page.wait_until_add_btn_absent()
        assert self.dynamic_contols_page.is_add_btn_absent_or_hidden() is True
        assert self.dynamic_contols_page.is_remove_btn_displayed() is True
        assert self.dynamic_contols_page.get_rmv_btn_text() == DynamicControlsData.REMOVE_BUTTON_TITLE 
        assert self.dynamic_contols_page.is_text_displayed_under_button() is True
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_REMOVE 
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_ADD

    def test_TC46_navigate_select_and_change_input_field_section_state_using_keyboard(self):
# step 1
        self.dynamic_contols_page.focus_enale_btn()
        assert self.dynamic_contols_page.is_enable_btn_focused() is True
# step 2
        self.dynamic_contols_page.press_enter_on_enable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT 
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        assert self.dynamic_contols_page.wait_until_input_is_enabled() is True
        assert self.dynamic_contols_page.is_btn_displayed(2) is True
        assert self.dynamic_contols_page.get_btn_text(2) != DynamicControlsData.ENABLE_BUTTON_TITLE
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.DISABLE_BUTTON_TITLE         
        assert self.dynamic_contols_page.get_text_under_btn() == "It's enabled!"
# step 3
        self.dynamic_contols_page.focus_input_field()
        assert self.dynamic_contols_page.is_input_filed_focused()
# step 4
        self.dynamic_contols_page.enter_to_input_field(DynamicControlsData.INPUT_TEXT_SPECIAL_CHAR_AT_START)
        assert self.dynamic_contols_page.get_inputed_text() == DynamicControlsData.INPUT_TEXT_SPECIAL_CHAR_AT_START
# step 5
        self.dynamic_contols_page.focus_disable_btn()
        assert self.dynamic_contols_page.is_disable_btn_focused() is True
# step 6
        self.dynamic_contols_page.press_enter_on_disable_btn()
        assert self.dynamic_contols_page.is_wait_text_displayed() is True
        assert self.dynamic_contols_page.get_wait_text() == DynamicControlsData.WAIT_TEXT 
        assert self.dynamic_contols_page.is_progress_bar_displayed() is True
        self.dynamic_contols_page.wait_until_input_is_disabled()
        assert self.dynamic_contols_page.get_inputed_text() == DynamicControlsData.INPUT_TEXT_SPECIAL_CHAR_AT_START 
        assert self.dynamic_contols_page.get_btn_text(2) != DynamicControlsData.DISABLE_BUTTON_TITLE 
        assert self.dynamic_contols_page.get_btn_text(2) == DynamicControlsData.ENABLE_BUTTON_TITLE 
        assert self.dynamic_contols_page.get_text_under_btn() != DynamicControlsData.TEXT_AFTER_ENABLE
        assert self.dynamic_contols_page.get_text_under_btn() == DynamicControlsData.TEXT_AFTER_DISABLE


