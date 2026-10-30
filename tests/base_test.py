from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pytest
from pages.home_page import HomePage


class BaseTest:
    pytestmark = pytest.mark.nondestructive

    @pytest.fixture(autouse=True)    
    def setup_test(self, request, base_url):
        # print(f"==========-=========The {request.node.nodeid} is started==========-=========")
        options = Options()
        options.add_argument("--incognito")
        if os.environ.get("GITHUB_ACTIONS") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        self.base_url = base_url
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(810, 1080)
        self.home_page = HomePage(self.driver)
        self.driver.get(self.base_url)

        yield
        self.driver.quit()