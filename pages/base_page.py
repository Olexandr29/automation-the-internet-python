from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from utils.reporter import Reporter
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_element_by_number(self, locator, number):
        elements = self.find_elements(locator)
        return elements[number - 1]

    def click(self, locator):
        element = self.find(locator)
        element.click()
        return element
    
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find(locator)
        return element.text
    
    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False

    def get_key_name(self, key):
        for name, value in vars(Keys).items():
            if value == key:
                return name
        return key

    def press_key(self, locator, specific_key):
        key_name = self.get_key_name(specific_key)
        with Reporter.step(f'Press {key_name} key'):
            element = self.find(locator);
            element.send_keys(specific_key)

    def press_key_on_element(self, element, specific_key):
            key_name = self.get_key_name(specific_key)
            with Reporter.step(f'Press {key_name} key'):
                element.send_keys(specific_key)        

    def focus_element(self, element):
        actions = ActionChains(self.driver)   
        for _ in range(10):
            active_element = self.driver.switch_to.active_element
            if active_element == element:
                    return 
            
            actions.send_keys(Keys.TAB).perform()  

    def is_element_focused(self, element):
        return self.driver.switch_to.active_element == element      