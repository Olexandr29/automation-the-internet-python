class BrokenImagesData:

    URL_BROKEN_IMAGES_PAGE = "https://the-internet.herokuapp.com/broken_images"
    HEADER = "Broken Images"
    IMGS_AMOUNT = 3
    FOOTER = "Powered by Elemental Selenium and Sauce Labs"
    FOOTER_LINK_SELENIUM = "Elemental Selenium"
    FOOTER_LINK_SAUCE_LABS = "Sauce Labs"

    
    @staticmethod
    def WARNING(img_number):
        return f"The image #{img_number} has broken image indicator or missing image placeholder"
