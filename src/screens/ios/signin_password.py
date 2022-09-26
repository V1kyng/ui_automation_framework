from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App
from src.data.patient import Patient


class SignInPasswordScreen(App):
    """
    Signin password screen
    """

    password_input = (MobileBy.IOS_PREDICATE, "value == 'Пароль'")
    # password_input = (MobileBy.XPATH, "//XCUIElementTypeWindow[1]//XCUIElementTypeOther"
    #                                   "//XCUIElementTypeOther//XCUIElementTypeOther//XCUIElementTypeOther//"
    #                                   "XCUIElementTypeOther//XCUIElementTypeOther//XCUIElementTypeTextField")
    password_inside = (MobileBy.IOS_PREDICATE, f"value == '{Patient.PASSWORD}'")
    signin_button = (MobileBy.ACCESSIBILITY_ID, "Войти")
    new_password_input = (MobileBy.IOS_PREDICATE, "value == 'Придумайте новый пароль'")
    hidden_password = (MobileBy.ACCESSIBILITY_ID, "ic password hidden")
    forgot_password = (MobileBy.ACCESSIBILITY_ID, "Не помню пароль")
    register_button = (MobileBy.ACCESSIBILITY_ID, "Зарегистрироваться")
