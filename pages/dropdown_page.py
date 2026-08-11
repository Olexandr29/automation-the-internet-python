from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class DropdownPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.locators = {
            "dropdownLocator" : (By.ID, "dropdown"),

        }

    def open_dropdown(self):
        self.click(self.locators["dropdownLocator"])

    def is_dropdown_visible(self):
        return self.is_visible(self.locators["dropdownLocator"])

    def get_selected_option_text(self):
        dropdown = Select(self.find(self.locators["dropdownLocator"]))
        return dropdown.first_selected_option.text

    def get_available_options(self):
        dropdown = Select(self.find(self.locators["dropdownLocator"]))
        available_options = []
        for option in dropdown.options:
            available_options.append(option.text)
        return available_options

    def are_expected_options_displayed(self, expected_options):
        result = self.get_available_options() == expected_options
        return result

    def select_option(self, specific_option):
        dropdown = Select(self.find(self.locators["dropdownLocator"]))
        return dropdown.select_by_visible_text(specific_option)

    def press_escape(self):
        return self.press_key(self.locators["dropdownLocator"], Keys.ESCAPE)

    def focus_dropdown(self):
        actions = ActionChains(self.driver)
        dropdown = self.find(self.locators["dropdownLocator"])
        for _ in range(10):
            active_element = self.driver.switch_to.active_element
            if active_element == dropdown:
                return
            actions.send_keys(Keys.TAB).perform()

    def is_dropdown_focused(self):
        focused = self.driver.switch_to.active_element
        dropdown = self.find(self.locators["dropdownLocator"])
        return focused == dropdown

    def press_arrow_down(self):
        return self.press_key(self.locators["dropdownLocator"], Keys.ARROW_DOWN)

    def press_enter(self):
        return self.press_key(self.locators['dropdownLocator'], Keys.ENTER)

    def press_arrow_up(self):
        return self.press_key(self.locators["dropdownLocator"], Keys.ARROW_UP)

    
    