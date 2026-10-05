from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class BrokenImagesPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.locators = {
            "header" : (By.TAG_NAME, "h3"),
            "imgs" : (By.XPATH, "//div[@class='example']//img"),
            "footer" : (By.XPATH, "//div[@style='text-align: center;']"),
            "footer_link" : (By.LINK_TEXT, "Elemental Selenium")
        }

    def get_document_ready_state(self):
        ready_state = self.driver.execute_script("return document.readyState")
        return ready_state 

    def is_header_displayed(self):
        header_element = self.driver.find_element(*self.locators["header"])
        return header_element.is_displayed()

    def get_header_text(self):
        header_element = self.driver.find_element(*self.locators["header"])
        return header_element.text

    def get_imgs_amount(self):
        img_elements = self.driver.find_elements(*self.locators["imgs"])
        return len(img_elements)

    def is_footer_displayed(self):
        footer_element = self.driver.find_element(*self.locators["footer"])
        return footer_element.is_displayed()
    
    def get_footer_text(self):
        footer_element = self.driver.find_element(*self.locators["footer"])
        return footer_element.text

    def is_footer_link_displayed(self):
        footer_link_element = self.driver.find_element(*self.locators["footer_link"])
        return footer_link_element.is_displayed()

    def get_footer_link_text(self):
        footer_link_element = self.driver.find_element(*self.locators["footer_link"])
        return footer_link_element.text

    
