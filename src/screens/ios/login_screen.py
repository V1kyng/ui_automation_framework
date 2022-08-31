import time

from appium.webdriver.common.mobileby import MobileBy
from src.helpers.app import App
from src.helpers.ios.common import Common
from src.screens.ios.allow_location import AllowLocationScreen
from src.screens.ios.bottom_menu import BottomMenuScreen
from src.screens.ios.common import CommonScreen
from src.screens.ios.home import HomeScreen
from src.screens.ios.notification_screen import NotificationScreen
from src.model.AppDataModel import Patient
from src.screens.ios.patient import PatientScreen
from src.screens.ios.profile import ProfileScreen
from src.screens.ios.send_sms_code import SendSmsCodeScreen
from src.screens.ios.signin_button import SignInButtonScreen
from src.screens.ios.signin_password import SignInPasswordScreen
from src.screens.ios.signin_phone import SignInPhoneScreen
from src.screens.ios.welcome import WelcomeTutorialScreen


class LoginScreen(App):
    """
    login screen locators
    """
    LOGIN_PATIENT = Patient(phone="8888887766", password="00000000")
    inputField = (MobileBy.ACCESSIBILITY_ID, 'input-email')
    passwordField = (MobileBy.ACCESSIBILITY_ID, 'input-password')
    loginButton = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="LOGIN"]')

    # LOGIN_PATIENT = Patient(phone="8888887766", password="00000000")

    def session_login(self):
        patient = LoginScreen.LOGIN_PATIENT
        # After logout and login repeat if-steps below is removed
        if App.is_exist(self, AllowLocationScreen.skipLocationButton, expected=True, n=2) == True:
            App.click(self, AllowLocationScreen.skipLocationButton)
            App.click(self, WelcomeTutorialScreen.skip_tutorial_button)
        else:
            pass
        time.sleep(5)
        if App.is_exist(self, SignInButtonScreen.button):
            App.click(self, SignInButtonScreen.button)
            App.click(self, SignInPhoneScreen.phone_input)
            App.send_keys(self, SignInPhoneScreen.phone_input, patient.phone)
            App.tap_by_coordinates(self, x=163, y=319)
            App.click(self, SignInPhoneScreen.next_button)
            App.send_keys(self, SignInPasswordScreen.password_input, patient.password)
            App.tap_by_coordinates(self, x=163, y=319)
            App.click(self, SignInPasswordScreen.signin_button)
            code = App.get_activation_code(self, patient.phone).split(":")[1].strip()
            App.send_keys(self, SendSmsCodeScreen.code_frame, code)
            # create code after install
            for i in range(2):
                for i in range(4):
                    App.click(self, CommonScreen.code_zero)
        else:
            # entering installed code
            for i in range(4):
                App.click(self, CommonScreen.code_zero)
        Common.skip_notifications(self)

    def profile_logout(self, patient: Patient):
        HomeScreen.get_app_main_page(self)
        if App.is_exist(self, NotificationScreen.skipNotificationSettingsRu, expected=True, n=2):
            App.click(self, NotificationScreen.skipNotificationSettingsRu)
        if App.is_exist(self, NotificationScreen.skipNotificationButton, expected=True, n=2):
            App.click(self, NotificationScreen.skipNotificationButton)
        App.wait_until_exists(self, BottomMenuScreen.more_option)
        App.click(self, BottomMenuScreen.more_option)
        App.click(self, PatientScreen.get_profile_name_xpath_by_value(self, patient.name))
        App.swipe_top_to_bottom(self)
        App.click(self, ProfileScreen.profile_logout)
        App.click(self, ProfileScreen.profile_exit)
