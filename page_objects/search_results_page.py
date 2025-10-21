from page_objects.baseclass.dhcw_page import DHCWPage
from page_objects.partial.upper_ribbon_page import UpperRibbonPage
from playwright.sync_api import expect

class SearchResultPage(DHCWPage):
    def __init__(self, page):
        super().__init__(page)
        self.upperribbon = UpperRibbonPage(page)
        self.heading = page.get_by_role("heading", name="Search Results")

    def assert_result_is_present(self, result_text):
        expect(self.get_by_role_filter_by_text("link", result_text)).to_be_visible()

    def assert_heading_is_visible(self):
        self.assert_element_is_visible(self.heading)

