class BrokenImagesData:

    URL_BROKEN_IMAGES_PAGE = "https://the-internet.herokuapp.com/broken_images"
    HEADER = "Broken Images"
    IMGS_AMOUNT = 3
    FOOTER = "Powered by Elemental Selenium"
    FOOTER_LINK = "Elemental Selenium"
    
    @staticmethod
    def WARNING(img_number):
        return f"The image #{img_number} has broken image indicator or missing image placeholder"
                       
