from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SignInPasswordScreen(App):
    """
    Signin password screen
    """

    def __init__(self, driver):
        super().__init__()

    password_input = (MobileBy.IOS_PREDICATE, "value == 'Пароль'")
    signin_button = (MobileBy.ACCESSIBILITY_ID, "Войти")
    new_password_input = (MobileBy.IOS_PREDICATE, "value == 'Придумайте новый пароль'")
    hidden_password = (MobileBy.ACCESSIBILITY_ID, "ic password hidden")
    forgot_password = (MobileBy.ACCESSIBILITY_ID, "Не помню пароль")
    register_button = (MobileBy.ACCESSIBILITY_ID, "Зарегистрироваться")