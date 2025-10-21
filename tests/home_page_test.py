import pytest
from page_objects.__init__ import Pages

@pytest.fixture
def pages(page): 
    return Pages(page)

def test_slogan_present(pages):
    pages.home.goto("https://dhcw.nhs.wales")
    pages.home.assert_slogan_present()