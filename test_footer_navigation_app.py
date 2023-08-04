from dostapages import FooterNavigationApp


def test_footer_navigation_app_itunes(driver):
    itunes = FooterNavigationApp(driver)
    itunes.get_to_site()
    itunes.footer_navigation_app_itunes()

    assert driver.current_url == 'https://apps.apple.com/ru/app/dostaevskij-dostavka-edy/id982919070'


def test_footer_navigation_app_google_play(driver):
    google_play = FooterNavigationApp(driver)
    google_play.get_to_site()
    google_play.footer_navigation_app_google_play()

    assert driver.current_url == 'https://play.google.com/store/apps/details?id=ru.dostaevsky.android'


def test_footer_navigation_app_huawei(driver):
    huawei = FooterNavigationApp(driver)
    huawei.get_to_site()
    huawei.footer_navigation_app_huawei()

    assert driver.current_url == 'https://appgallery.huawei.com/#/app/C101172305'
