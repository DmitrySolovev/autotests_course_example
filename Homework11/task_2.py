# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep


browser = webdriver.Chrome()
auth = 'https://fix-online.sbis.ru/auth/'
contacts = 'https://fix-online.sbis.ru/page/dialogs'
login = 'new_roles'
password = 'new_roles123'
message_text = 'Тестовое сообщение 123'

try:
    browser.maximize_window()
    browser.get(auth)
    sleep(1)
    login_field = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login_field.send_keys(login, Keys.ENTER)
    assert login_field.get_attribute('value') == login, 'Логин не введен в поле'
    password_field = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password_field.send_keys(password, Keys.ENTER)
    sleep(4)
    browser.get(contacts)
    sleep(2)
    add_btn = browser.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    add_btn.click()
    sleep(2)
    address_window = browser.find_element(By.CSS_SELECTOR, '[data-qa = "addressee-selector-root"]')
    assert address_window.is_displayed(), 'Справочник выбора адресата не открыт'
    address_window_search = browser.find_element(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"] .controls-Field')
    address_window_search.send_keys('Соловьев НовыеРоли')
    sleep(2)
    address_message = browser.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    assert address_message.get_attribute('title') == 'Соловьев НовыеРоли', 'В справочнике не найдена запись'
    address_message.click()
    sleep(2)
    message_field = browser.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    assert message_field.is_displayed(), 'Поле ввода сообщения не отображается'
    message_field.send_keys(message_text)
    sleep(2)
    message_send_btn = browser.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    message_send_btn.click()
    sleep(2)
    messages = browser.find_elements(By.CSS_SELECTOR, '.controls-MasterDetail_details .msg-entity-text')
    assert messages[0].text == message_text, 'Отправленное сообщение не найдено в реестре'
    actions_chain = ActionChains(browser)
    actions_chain.move_to_element(messages[0])
    actions_chain.perform()
    sleep(1)
    delete_message_btn = browser.find_elements(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete_message_btn[0].click()
    sleep(1)
    messages = browser.find_elements(By.CSS_SELECTOR, '.controls-MasterDetail_details .msg-entity-text')
    assert messages[0].text != message_text, 'Последнее сообщение не удалено'
    sleep(1)
finally:
    browser.quit()