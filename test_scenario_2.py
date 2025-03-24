import pytest
from pages.sbis_main_page import SbisMainPage
from pages.sbis_contacts_page import SbisContactsPage

def test_scenario_2(driver):
    sbis_main = SbisMainPage(driver)
    sbis_contacts = SbisContactsPage(driver)

    # Открываем страницу контактов
    sbis_main.open_url("https://sbis.ru/")
    sbis_main.go_to_contacts()

    # Проверяем регион и список партнеров
    initial_region = sbis_contacts.get_region_name()
    initial_partners = sbis_contacts.get_partners()
    assert initial_region, "Регион не определился"
    assert initial_partners, "Список партнеров пуст"

    # Меняем регион на Камчатский край
    sbis_contacts.change_region("Камчатский край")

    # Проверяем изменения
    assert sbis_contacts.get_region_name() == "Камчатский край"
    assert sbis_contacts.get_partners() != initial_partners
    assert "kamchatskij-kraj" in driver.current_url
