from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SbisContactsPage(BasePage):
    TENSOR_BANNER = (By.XPATH, "//a[contains(@href, 'tensor.ru')]")
    REGION_NAME = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    PARTNERS_LIST = (By.CLASS_NAME, "sbisru-Contacts-Persons__list")
    REGION_INPUT = (By.CLASS_NAME, "sbis_ru-Region-Panel__list")
    
    def click_tensor_banner(self):
        self.click(self.TENSOR_BANNER)

    def get_region_name(self):
        return self.find_element(self.REGION_NAME).text

    def get_partners(self):
        return self.find_elements(self.PARTNERS_LIST)

    def change_region(self, region_name):
        self.click(self.REGION_NAME)
        region_locator = (By.XPATH, f"//span[contains(text(), '{region_name}')]")
        self.click(region_locator)
