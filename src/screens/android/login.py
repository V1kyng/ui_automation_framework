import time
from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App
from src.screens.android.allow_location import AllowLocationScreen
from src.screens.android.bottom_menu import BottomMenuScreen
from src.screens.android.city_selection import CitySelectionScreen
from src.screens.android.common import CommonScreen
from src.screens.android.patients import PatientScreen
from src.screens.android.profile import ProfileScreen
from src.screens.android.signin_button import SignInButtonScreen
from src.screens.android.signin_password import SignInPasswordScreen
from src.screens.android.signin_phone import SignInPhoneScreen
from src.screens.android.welcome import WelcomeTutorialScreen


class LoginScreen(App):
    """
    login screen locators
    """

    LOGIN_PATIENT = {"phone": "8888887766", "password": "00000000"}
    input_field = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="input-email"]')
    password_field = (MobileBy.ACCESSIBILITY_ID, 'input-password')
    login_button = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="button-LOGIN"]/android.view.ViewGroup')
    ZERO_BTN = (MobileBy.ID, "ru.mts.smartmed.dev:id/tbZero")
    """
    package	ru.mts.smartmed.dev
    class android.widget.TextView
    text 0
    """

    def enter_login_pin(self):
        for i in range(0, 4):
            self.click_to_element(self.ZERO_BTN)
            time.sleep(0.5)
        for i in range(0, 4):
            self.click_to_element(self.ZERO_BTN)

    def enter_pin(self):
        for i in range(0, 4):
            self.click_to_element(self.ZERO_BTN)

    # def send_key_events(self, input):
    #     for char in input:
    #         self.driver.keyevent(NUMERIC_KEYBOARD[char])
    def dont_allow_notification(self):
        self.find_clickable_element(WelcomeTutorialScreen.not_use_fingerprint).click()



    def session_login(self):
        # TODO: добавить проверку что мы залогинены
        patient = LoginScreen.LOGIN_PATIENT
        self.driver.save_screenshot(f"screenshots/test_before_login.png")
        if App.is_exist(self, AllowLocationScreen.skipLocationButton) == True:
            App.click(self, AllowLocationScreen.skipLocationButton)
            App.click(self, CitySelectionScreen.moscow_city)
            App.click(self, CitySelectionScreen.continue_button)
            App.click(self, WelcomeTutorialScreen.skip_tutorial_button)
        App.click(self, SignInButtonScreen.button)
        self.driver.save_screenshot(f"screenshots/1.png")
        App.click(self, SignInPhoneScreen.phone_input)
        self.driver.save_screenshot(f"screenshots/2.png")
        App.send_key_events(self, patient["phone"])
        self.driver.save_screenshot(f"screenshots/3.png")
        App.click(self, SignInPhoneScreen.next_button)
        self.driver.save_screenshot(f"screenshots/4.png")
        App.send_keys(self, SignInPasswordScreen.password_input, patient["password"])
        self.driver.save_screenshot(f"screenshots/5.png")
        App.click(self, SignInPasswordScreen.signin_button)
        code = App.get_activation_code(self, patient["phone"]).split(":")[1].strip()
        App.send_key_events(self, code)
        for i in range(2):
            for i in range(4):
                App.click(self, CommonScreen.code_zero)
        # time.sleep(4)
        App.click(self, WelcomeTutorialScreen.not_use_fingerprint)

    def profile_logout(self):
        # for i in range(4):
        #     App.click(self, CommonScreen.code_zero)
        App.wait_until_exists(self, BottomMenuScreen.more_option)
        App.click(self, BottomMenuScreen.more_option)
        App.click(self, PatientScreen.patient_profile_name)
        App.click(self, ProfileScreen.profile_logout)
        App.click(self, ProfileScreen.profile_exit)
        time.sleep(3)