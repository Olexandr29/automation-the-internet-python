from tests.base_test import BaseTest, pytest
from pages.broken_images_page import BrokenImagesPage

class TestBrokenImages(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_broken_images_page(self, setup_test):
        self.broken_images_page = self.home_page.open_broken_images_page()

    def test_TC36_verify_page_content(self):
        assert self.driver.current_url == "https://the-internet.herokuapp.com/broken_images", f"The Broken Images page is not loaded successfully, current page is {self.driver.current_url}"
        assert self.broken_images_page.get_document_ready_state() == "complete", f"The document readyState is not 'complete', but now the state is {self.broken_images_page.get_document_ready_state()}"
        assert self.broken_images_page.is_header_displayed() is True, "The 'Broken Images' header is not displayed"
        assert self.broken_images_page.get_header_text() == "Broken Images", f"The header text is not 'Broken Images' but equal {self.broken_images_page.get_header_text}"
        assert self.broken_images_page.get_imgs_amount() == 3, f"Three elements are not displayed, but found = {self.broken_images_page.get_imgs_amount()}"
        assert self.broken_images_page.is_footer_displayed() is True, "The footer is not displayed"
        assert self.broken_images_page.get_footer_text() == "Powered by Elemental Selenium", f"The footer text is not 'Powered by Elemental Selenium' but equal {self.broken_images_page.get_footer_text()}"
        assert self.broken_images_page.is_footer_link_displayed() is True, "The footer link is not displayed"
        assert self.broken_images_page.get_footer_link_text() == "Elemental Selenium", f"The link text is not 'Elemental Selenium' but equal {self.broken_images_page.get_footer_link_text}"
