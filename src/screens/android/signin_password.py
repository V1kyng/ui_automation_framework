from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SignInPasswordScreen(App):
    """
    Signin password screen
    """

    password_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/txtPassword")
    signin_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/button_text")
    new_password_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/password_new_input_text")
    