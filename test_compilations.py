from dostapages import CategoryMenu, Compilations
from selenium.webdriver.common.by import By


def test_compilations_new(driver):
    new = Compilations(driver)
    new.get_to_site()
    new.compilations_new()

    assert driver.current_url == 'https://dostaevsky.ru/new'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Новинки'


def test_compilations_fastfood(driver):
    fastfood = Compilations(driver)
    fastfood.get_to_site()
    fastfood.compilations_fastfood()

    assert driver.current_url == 'https://dostaevsky.ru/fastfood'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Фастфуд'


def test_compilations_pan_asian(driver):
    pan_asian = Compilations(driver)
    pan_asian.get_to_site()
    pan_asian.compilations_pan_asian()

    assert driver.current_url == 'https://dostaevsky.ru/pan-asian'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Паназия'


def test_compilations_lunch(driver):
    lunch = Compilations(driver)
    lunch.get_to_site()
    lunch.compilations_lunch()

    assert driver.current_url == 'https://dostaevsky.ru/lunch'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Обед'


def test_compilations_hearty(driver):
    hearty = Compilations(driver)
    hearty.get_to_site()
    hearty.compilations_hearty()

    assert driver.current_url == 'https://dostaevsky.ru/hearty'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Сытно'


def test_compilations_light(driver):
    light = Compilations(driver)
    light.get_to_site()
    light.compilations_light()

    assert driver.current_url == 'https://dostaevsky.ru/light'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Лайт'


def test_compilations_shrimps(driver):
    shrimps = Compilations(driver)
    shrimps.get_to_site()
    shrimps.compilations_shrimps()

    assert driver.current_url == 'https://dostaevsky.ru/shrimps'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Креветки'


def test_compilations_salmon(driver):
    salmon = Compilations(driver)
    salmon.get_to_site()
    salmon.compilations_salmon()

    assert driver.current_url == 'https://dostaevsky.ru/salmon'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Лосось'


def test_compilations_vegetarian_menu(driver):
    vegetarian_menu = Compilations(driver)
    vegetarian_menu.get_to_site()
    vegetarian_menu.compilations_vegetarian_menu()

    assert driver.current_url == 'https://dostaevsky.ru/vegetarian-menu'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Вегетарианское меню'


def test_compilations_for_kids(driver):
    for_kids = Compilations(driver)
    for_kids.get_to_site()
    for_kids.compilations_for_kids()

    assert driver.current_url == 'https://dostaevsky.ru/for-kids'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Детское меню'


def test_compilations_sweet(driver):
    sweet = Compilations(driver)
    sweet.get_to_site()
    sweet.compilations_sweet()

    assert driver.current_url == 'https://dostaevsky.ru/sweet'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Сладкое'
