from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SbisMainPage(BasePage):
    CONTACTS_BUTTON = (By.XPATH, "//a[contains(@href, '/contacts')]")

    def go_to_contacts(self):
        self.click(self.CONTACTS_BUTTON)
