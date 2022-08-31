from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class BaseScreen(App):
    """
    common screen locators
    """

    def __init__(self, driver):
        super().__init__()