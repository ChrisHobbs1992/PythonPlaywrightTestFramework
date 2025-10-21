from page_objects.baseclass.dhcw_page import DHCWPage
from page_objects.partial.upper_ribbon_page import UpperRibbonPage

class OurDigitalServicesPage(DHCWPage):
    def __init__(self, page):
        super().__init__(page)
        self.upperribbon = UpperRibbonPage(page)
        self.our_digital_services_heading = page.get_by_role("heading", name="Our Digital Services")
        self.child_health_link = page.get_by_role("link", name="Child Health")
        self.choose_pharmacy_link = page.get_by_role("link", name="Choose Pharmacy")
        self.connecting_care_link = page.get_by_role("link", name="Connecting Care")
        self.dental_access_portal_link = page.get_by_role("link", name="Dental Access Portal")
        self.dental_ereferrals_link = page.get_by_role("link", name="Dental e-Referrals")
        self.electronic_test_requesting_gp_link = page.get_by_role("link", name="Electronic Test Requesting in GP Practices")
        self.my_a_and_e_live_link = page.get_by_role("link", name="My A&E Live")
        self.my_health_online_link = page.get_by_role("link", name="My Health Online")
        self.patient_access_link = page.get_by_role("link", name="Patient Access")
        self.primary_care_and_electronic_prescription_service_link = page.get_by_role("link", name="Primary Care Electronic Prescription Service")
        self.secondary_care_electronic_prescribing_and_medicines_administration_link = page.get_by_role("link", name="Secondary Care electronic Prescribing and Medicines Administration")
        self.shared_medicines_record_link = page.get_by_role("link", name="Shared Medicines Record")
        self.welsh_clinical_portal_link = page.get_by_role("link", name="Welsh Clinical Portal")
        self.welsh_gp_record_link = page.get_by_role("link", name="Welsh GP Record")
        self.wicis_system_link = page.get_by_role("link", name="Welsh Intensive Care Information System")
        self.wcnr_link = page.get_by_role("link", name="Welsh Nursing Care Record (WNCR)")

    def assert_our_digital_services_heading_is_present(self):
        self.assert_element_contains_text(self.our_digital_services_heading, "Our Digital Services")

    def assert_digital_service_is_visible(self, service_name):
        element_to_check = self.get_element_from_page_text(service_name)
        self.assert_element_is_visible(element_to_check)

    def assert_digital_service_is_hidden(self, service_name):
        element_to_check = self.get_element_from_page_text(service_name)
        self.assert_element_is_hidden(element_to_check)

    def click_digital_service(self, service_name):
        element_to_click = self.get_element_from_page_text(service_name)
        self.click(element_to_click)


    #####################

    def get_element_from_page_text(self, link_text):
        
        #then assign it with a switch/match statement
        match(link_text):
            case "Child Health":
                element = self.child_health_link
            case "Choose Pharmacy":
                element = self.choose_pharmacy_link
            case "Connecting Care":
                element = self.connecting_care_link
            case "Dental Access Portal":
                element = self.dental_access_portal_link
            case "Dental e-Referrals":
                element = self.dental_ereferrals_link
            case "Electronic Test Requesting in GP Practices":
                element = self.electronic_test_requesting_gp_link
            case "My A&E Live":
                element = self.my_a_and_e_live_link
            case "My Health Online":
                element = self.my_health_online_link
            case "Patient Access":
                element = self.patient_access_link
            case "Primary Care Electronic Prescription Service":
                element = self.primary_care_and_electronic_prescription_service_link
            case "Secondary Care electronic Prescribing and Medicines Administration":
                element = self.secondary_care_electronic_prescribing_and_medicines_administration_link
            case "Shared Medicines Record":
                element = self.shared_medicines_record_link
            case "Welsh Clinical Portal":
                element = self.welsh_clinical_portal_link
            case "Welsh GP Record":
                element = self.welsh_gp_record_link
            case "Welsh Intensive Care Information System":
                element = self.wicis_system_link
            case "Welsh Nursing Care Record (WCNR)":
                element = self.wcnr_link

        #catch error if the name is wrong
        if not element:
            raise NotImplementedError("element provided is not coded, check for typos or implement the new option")
        
        #then return it
        return element