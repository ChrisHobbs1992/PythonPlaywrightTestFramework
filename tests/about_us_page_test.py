import pytest
from page_objects.__init__ import Pages

@pytest.fixture
def pages(page): 
    return Pages(page)

def test_images_have_alt_text(pages):
    pages.about_us.goto("https://dhcw.nhs.wales/about-us")
    pages.about_us.assert_all_images_have_alt_text()