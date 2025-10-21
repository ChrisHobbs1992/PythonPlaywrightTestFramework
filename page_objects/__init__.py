from page_objects.home_page import HomePage
from page_objects.product_directory_page import ProductDirectoryPage
from page_objects.our_digital_services_page import OurDigitalServicesPage
from page_objects.nhs_wales_app_help_and_support_page import NhsWalesAppHelpSupportPage
from page_objects.search_results_page import SearchResultPage
from page_objects.about_us_page import AboutUsPage

#Add pages to your init file to automatically be able to call them in the test files using the following code

'''
from pages.__init__ import Pages

@pytest.fixture
def pages(page): 
    return Pages(page)

'''

class Pages:
    def __init__(self, page):
        self.page = page
        self.home = HomePage(page)
        self.product_directory = ProductDirectoryPage(page)
        self.our_digital_services = OurDigitalServicesPage(page)
        self.nhs_wales_app_help_support = NhsWalesAppHelpSupportPage(page)
        self.search_results = SearchResultPage(page)
        self.about_us = AboutUsPage(page)