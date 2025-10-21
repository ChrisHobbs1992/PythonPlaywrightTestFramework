from playwright.sync_api import expect
from datetime import datetime

#The wrapper class forming the base of each page in the framework

class DHCWPage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, target):
    # If target is a Playwright Locator, click it
        if hasattr(target, "click"):
            target.click()
        else:
            # if it is a selector string, then find it, then click it
            self.page.locator(target).click()

    def click_and_switch_to_new_tab(self, locator):
        with self.page.context.expect_page() as new_page_info:
            if hasattr(locator, "click"):
                locator.click()
            else:
                self.page.locator(locator).click()
        new_page = new_page_info.value
        new_page.wait_for_load_state("load")
        return new_page
    
    def take_screenshot(self, page):
        date = "{:%B %d, %Y}".format(datetime.now())
        page.screenshot(path="screenshot" + date + ".png")

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)

    def get_text(self, selector):
        return self.page.locator(selector).inner_text()
        
    def assert_element_is_visible(self, selector):
        expect(selector).to_be_visible()

    def assert_element_is_hidden(self, selector):
        expect(selector).to_be_hidden()

    def assert_element_contains_text(self, selector, text):
        expect(selector).to_contain_text(text)

    #This could do with some thought - how will you manage all of these longer term?
    #For now this is only for search results so makes sense.
    def get_by_role_filter_by_text(self, role, expected_text):
        return self.page.get_by_role(role).filter(has_text=expected_text)