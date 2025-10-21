import pytest
from page_objects.__init__ import Pages

@pytest.fixture
def pages(page): 
    return Pages(page)

def test_search_results(pages):
    pages.home.goto("https://dhcw.nhs.wales")
    pages.home.upperribbon.search_for_search_term("WIS")
    pages.search_results.assert_heading_is_visible()
    pages.search_results.assert_result_is_present("Welsh Immunisation System reaches 7 million vaccination milestone")
