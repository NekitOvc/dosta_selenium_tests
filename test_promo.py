from dostapages import PromoPages
from selenium.webdriver.common.by import By


def test_promo_button(driver):
    button = PromoPages(driver)
    button.get_to_site()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[3]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()
    button.promo_button()

    assert driver.current_url == 'https://dostaevsky.ru/promo'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Акции'


def test_promo_present_when_ordering_through_app(driver):
    promo = PromoPages(driver)
    promo.get_to_site()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[3]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()
    promo.promo_button()

    promo.promo_present_when_ordering_through_app()

    assert driver.current_url == 'https://dostaevsky.ru/promo/present-when-ordering-through-app'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Подарок при заказе через мобильное приложение'


def test_promo_3_for_439(driver):
    promo = PromoPages(driver)
    promo.get_to_site()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[3]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()
    promo.promo_button()

    promo.promo_3_for_439()

    assert driver.current_url == 'https://dostaevsky.ru/promo/3-for-439'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Три smart-ролла за 439 рублей'


def test_promo_2_for_649(driver):
    promo = PromoPages(driver)
    promo.get_to_site()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[3]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()
    promo.promo_button()

    promo.promo_2_for_649()

    assert driver.current_url == 'https://dostaevsky.ru/promo/2-for-649'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Две smart-пиццы за 649 рублей'


def test_promo_3_for_1149(driver):
    promo = PromoPages(driver)
    promo.get_to_site()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[3]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()
    promo.promo_button()

    promo.promo_3_for_1149()

    assert driver.current_url == 'https://dostaevsky.ru/promo/3-for-1149'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Собери свое комбо за 1149 рублей'


def test_promo_2_woks_for_499(driver):
    promo = PromoPages(driver)
    promo.get_to_site()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[3]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()
    promo.promo_button()

    promo.promo_2_woks_for_499()

    assert driver.current_url == 'https://dostaevsky.ru/promo/2-woks-for-499'
    assert driver.find_element(By.TAG_NAME, 'h1').text == "2 Wok'а за 499 рублей"


def test_promo_2_for_849(driver):
    promo = PromoPages(driver)
    promo.get_to_site()
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[3]/aside/nav/div/div/div[1]/div[1]/div/div[2]/button[1]').click()
    promo.promo_button()

    promo.promo_2_for_849()

    assert driver.current_url == 'https://dostaevsky.ru/promo/2-for-849'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Две пиццы или пирога за 849 рублей'
