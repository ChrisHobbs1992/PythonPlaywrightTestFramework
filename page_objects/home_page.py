from page_objects.baseclass.dhcw_page import DHCWPage
from page_objects.partial.upper_ribbon_page import UpperRibbonPage

class HomePage(DHCWPage):
    def __init__(self, page):
        super().__init__(page)
        self.upperribbon = UpperRibbonPage(page)
        self.slogan = page.get_by_role("heading", name="Making digital a force for")
    
    def assert_slogan_present(self):
        self.assert_element_contains_text(self.slogan, "Making digital a force for good in health and care")