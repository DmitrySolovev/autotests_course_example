# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'

try:
    browser.get(sbis_site)
    sleep(1)
    assert browser.current_url == sbis_site, 'Неверный url'
    contacts_link = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link[href="/contacts"]')
    contacts_link.click()
    sleep(1)
    tensor_logo = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__logo-link')
    tensor_logo.click()
    sleep(1)
    browser.get(tensor_site)
    sleep(1)
    assert browser.current_url == tensor_site, 'Неверный url'
    content_block = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    content_block.location_once_scrolled_into_view
    assert content_block.is_displayed(), 'Блок не отображается'
    content_block_link = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link')
    content_block_link.click()
    sleep(1)
    assert browser.current_url == 'https://tensor.ru/about', 'Неверный url'
finally:
    browser.quit()
