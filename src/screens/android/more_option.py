from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class MoreOptionScreen(App):
    """
    More option screen locators
    """

    root_user = (MobileBy.ID, 'ru.mts.smartmed.dev:id/root_user')
    family = (MobileBy.ID, 'ru.mts.smartmed.dev:id/my_family')
    cards = (MobileBy.ID, 'ru.mts.smartmed.dev:id/my_cards')
    activity = (MobileBy.ID, 'ru.mts.smartmed.dev:id/my_activity')
    payment = (MobileBy.ID, 'ru.mts.smartmed.dev:id/payment')
    promocode = (MobileBy.ID, 'ru.mts.smartmed.dev:id/promo_code')
    settings = (MobileBy.ID, 'ru.mts.smartmed.dev:id/settings')
    help = (MobileBy.ID, 'ru.mts.smartmed.dev:id/help')


