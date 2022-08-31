from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class BottomMenuScreen(App):
    """
    Home screen locators
    """

    home_option = (MobileBy.ACCESSIBILITY_ID, 'Главная')
    patients_card_option = (MobileBy.ACCESSIBILITY_ID, 'Медкарта')
    doctors_option = (MobileBy.ACCESSIBILITY_ID, 'Врачи')
    more_option = (MobileBy.ACCESSIBILITY_ID, 'Ещё')

    def __init__(self, driver):
        super().__init__()