from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SignInButtonScreen(App):
    """
    Signing button screen
    """

    def __init__(self, driver):
        super().__init__()

    button = (MobileBy.ACCESSIBILITY_ID, "Войти")
