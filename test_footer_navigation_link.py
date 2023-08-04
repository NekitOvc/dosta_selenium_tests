from dostapages import FooterNavigationLink
from selenium.webdriver.common.by import By


def test_footer_navigation_link_our_kitchen(driver):
    our_kitchen = FooterNavigationLink(driver)
    our_kitchen.get_to_site()
    our_kitchen.footer_navigation_link_our_kitchen()

    assert driver.current_url == 'https://dostaevsky.ru/our-kitchen'
    assert driver.find_element(By.CLASS_NAME, 'article-header__title').text == 'Наша кухня'


def test_footer_navigation_link_shipping(driver):
    shipping = FooterNavigationLink(driver)
    shipping.get_to_site()
    shipping.footer_navigation_link_shipping()

    assert driver.current_url == 'https://dostaevsky.ru/shipping'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Доставка и оплата в Санкт-Петербурге'


def test_footer_navigation_link_payment(driver):
    payment = FooterNavigationLink(driver)
    payment.get_to_site()
    payment.footer_navigation_link_payment()

    assert driver.current_url == 'https://dostaevsky.ru/payment'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Оплата еды в Санкт-Петербурге'


def test_footer_navigation_link_reviews(driver):
    reviews = FooterNavigationLink(driver)
    reviews.get_to_site()
    reviews.footer_navigation_link_reviews()

    assert driver.current_url == 'https://dostaevsky.ru/reviews'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Отзывы'


def test_footer_navigation_link_contacts(driver):
    contacts = FooterNavigationLink(driver)
    contacts.get_to_site()
    contacts.footer_navigation_link_contacts()

    assert driver.current_url == 'https://dostaevsky.ru/contacts'
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Контакты'


def test_footer_navigation_link_job(driver):
    job = FooterNavigationLink(driver)
    job.get_to_site()
    job.footer_navigation_link_job()

    assert driver.current_url == 'https://spb.hh.ru/employer/1340780'


def test_footer_navigation_link_franchise(driver):
    franchise = FooterNavigationLink(driver)
    franchise.get_to_site()
    franchise.footer_navigation_link_franchise()

    assert driver.current_url == 'https://franchise.dostaevsky.ru/'


def test_footer_navigation_link_google_form(driver):
    google_form = FooterNavigationLink(driver)
    google_form.get_to_site()
    google_form.footer_navigation_link_google_form()

    assert driver.current_url == 'https://docs.google.com/forms/d/e/1FAIpQLScviSRjfU1eLiT1mvzBL0VqTQQo9hji78u_6AcGE1OK8UwBBQ/viewform'