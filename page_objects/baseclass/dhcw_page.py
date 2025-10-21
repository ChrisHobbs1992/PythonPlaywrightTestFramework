from playwright.sync_api import expect
from datetime import datetime

#The wrapper class forming the base of each page in the framework

class DHCWPage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator_or_element):
    # If target is a Playwright Locator, click it
        if hasattr(locator_or_element, "click"):
            locator_or_element.click()
        else:
            # if it is a selector string, then find it, then click it
            self.page.locator(locator_or_element).click()

    def click_and_switch_to_new_tab(self, locator_or_element):
        with self.page.context.expect_page() as new_page_info:
            if hasattr(locator_or_element, "click"):
                locator_or_element.click()
            else:
                self.page.locator(locator_or_element).click()
        new_page = new_page_info.value
        new_page.wait_for_load_state("load")
        return new_page

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
    
    #Examples of expansions

    def assert_option_is_checked(self,selector):
        expect(selector).to_be_checked()

    def take_screenshot(self, page):
        date = "{:%B %d, %Y}".format(datetime.now())
        page.screenshot(path="screenshot" + date + ".png")

    def take_screenshot_of_element(self, locator, file_name):
        date = "{:%B %d, %Y}".format(datetime.now())
        self.page.locator(locator).screenshot(path= file_name +"screenshot" + date + ".png")