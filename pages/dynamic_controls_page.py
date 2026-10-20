from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DynamicControlsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.locators = {
            "header" : (By.XPATH, "//h4[1]"),
            "paragraph" : (By.TAG_NAME, "p"),
            "remove_add_subheader" : (By.XPATH, "//h4[text()='Remove/add']"),
            "checkbox" : (By.ID, "checkbox"),
            "remove_btn" : (By.XPATH, "//button[text()='Remove']"),
            "enabel_disable_subheader" : (By.XPATH, "//h4[text()='Enable/disable']"),
            "input" : (By.XPATH, "//input[@type='text']"),
            "enable_btn" : (By.XPATH, "//button[text()='Enable']"),
            "footer" : (By.XPATH, "//div[@style='text-align: center;']"),
            "selenium" : (By.LINK_TEXT, "Elemental Selenium"),
            "sauce_labs" : (By.LINK_TEXT, "Sauce Labs")
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
        checkboxes_el = self.driver.find_elements(*self.locators["checkbox"])
        return len(checkboxes_el)

    def is_checkbox_displayed(self):
        checkbox_el = self.driver.find_element(*self.locators["checkbox"])
        return checkbox_el.is_displayed()
    
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
