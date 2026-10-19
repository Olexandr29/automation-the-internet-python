from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DynamicControlsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.locators = {
            "header" : (By.XPATH, "//h4[1]"),
            "paragraph" : (By.TAG_NAME, "p"),
            "remove_add_subheader" : (By.XPATH, "//h4[text()='Remove/add']"),
            "checkbox" : (By.XPATH, "//input[@type='checkbox']")

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

    
