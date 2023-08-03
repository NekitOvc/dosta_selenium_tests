from dostapages import CategoryMenu
from selenium.webdriver.common.by import By


def test_category_georgia(driver):
    georgia = CategoryMenu(driver)
    georgia.get_to_site()
    georgia.category_georgia()

    assert driver.current_url == 'https://dostaevsky.ru/georgia'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Грузия'


def test_category_main_dishes(driver):
    main_dishes = CategoryMenu(driver)
    main_dishes.get_to_site()
    main_dishes.category_hot_menu()

    assert driver.current_url == 'https://dostaevsky.ru/main-dishes'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Горячее'


def test_category_breakfast(driver):
    breakfast = CategoryMenu(driver)
    breakfast.get_to_site()
    breakfast.category_breakfast()

    assert driver.current_url == 'https://dostaevsky.ru/breakfast'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Завтраки'


def test_category_pizza(driver):
    pizza = CategoryMenu(driver)
    pizza.get_to_site()
    pizza.category_pizza()

    assert driver.current_url == 'https://dostaevsky.ru/pizza'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Пицца'


def test_category_pies(driver):
    pies = CategoryMenu(driver)
    pies.get_to_site()
    pies.category_pies()

    assert driver.current_url == 'https://dostaevsky.ru/pies'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Пироги'


def test_category_sets_sushi_rolls(driver):
    sets_sushi_rolls = CategoryMenu(driver)
    sets_sushi_rolls.get_to_site()
    sets_sushi_rolls.category_sets_sushi_rolls()

    assert driver.current_url == 'https://dostaevsky.ru/sets-sushi-rolls'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Суши и роллы'


def test_category_onigiri(driver):
    onigiri = CategoryMenu(driver)
    onigiri.get_to_site()
    onigiri.category_onigiri()

    assert driver.current_url == 'https://dostaevsky.ru/onigiri'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Онигири'


def test_category_combo_sets(driver):
    combo_sets = CategoryMenu(driver)
    combo_sets.get_to_site()
    combo_sets.category_combo_sets()

    assert driver.current_url == 'https://dostaevsky.ru/combo-sets'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Комбо и сеты'


def test_category_burgers(driver):
    burgers = CategoryMenu(driver)
    burgers.get_to_site()
    burgers.category_burgers()

    assert driver.current_url == 'https://dostaevsky.ru/burgers'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Бургеры'


def test_category_streetfood(driver):
    streetfood = CategoryMenu(driver)
    streetfood.get_to_site()
    streetfood.category_streetfood()

    assert driver.current_url == 'https://dostaevsky.ru/streetfood'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Стритфуд'


def test_category_snacks(driver):
    snacks = CategoryMenu(driver)
    snacks.get_to_site()
    snacks.category_snacks()

    assert driver.current_url == 'https://dostaevsky.ru/snacks'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Закуски'


def test_category_bowls(driver):
    bowls = CategoryMenu(driver)
    bowls.get_to_site()
    bowls.category_bowls()

    assert driver.current_url == 'https://dostaevsky.ru/bowls'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Боулы'

def test_category_woks(driver):
    woks = CategoryMenu(driver)
    woks.get_to_site()
    woks.category_woks()

    assert driver.current_url == 'https://dostaevsky.ru/woks'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Wok'


def test_category_salads(driver):
    salads = CategoryMenu(driver)
    salads.get_to_site()
    salads.category_salads()

    assert driver.current_url == 'https://dostaevsky.ru/salads'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Салаты'