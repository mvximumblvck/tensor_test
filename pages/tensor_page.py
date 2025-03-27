from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorPage(BasePage):
    STRENGTH_IN_PEOPLE = (By.XPATH, "//h2[contains(text(), 'Сила в людях')]")
    MORE_BUTTON = (By.XPATH, "//a[contains(text(), 'Подробнее')]")
    WORK_SECTION_IMAGES = (By.XPATH, "//section[contains(@class, 'work')]//img")

    def check_strength_in_people(self):
        return self.find_element(self.STRENGTH_IN_PEOPLE)

    def click_more(self):
        self.click(self.MORE_BUTTON)

    def get_work_section_images(self):
        return self.find_elements(self.WORK_SECTION_IMAGES)
