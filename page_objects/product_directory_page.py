from page_objects.baseclass.dhcw_page import DHCWPage
from page_objects.partial.upper_ribbon_page import UpperRibbonPage

class ProductDirectoryPage(DHCWPage):
    def __init__(self, page):
        super().__init__(page)
        self.upperribbon = UpperRibbonPage(page)
        self.product_directory_heading = page.get_by_role("heading", name="Product directory")
        #self.hospitals_and_clinics_link = page.get_by_role("link", name="Hospitals and clinics ▯")
        self.hospitals_and_clinics_link = (page.get_by_role("link").filter(has_text="Hospitals and clinics"))
        self.gp_and_community_care_link = (page.get_by_role("link").filter(has_text="GP and community care"))
        self.medicines_and_pharmacy_link = (page.get_by_role("link").filter(has_text="Medicines and pharmacy"))
        self.the_nhs_wales_app_link = (page.get_by_role("link").filter(has_text="The NHS Wales App"))
        self.urgent_and_emergency_care_link = (page.get_by_role("link").filter(has_text="Urgent and Emergency Care"))
        self.diagnostics_department_link = (page.get_by_role("link").filter(has_text="Diagnostics Departments"))


    def assert_hospital_clinic_link_present(self):
        self.assert_element_contains_text(self.hospitals_and_clinics_link, "Hospitals and clinics")

    def assert_product_directory_header_is_present(self):
        self.assert_element_contains_text(self.product_directory_heading, "Product directory")

    def click_digital_service_category(self, category_name):
        element_to_click = self.get_category_link_by_name(category_name)
        new_tab = self.click_and_switch_to_new_tab(element_to_click)
        return new_tab
    
    def assert_digital_service_category_link_is_visible(self, category_name):
        element_to_check = self.get_category_link_by_name(category_name)
        self.assert_element_is_visible(element_to_check)

    def get_category_link_by_name(self, category_name):
        match(category_name):
            case "Hospitals and clinics":
                element = self.hospitals_and_clinics_link
            case "GP and community care":
                element = self.gp_and_community_care_link
            case "Medicines and pharmacy":
                element=self.medicines_and_pharmacy_link
            case "The NHS Wales App":
                element=self.the_nhs_wales_app_link
            case "Urgent and Emergency Care":
                element=self.urgent_and_emergency_care_link
            case "Diagnostics Departments":
                element=self.diagnostics_department_link
        #catch error if the name is wrong
        if not element:
            raise NotImplementedError("element provided is not coded, check for typos or implement the new option")

        return element