import pytest
from page_objects.__init__ import Pages

@pytest.fixture
def pages(page): 
    return Pages(page)

# To run tests run: $ python -m venv venv
# Then you can activeate the venv using $ source venv/Scripts/activate
# This will enable reporting

def test_example(page):
    page.goto("https://dhcw.nhs.wales")
    title = page.title()
    slogan = page.get_by_role("heading", name="Making digital a force for").inner_text()
    assert "Home - Digital Health and Care Wales" in title
    assert "Making digital a force for good in health and care" in slogan

def test_slogan_present(pages):
    pages.home.goto("https://dhcw.nhs.wales")
    pages.home.assert_slogan_present()

def test_hospital_and_clinic_link_present(pages):
    pages.home.goto("https://dhcw.nhs.wales")
    pages.home.upperribbon.click_navigation_option("Product directory")
    pages.product_directory.assert_product_directory_header_is_present()
    pages.product_directory.assert_hospital_clinic_link_present()

def test_our_digital_service_heading_present(pages):
    pages.home.goto("https://dhcw.nhs.wales")
    pages.home.upperribbon.click_navigation_option("Our Digital Services")
    pages.our_digital_services.assert_our_digital_services_heading_is_present()

