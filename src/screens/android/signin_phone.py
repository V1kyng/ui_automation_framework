from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SignInPhoneScreen(App):
    """
    Send phone number
    """

    def __init__(self, driver):
        super().__init__()

    phone_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/txtPhoneNumber")
    next_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/button_text")