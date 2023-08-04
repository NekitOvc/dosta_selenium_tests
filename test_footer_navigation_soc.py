from dostapages import FooterNavigationSoc


def test_footer_navigation_soc_vk(driver):
    vk = FooterNavigationSoc(driver)
    vk.get_to_site()
    vk.footer_navigation_soc_vk()

    assert driver.current_url == 'https://vk.com/dostaevsky_ru'


def test_footer_navigation_soc_telegram(driver):
    telegram = FooterNavigationSoc(driver)
    telegram.get_to_site()
    telegram.footer_navigation_soc_vk()

    assert driver.current_url == 'https://t.me/dosta_evsky'


def test_footer_navigation_soc_youtube(driver):
    youtube = FooterNavigationSoc(driver)
    youtube.get_to_site()
    youtube.footer_navigation_soc_vk()

    assert driver.current_url == 'https://www.youtube.com/channel/UC-P57_un95d2AiES0qZ3kXQ'
