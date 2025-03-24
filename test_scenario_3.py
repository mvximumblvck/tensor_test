import os
import requests
from pages.sbis_main_page import SbisMainPage

def test_scenario_3(driver):
    sbis_main = SbisMainPage(driver)
    
    # Открываем главную страницу и переходим к загрузке плагина
    sbis_main.open_url("https://sbis.ru/")
    driver.find_element("xpath", "//a[contains(text(), 'Скачать локальные версии')]").click()
    download_link = driver.find_element("xpath", "//a[contains(text(), 'Скачать СБИС Плагин')]").get_attribute("href")

    # Скачиваем файл
    response = requests.get(download_link, stream=True)
    file_path = "sbis_plugin.exe"
    with open(file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    # Проверяем размер
    file_size = os.path.getsize(file_path) / (1024 * 1024)
    assert round(file_size, 2) == 3.64, "Размер файла не совпадает"
