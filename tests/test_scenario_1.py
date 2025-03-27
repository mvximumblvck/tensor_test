import pytest
from pages.sbis_main_page import SbisMainPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_page import TensorPage

def test_scenario_1(driver):
    sbis_main = SbisMainPage(driver)
    sbis_contacts = SbisContactsPage(driver)
    tensor_page = TensorPage(driver)

    # Открываем СБИС, переходим в Контакты
    sbis_main.open_url("https://sbis.ru/")
    sbis_main.go_to_contacts()

    # Нажимаем на баннер Тензора
    sbis_contacts.click_tensor_banner()

    # Проверяем блок "Сила в людях"
    assert tensor_page.check_strength_in_people()

    # Переходим в "Подробнее"
    tensor_page.click_more()
    assert "https://tensor.ru/about" in driver.current_url

    # Проверяем одинаковые размеры изображений
    images = tensor_page.get_work_section_images()
    sizes = [(img.get_attribute("naturalWidth"), img.get_attribute("naturalHeight")) for img in images]
    assert all(size == sizes[0] for size in sizes), "Изображения имеют разные размеры"
