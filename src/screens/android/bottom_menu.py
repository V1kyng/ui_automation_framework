from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class BottomMenuScreen(App):
    """
    Home screen locators
    """
    def __init__(self):
        super().__init__()

    home_option = (MobileBy.ID, 'ru.mts.smartmed.dev:id/bottom_menu_dashboard')
    patients_card_option = (MobileBy.ID, 'ru.mts.smartmed.dev:id/bottom_menu_medcard')
    doctors_option = (MobileBy.ID, "ru.mts.smartmed.dev:id/bottom_menu_doctors")
    more_option = (MobileBy.ID, "ru.mts.smartmed.dev:id/bottom_menu_more")



