from tests.base_test import BaseTest, pytest
from pages.broken_images_page import BrokenImagesPage
import pytest_check as check
from test_data.broken_images_data import BrokenImagesData
import allure
from utils.reporter import Reporter

@allure.feature("Broken_Images")
@pytest.mark.regression
class TestBrokenImages(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_broken_images_page(self, setup_test):
        with Reporter.step("Open Broken images page"):
            self.broken_images_page = self.home_page.open_broken_images_page()

    def test_TC36_verify_page_content(self):
        assert self.driver.current_url == BrokenImagesData.URL_BROKEN_IMAGES_PAGE, f"The Broken Images page is not loaded successfully, current page is {self.driver.current_url}"
        assert self.broken_images_page.get_document_ready_state() == "complete", f"The document readyState is not 'complete', but now the state is {self.broken_images_page.get_document_ready_state()}"
        assert self.broken_images_page.is_header_displayed() is True, f"The '{BrokenImagesData.HEADER}' header is not displayed"
        assert self.broken_images_page.get_header_text() == BrokenImagesData.HEADER, f"The header text is not '{BrokenImagesData.HEADER}' but equal {self.broken_images_page.get_header_text}"
        with Reporter.step(self.broken_images_page.text_for_steps("Images")):
            assert self.broken_images_page.get_imgs_amount() == BrokenImagesData.IMGS_AMOUNT, f"{BrokenImagesData.IMGS_AMOUNT} image elements are not displayed, but found = {self.broken_images_page.get_imgs_amount()}"
        assert self.broken_images_page.is_footer_displayed() is True, "The footer is not displayed"
        assert self.broken_images_page.get_footer_text() == BrokenImagesData.FOOTER, f"The footer text is not '{BrokenImagesData.FOOTER}' but equal {self.broken_images_page.get_footer_text()}"
        assert self.broken_images_page.is_footer_link_displayed() is True, "The footer link is not displayed"
        assert self.broken_images_page.get_footer_link_text() == BrokenImagesData.FOOTER_LINK, f"The link text is not '{BrokenImagesData.FOOTER_LINK}' but equal {self.broken_images_page.get_footer_link_text}"

    @pytest.mark.smoke
    def test_TC37_verify_image_loading(self):
        check.is_true(self.broken_images_page.is_img_loaded(1), BrokenImagesData.WARNING(1))
        check.is_true(self.broken_images_page.is_img_loaded(2), BrokenImagesData.WARNING(2))
        check.is_true(self.broken_images_page.is_img_loaded(3), BrokenImagesData.WARNING(3))
