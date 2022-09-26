from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from appium.webdriver.common.mobileby import MobileBy
from src.helpers.app import App

from src.screens.ios.signin_password import SignInPasswordScreen
from src.screens.ios.signin_phone import SignInPhoneScreen
from src.data.patient import Patient


class LoginScreen(App):
    """
    login screen locators
    """

    inputField = (MobileBy.ACCESSIBILITY_ID, "input-email")
    passwordField = (MobileBy.ACCESSIBILITY_ID, "input-password")
    loginButton = (MobileBy.XPATH, "//XCUIElementTypeStaticText[@name='LOGIN']")
    ENTER_BTN = (MobileBy.ACCESSIBILITY_ID, "Войти")
    ENTER_SMS_FIELD = (MobileBy.IOS_PREDICATE, "type == 'XCUIElementTypeTextField'")
    SMS_SCREEN_HEADER = (MobileBy.ACCESSIBILITY_ID, "Введите код из смс")
    ZERO_BTN = (MobileBy.ACCESSIBILITY_ID, "0")
    ENTER_PIN = (MobileBy.ACCESSIBILITY_ID, "Создайте код доступа")
    ENTER_PIN_AGAIN = (MobileBy.ACCESSIBILITY_ID, "Повторите код доступа")
    ENTER_PIN_SECOND = (MobileBy.ACCESSIBILITY_ID, "Введите код доступа")
    NOT_ALLOW = (MobileBy.ACCESSIBILITY_ID, "Don’t Allow")
    ALLOW = (MobileBy.ACCESSIBILITY_ID, "Allow")
    INFO_MSG = (MobileBy.ACCESSIBILITY_ID, "Notifications may include alerts, sounds and icon badges. These can be "
                                           "configured in Settings.")

    def click_to_login_btn(self):
        if self.find_element(self.ENTER_BTN):
            self.click_to_element(self.ENTER_BTN)

    def fill_phone_number(self):
        self.set_field(SignInPhoneScreen.phone_input, Patient.PHONE)
        while self.find_text(SignInPhoneScreen.phone_input).text != Patient.PHONE:
            self.click_to_element(SignInPhoneScreen.clear_button)
            self.set_field(SignInPhoneScreen.phone_input, Patient.PHONE)
        self.tap_by_coordinates(x=163, y=319)
        self.click_to_element(SignInPhoneScreen.next_button)

    def fill_password_field(self):
        self.set_field(SignInPasswordScreen.password_input, Patient.PASSWORD)
        self.click_to_element(SignInPasswordScreen.hidden_password)
        self.find_visible_elem(SignInPasswordScreen.password_inside)
        while self.find_visible_elem(SignInPasswordScreen.password_inside).text != Patient.PASSWORD:
            action = ActionChains(self.driver)
            action.send_keys_to_element(SignInPasswordScreen.password_inside,
                                        Keys.CONTROL + 'a', Keys.BACKSPACE)
            action.release()
            self.set_field(SignInPasswordScreen.password_inside, Patient.PASSWORD)
        self.tap_by_coordinates(x=163, y=319)
        self.click_to_element(SignInPasswordScreen.signin_button)

    def enter_sms_code(self, code):
        self.set_field(self.ENTER_SMS_FIELD, code)

    def enter_login_pin(self):
        self.find_text(self.ENTER_PIN)
        for i in range(0, 4):
            self.click_to_element(self.ZERO_BTN)
        self.find_text(self.ENTER_PIN_AGAIN)
        for i in range(0, 4):
            self.click_to_element(self.ZERO_BTN)

    def enter_pin(self):
        if self.until_element_invisible(self.SMS_SCREEN_HEADER):
            for i in range(0, 4):
                self.click_to_element(self.ZERO_BTN)

    def dont_allow_notification(self):
        button = self.find_clickable_element(self.NOT_ALLOW)
        button.click()

