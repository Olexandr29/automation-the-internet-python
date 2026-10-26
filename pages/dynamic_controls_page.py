from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class DynamicControlsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.locators = {
            "header" : (By.XPATH, "//h4[1]"),
            "paragraph" : (By.TAG_NAME, "p"),
            "remove_add_subheader" : (By.XPATH, "//h4[text()='Remove/add']"),
            "checkbox" : (By.ID, "checkbox"),
            "check_box" : (By.XPATH, "//input[@type='checkbox']"),
            "remove_btn" : (By.XPATH, "//button[text()='Remove']"),
            "add_btn" : (By.XPATH, "//button[text()='Add']"),
            "text_under_btn" : (By.XPATH, "//p[@id='message']"),
            "enabel_disable_subheader" : (By.XPATH, "//h4[text()='Enable/disable']"),
            "input" : (By.XPATH, "//input[@type='text']"),
            "enable_btn" : (By.XPATH, "//button[text()='Enable']"),
            "disable_btn" : (By.XPATH, "//button[text()='Disable']"),
            "footer" : (By.XPATH, "//div[@style='text-align: center;']"),
            "selenium" : (By.LINK_TEXT, "Elemental Selenium"),
            "sauce_labs" : (By.LINK_TEXT, "Sauce Labs"),
            "loading" : (By.XPATH, "//div[@id='loading']"),
            "progress_bar" : (By.XPATH, "//img[@src='/img/ajax-loader.gif']"),
            "just_txt_of_checkbox" : (By.XPATH, "//div[text()=' A checkbox']"),
            "btn" : (By.TAG_NAME, "button")
        }

    def get_document_ready_state(self):
        ready_state = self.driver.execute_script("return document.readyState")
        return ready_state

    def is_header_displayed(self):
        header_element = self.driver.find_element(*self.locators["header"])
        return header_element.is_displayed()

    def get_header_text(self):
        return self.get_text(self.locators["header"])

    def is_paragraph_displayed(self):
        paragraph_element = self.driver.find_element(*self.locators["paragraph"])
        return paragraph_element.is_displayed()

    def get_paragraph_text(self):
        return self.get_text(self.locators["paragraph"])

    def is_subheader_remove_add_displayed(self):
        subheader_el = self.driver.find_element(*self.locators["remove_add_subheader"])
        return subheader_el.is_displayed()

    def get_subheader_remove_add_text(self):
        return self.get_text(self.locators["remove_add_subheader"])

    def get_amount_of_checkboxes(self):
        checkboxes_el = self.driver.find_elements(*self.locators["check_box"])
        checkbox_length = len(checkboxes_el)
        print("checkbox_length =", checkbox_length)
        return checkbox_length
    
    def is_checkbox_displayed(self):
        return self.is_visible(self.locators["checkbox"])
    
    def get_checkbox_text(self):
        return self.get_text(self.locators["checkbox"])

    def is_remove_btn_displayed(self):
        remove_el = self.driver.find_element(*self.locators["remove_btn"])
        return remove_el.is_displayed()

    def get_rmv_btn_text(self):
        return self.get_text(self.locators["remove_btn"])

    def is_subheader_enabel_disable_displayed(self):
        subheader_el = self.driver.find_element(*self.locators["enabel_disable_subheader"])
        return subheader_el.is_displayed()
    
    def get_subheader_enabel_disable_text(self):
        return self.get_text(self.locators["enabel_disable_subheader"])

    def is_input_displayed(self):
        return self.is_visible(self.locators["input"])

    def is_enable_btn_displayed(self):
        return self.is_visible(self.locators["enable_btn"])

    def get_enable_btn_text(self):
        return self.get_text(self.locators["enable_btn"])
    
    def is_footer_displayed(self):
        return self.is_visible(self.locators["footer"])

    def get_footer_text(self):
        return self.get_text(self.locators["footer"])

    def is_elemental_selenium_link_displayed(self):
        return self.is_visible(self.locators["selenium"])

    def is_sauce_labs_link_displayed(self):
        return self.is_visible(self.locators["sauce_labs"])

    def is_checkbox_checked(self):
        checkbox_el = self.find(self.locators["check_box"])
        return checkbox_el.is_selected()

    def click_on_checkbox(self):
        return self.click(self.locators["check_box"])

    def click_on_remove_btn(self):
        return self.click(self.locators["remove_btn"])

    def is_wait_text_displayed(self):
        return self.is_visible(self.locators["loading"])

    def get_wait_text(self):
        return self.get_text(self.locators["loading"])

    def is_progress_bar_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators["progress_bar"])
            ).is_displayed()

    def wait_until_checkbox_absent(self):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.locators["check_box"]))

    def is_checkbox_absent_or_hidden(self):
        checkbox_elements = self.driver.find_elements(*self.locators["check_box"])
        return len(checkbox_elements) == 0 or not checkbox_elements[0].is_displayed()

    def wait_until_remove_btn_absent(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.locators["remove_btn"])
        )
    
    def is_remove_btn_absent_or_hidden(self):
        remove_btn_elements = self.driver.find_elements(*self.locators["remove_btn"])
        return len(remove_btn_elements) == 0 or not remove_btn_elements[0].is_displayed()

    def is_add_btn_displayed(self):
        add_btn_element = self.driver.find_element(*self.locators["add_btn"])
        return add_btn_element.is_displayed()

    def get_add_btn_text(self):
        return self.get_text(self.locators["add_btn"])

    def is_text_displayed_under_button(self):
        return self.is_visible(self.locators["text_under_btn"])

    def get_text_under_btn(self):
        return self.get_text(self.locators["text_under_btn"])

    def click_on_add_btn(self):
        return self.click(self.locators["add_btn"])

    def wait_until_add_btn_absent(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.locators["add_btn"])
            )
    
    def is_add_btn_absent_or_hidden(self):
        add_btn_elements = self.driver.find_elements(*self.locators["add_btn"])
        return len(add_btn_elements) == 0 or not add_btn_elements[0].is_displayed()
    
    
    def wait_until_text_its_gone_absent(self):
        return WebDriverWait(self.driver, 10).until(
        EC.invisibility_of_element_located(self.locators["text_under_btn"])
                )

    def is_text_its_gone_absent_or_hidden(self):
        text_its_gone_elements = self.driver.find_elements(*self.locators["text_under_btn"])
        return len(text_its_gone_elements) == 0 or not text_its_gone_elements[0].is_displayed()

    def is_text_from_checkbox_displayed(self):
        return self.is_visible(self.locators["just_txt_of_checkbox"])

    def get_text_from_place_where_was_checkbox(self):
        return self.get_text(self.locators["just_txt_of_checkbox"])

    def get_amount_of_text_without_checkboxes(self):
        text_without_checkboxes_el = self.driver.find_elements(*self.locators["just_txt_of_checkbox"])
        length = len(text_without_checkboxes_el)
        print("length =", length)
        return length

    def is_input_field_enabeled(self):
        return self.find(self.locators["input"]).is_enabled()

    def click_on_enable_btn(self):
        return self.click(self.locators["enable_btn"])

    def wait_until_enable_btn_absent(self):
            return WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.locators["enable_btn"])
                )

    def is_btn_displayed(self, button_number):
        return self.find_element_by_number(self.locators["btn"], button_number).is_displayed()

    def get_btn_text(self, button_number):
        target_btn = self.find_element_by_number(self.locators["btn"], button_number)
        return target_btn.text
    
    def wait_until_input_is_clickable(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators["input"]))

    def enter_to_input_field(self, text):
        return self.type(self.locators["input"], text)

    def get_inputed_text(self):
        input_webelement = self.find(self.locators["input"])
        attribute_txt = input_webelement.get_attribute("value")
        print("attribute_txt =", attribute_txt)
        return attribute_txt

    def click_on_btn(self, button_number):
        btn_webelement = self.find_element_by_number(self.locators["btn"], button_number)
        return btn_webelement.click()
    
    def wait_until_input_is_disabled(self):
        return WebDriverWait(self.driver, 10).until(
                    EC.all_of(EC.element_attribute_to_include(self.locators["input"], 'disabled')
                    ))

    def focus_checkbox(self):
        target_webelement = self.find(self.locators["check_box"])
        return self.focus_element(target_webelement)

    def is_checkbox_focused(self):
        target_webelement = self.find(self.locators["check_box"])
        return self.is_element_focused(target_webelement)

    def press_space(self):
        webelement = self.find(self.locators["check_box"])
        return self.press_key_on_element(webelement, Keys.SPACE)

    def focus_remove_btn(self):
        target_webelement = self.find(self.locators["remove_btn"])
        return self.focus_element(target_webelement)

    def is_remove_btn_focused(self):
        target_webelement = self.find(self.locators["remove_btn"])
        return self.is_element_focused(target_webelement)

    def press_enter(self):
        target_webelement = self.find(self.locators["remove_btn"])
        return self.press_key_on_element(target_webelement, Keys.ENTER)

    def focus_add_btn(self):
        target_webelement = self.find(self.locators["add_btn"])
        return self.focus_element(target_webelement)
    
    def is_add_btn_focused(self):
        target_webelement = self.find(self.locators["add_btn"])
        return self.is_element_focused(target_webelement)
    
    def press_enter_on_add_btn(self):
        target_webelement = self.find(self.locators["add_btn"])
        return self.press_key_on_element(target_webelement, Keys.ENTER)

    def focus_enale_btn(self):
        target_webelement = self.find(self.locators["enable_btn"])
        return self.focus_element(target_webelement)
        
    def is_enable_btn_focused(self):
        target_webelement = self.find(self.locators["enable_btn"])
        return self.is_element_focused(target_webelement)
        
    def press_enter_on_enable_btn(self):
        target_webelement = self.find(self.locators["enable_btn"])
        return self.press_key_on_element(target_webelement, Keys.ENTER)

    def focus_input_field(self):
        target_webelement = self.find(self.locators["input"])
        return self.focus_element(target_webelement)
            
    def is_input_filed_focused(self):
        target_webelement = self.find(self.locators["input"])
        return self.is_element_focused(target_webelement)

    def focus_disable_btn(self):
        target_webelement = self.find(self.locators["disable_btn"])
        return self.focus_element(target_webelement)
            
    def is_disable_btn_focused(self):
        target_webelement = self.find(self.locators["disable_btn"])
        return self.is_element_focused(target_webelement)
            
    def press_enter_on_disable_btn(self):
        target_webelement = self.find(self.locators["disable_btn"])
        return self.press_key_on_element(target_webelement, Keys.ENTER)
    


    