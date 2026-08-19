from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils.reporter import Reporter

class DropdownPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.locators = {
            "dropdownLocator" : (By.ID, "dropdown"),
        }

    def open_dropdown(self):
        with Reporter.step("Open Dropdown"):
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

    @Reporter.step("Observe all available options")
    def are_expected_options_displayed(self, expected_options):
            result = self.get_available_options() == expected_options
            return result

    def select_option(self, specific_option):
        with Reporter.step(f"Select: '{specific_option}' from dropdown"):
            dropdown = Select(self.find(self.locators["dropdownLocator"]))
        return dropdown.select_by_visible_text(specific_option)

    def press_escape(self):
            return self.press_key(self.locators["dropdownLocator"], Keys.ESCAPE)

    @Reporter.step("Focus the dropdown")
    def focus_dropdown(self):
        dropdown = self.find(self.locators["dropdownLocator"])
        return self.focus_element(dropdown)
    
    def is_dropdown_focused(self):
        dropdown = self.find(self.locators["dropdownLocator"])
        return self.is_element_focused(dropdown)

    def press_arrow_down(self):
        return self.press_key(self.locators["dropdownLocator"], Keys.ARROW_DOWN)

    def press_enter(self):
        return self.press_key(self.locators['dropdownLocator'], Keys.ENTER)

    def press_arrow_up(self):
        return self.press_key(self.locators["dropdownLocator"], Keys.ARROW_UP)

    
    