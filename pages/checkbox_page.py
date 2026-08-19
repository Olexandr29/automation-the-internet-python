from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CheckboxPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.locators = {
            # "checkboxes": (By.ID, "checkboxes")
            "checkboxes": (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
        }

    def is_checkbox_visible(self, checkbox_number):
        checkboxes = self.driver.find_elements(*self.locators["checkboxes"])
        if checkbox_number > len(checkboxes):
            return False
        return checkboxes[checkbox_number - 1].is_displayed()

    def is_checkbox_checked(self, checkbox_number):
        checkboxes = self.driver.find_elements(*self.locators["checkboxes"])
        return checkboxes[checkbox_number - 1].is_selected()

    def check_specific_checkbox(self, checkbox_number):
        checkboxes = self.driver.find_elements(*self.locators["checkboxes"])
        return checkboxes[checkbox_number - 1].click()

    # @Reporter.step("Focus the checkbox")
    def focus_checkbox(self, checkbox_number):
        actions = ActionChains(self.driver)
        checkboxes = self.driver.find_elements(*self.locators["checkboxes"])
        target_checkbox = checkboxes[checkbox_number - 1]

        for _ in range(10):
            active_element = self.driver.switch_to.active_element
            if active_element == target_checkbox:
                return 
            actions.send_keys(Keys.TAB).perform()
   
    def is_checkbox_focused(self, checkbox_number):
        focused = self.driver.switch_to.active_element
        checkboxes = self.driver.find_elements(*self.locators["checkboxes"])
        return focused == checkboxes[checkbox_number - 1]

    def press_space(self, checkbox_number):
        checkboxes = self.driver.find_elements(*self.locators["checkboxes"])
        checkboxes[checkbox_number - 1].send_keys(Keys.SPACE)

        
       