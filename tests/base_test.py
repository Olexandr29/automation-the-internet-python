from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pytest
from pages.home_page import HomePage


class BaseTest:
 
    @pytest.fixture(autouse=True)    
    def setup_test(self, request):
        # print(f"==========-=========The {request.node.nodeid} is started==========-=========")
        options = Options()
        options.add_argument("--incognito")
        if os.environ.get("GITHUB_ACTIONS") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.home_page = HomePage(self.driver)
        self.driver.get(self.home_page.URL)

        yield
        self.driver.quit()