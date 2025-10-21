from page_objects.baseclass.dhcw_page import DHCWPage
from page_objects.partial.upper_ribbon_page import UpperRibbonPage

class NhsWalesAppHelpSupportPage(DHCWPage):
    def __init__(self, page):
        super().__init__(page)
        self.upperribbon = UpperRibbonPage(page)
        self.heading = (page.get_by_role("strong").filter(has_text="NHS Wales App: Help and support"))

    def assert_heading_is_present(self):
        self.assert_element_contains_text(self.heading, "NHS Wales App: Help and support")