from page_objects.baseclass.dhcw_page import DHCWPage
from playwright.sync_api import expect
from page_objects.partial.upper_ribbon_page import UpperRibbonPage

class AboutUsPage(DHCWPage):
    def __init__(self, page):
        super().__init__(page)
        self.upperribbon = UpperRibbonPage(page)
        self.rhidian_hurle_image = page.get_by_alt_text("Rhidian Hurle using a laptop.")
        self.mobile_phone_image = page.get_by_alt_text("Mobile phone displaying NHS Wales App.")
    
    def assert_all_images_have_alt_text(self):
        self.assert_element_is_visible(self.rhidian_hurle_image)
        self.assert_element_is_visible(self.mobile_phone_image)