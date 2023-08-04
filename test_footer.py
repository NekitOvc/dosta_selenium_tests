from dostapages import Footer
from selenium.webdriver.common.by import By


def test_footer_user_agreement(driver):
    user_agreement = Footer(driver)
    user_agreement.get_to_site()
    user_agreement.footer_user_agreement()

    assert driver.current_url == 'https://dostaevsky.ru/user-agreement'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Пользовательское соглашение ' \
                                                          'сервиса по заказу и доставке Продукции'


def test_footer_license_agreement(driver):
    license_agreement = Footer(driver)
    license_agreement.get_to_site()
    license_agreement.footer_license_agreement()

    assert driver.current_url == 'https://dostaevsky.ru/license-agreement'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Лицензионное соглашение на использование программы ' \
                                                          '«Достаевский» для мобильных устройств'


def test_footer_confidentiality_of_personal_information(driver):
    confidentiality_of_personal_information = Footer(driver)
    confidentiality_of_personal_information.get_to_site()
    confidentiality_of_personal_information.footer_confidentiality_of_personal_information()

    assert driver.current_url == 'https://dostaevsky.ru/confidentiality-of-personal-information'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Политика обработки персональных данных'


def test_footer_promo_codes(driver):
    promo_codes = Footer(driver)
    promo_codes.get_to_site()
    promo_codes.footer_promo_codes()

    assert driver.current_url == 'https://dostaevsky.ru/promo-codes-terms-and-conditions'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Условия использования промокодов'


def test_footer_full_menu(driver):
    full_menu = Footer(driver)
    full_menu.get_to_site()
    full_menu.footer_full_menu()

    assert driver.current_url == 'https://docs.google.com/spreadsheets/d/1AOhpTgj2npSecsW-C7WGmOyw_rNkf571k4bHodMv_RU/edit'


def test_footer_trademarks(driver):
    trademarks = Footer(driver)
    trademarks.get_to_site()
    trademarks.footer_trademarks()

    assert driver.current_url == 'https://dostaevsky.ru/trademarks'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Товарные знаки Dostaевский'
