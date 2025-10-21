import pytest
from page_objects.__init__ import Pages

@pytest.fixture
def pages(page): 
    return Pages(page)

def test_hospital_and_clinic_link_present(pages):
    pages.home.goto("https://dhcw.nhs.wales")
    pages.home.upperribbon.click_navigation_option("Product directory")
    pages.product_directory.assert_product_directory_header_is_present()
    pages.product_directory.assert_hospital_clinic_link_present()