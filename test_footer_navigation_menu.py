from dostapages import FooterNavigationMenu
from selenium.webdriver.common.by import By


def test_footer_navigation_menu_mexican(driver):
    mexican = FooterNavigationMenu(driver)
    mexican.get_to_site()
    mexican.footer_navigation_menu_mexican()

    assert driver.current_url == 'https://dostaevsky.ru/mexican-cuisine'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Мексиканская кухня'


def test_footer_navigation_menu_italian(driver):
    italian = FooterNavigationMenu(driver)
    italian.get_to_site()
    italian.footer_navigation_menu_italian()

    assert driver.current_url == 'https://dostaevsky.ru/italian-cuisine'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Итальянская кухня'


def test_footer_navigation_menu_chinese(driver):
    chinese = FooterNavigationMenu(driver)
    chinese.get_to_site()
    chinese.footer_navigation_menu_chinese()

    assert driver.current_url == 'https://dostaevsky.ru/chinese-cuisine'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Китайская кухня'


def test_footer_navigation_menu_japanese(driver):
    japanese = FooterNavigationMenu(driver)
    japanese.get_to_site()
    japanese.footer_navigation_menu_japanese()

    assert driver.current_url == 'https://dostaevsky.ru/japanese-cuisine'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Японская кухня'