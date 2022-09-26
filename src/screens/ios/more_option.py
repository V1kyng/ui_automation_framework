from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class MoreOptionScreen(App):
    """
    More option screen locators
    """

    root_user = (MobileBy.ACCESSIBILITY_ID, '%s')
    family = (MobileBy.ACCESSIBILITY_ID, 'Моя семья')
    cards = (MobileBy.ACCESSIBILITY_ID, 'Мои карты')
    activity = (MobileBy.ACCESSIBILITY_ID, 'Моя активность')
    payment = (MobileBy.ACCESSIBILITY_ID, 'Счета и история')
    promocode = (MobileBy.ACCESSIBILITY_ID, 'Промокоды')
    settings = (MobileBy.ACCESSIBILITY_ID, 'Настройки')
    help = (MobileBy.ACCESSIBILITY_ID, 'Помощь')


