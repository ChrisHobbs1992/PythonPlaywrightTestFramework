#Contains all locators and methods for using the upper nav ribbon to get around the site, the logo and the search bar

import playwright
from page_objects.baseclass.dhcw_page import DHCWPage

#Class inherits the base class - DHCWPage
class UpperRibbonPage(DHCWPage):
    def __init__(self, page):
        #Python's super class calls the parent classes constructor - in this case DHCWPage
        super().__init__(page)
        #Here are the locators - note the preferred playwright standard of using name
        #If you use the playwright inspector you can hover over the elements on the page to see their role and name
        #DHCW Button and search bar
        self.DHCW_logo = page.get_by_role("link", name="NHS Wales | Digital Health")
        self.search_filter = page.locator("#searchFilter")
        self.search_textbox = page.get_by_role("textbox", name="Search for")
        self.search_button = page.get_by_role("button", name="Search")
        self.cymraeg_button = page.get_by_role("link", name="Cymraeg")
        ##Menu Items
        self.home_button = page.get_by_role("menuItem", name="Home")
        self.product_directory_button = page.get_by_role("menuItem", name="Product directory", exact="true")
        self.our_digital_services_button = page.get_by_role("menuItem", name="Our Digital Services")
        self.digital_tools_for_clinical_staff_button = page.get_by_role("menuItem", name="Digital tools for clinical staff")
        self.digital_healthcare_in_your_community_button = page.get_by_role("menuItem", name="Digital healthcare in your community")

    def click_navigation_option(self, option):
        match option:
            case "Home":
                self.home_button.click()
            case "Product directory":
                self.product_directory_button.click()
            case "Our Digital Services":
                self.product_directory_button.hover()
                self.our_digital_services_button.click()
            case "Digital tools for clinical staff":
                self.product_directory_button.hover()
                self.digital_tools_for_clinical_staff_button.click()
            case "Digital healthcare in your community":
                self.product_directory_button.hover()
                self.digital_healthcare_in_your_community_button.click()
            case _: raise ValueError('The option is either unknown, or does not exist')


    def search_for_search_term(self, search_terms):
        self.search_textbox.fill(search_terms)
        self.search_button.click()