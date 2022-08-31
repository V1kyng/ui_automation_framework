import time
from time import sleep

import pytest

from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.helpers.ios.common import Common
from src.model.AppDataModel import Patient
from src.model.MedsiConstants import ClientType, Sex, BDay, Email, FirstName, SecondName, MiddleName
from src.screens.ios.bottom_menu import BottomMenuScreen
from src.screens.ios.common import CommonScreen
from src.screens.ios.fill_new_client_data import FillNewClientDataScreen
from src.screens.ios.home import HomeScreen
from src.screens.ios.login_screen import LoginScreen
from src.screens.ios.more_option import MoreOptionScreen
from src.screens.ios.notification_screen import NotificationScreen
from src.screens.ios.profile import ProfileScreen
from src.screens.ios.promo_views import PromoScreen
from src.screens.ios.send_sms_code import SendSmsCodeScreen
from src.screens.ios.signin_password import SignInPasswordScreen
from src.screens.ios.signin_phone import SignInPhoneScreen


class TestAuth(Driver):
    LOGIN_PATIENT = Patient(phone="8888887766", password="00000000", name="Vbb Ghhj")
    NEGATIVE_REG_PATIENT = Patient(password="00000000", name="Vasya", surname="Pupkin",
                                   middle_name="Petrovich", client_type=ClientType.NEW, sex=Sex.MALE,
                                   bday=BDay.INVALID_TOO_YOUNG_FOR_IOS, email=Email.VALID,
                                   address="1311313 131313 131313", android=False)
    POSITIVE_REG_PATIENT = Patient(password="00000000",
                                   name="Vasya", surname="Pupkin",
                                   middle_name="Petrovich", client_type=ClientType.NEW, sex=Sex.MALE,
                                   bday=BDay.VALID_FIRST_AVAILABLE_WORDS, bday_words=BDay.VALID_FIRST_AVAILABLE_WORDS_PRETTY,
                                   email=Email.VALID, address="1311313 131313 131313", android=False)

    @pytest.mark.login
    @pytest.mark.sign_in
    @pytest.mark.run(order=1)
    def test_login(self):
        """
        Fast login
        No location allowed
        Skip tutorial
        """
        self.logger.info("Login test")
        patient = self.LOGIN_PATIENT.get_clone()
        Common.skip_intro(self)
        App.wait_until_exists(self, SignInPhoneScreen.phone_input)
        App.click(self, SignInPhoneScreen.phone_input)
        App.send_keys(self, SignInPhoneScreen.phone_input, patient.phone)
        App.tap_by_coordinates(self, x=163, y=319)
        App.wait_until_clickable(self, SignInPhoneScreen.next_button)
        App.click(self, SignInPhoneScreen.next_button)
        App.send_keys(self, SignInPasswordScreen.password_input, patient.password)
        App.tap_by_coordinates(self, x=163, y=319)
        App.click(self, SignInPasswordScreen.signin_button)
        code = App.get_activation_code(self, patient.phone).split(":")[1].strip()
        App.send_keys(self, SendSmsCodeScreen.code_frame, code)
        App.wait_until_exists(self, CommonScreen.code_zero)
        for i in range(2):
            for i in range(4):
                App.click(self, CommonScreen.code_zero)
        # В этом месте уведомление может выскочить как на русском так и на английском
        if App.is_exist(self, NotificationScreen.skipNotificationSettingsRu):
            App.click(self, NotificationScreen.skipNotificationSettingsRu)
        if App.is_exist(self, NotificationScreen.skipNotificationButton):
            App.click(self, NotificationScreen.skipNotificationButton)
        LoginScreen.profile_logout(self, patient)

    @pytest.mark.login
    @pytest.mark.skip(reason="https://medsi.youtrack.cloud/youtrack/issue/SM-891")
    @pytest.mark.sign_up
    def test_positive_registration_new_data_verification(self):
        # Login
        self.logger.info("Positive registration")
        patient = self.POSITIVE_REG_PATIENT.get_clone()
        Common.skip_intro(self)
        App.send_keys(self, SignInPhoneScreen.phone_input, patient.phone)
        App.tap_by_coordinates(self, x=163, y=319)
        App.click(self, SignInPhoneScreen.next_button)
        App.send_keys(self, SignInPasswordScreen.password_input, patient.password)
        App.tap_by_coordinates(self, x=163, y=319)
        if App.is_exist(self, SignInPasswordScreen.register_button):
            App.click(self, SignInPasswordScreen.register_button)
        else:
            App.click(self, SignInPasswordScreen.signin_button)
        code = App.get_activation_code(self, patient.phone).split(":")[1].strip()
        App.send_keys(self, SendSmsCodeScreen.code_frame, code)
        # Submit valid registration data
        if App.is_exist(self, PromoScreen.close_button):
            App.click(self, PromoScreen.close_button)
        if App.is_exist(self, CommonScreen.code_zero):
            for i in range(4):
                App.click(self, CommonScreen.code_zero)
        FillNewClientDataScreen.fillForm(self, patient)
        App.click(self, FillNewClientDataScreen.submit_button)
        sleep(10)
        App.click(self, FillNewClientDataScreen.submit_button)
        for i in range(4):
            App.click(self, CommonScreen.code_zero)
        sleep(2)
        for i in range(4):
            App.click(self, CommonScreen.code_zero)

        if App.is_exist(self, PromoScreen.close_button):
            App.click(self, PromoScreen.close_button)
        Common.skip_notifications(self)
        if App.is_exist(self, PromoScreen.close_button):
            App.click(self, PromoScreen.close_button)
        App.wait_until_exists(self, HomeScreen.main_header)
        App.click(self, BottomMenuScreen.more_option)
        full_name = patient.name + ' ' + patient.surname
        (a, b) = MoreOptionScreen.root_user
        App.click(self, (a,b%full_name))
        App.wait_until_exists(self, ProfileScreen.phone_text)
        self.logger.info(App.element(self, ProfileScreen.phone_text).text)
        sleep(5)
        ProfileScreen.verify_user_data(self, patient)
        App.tap(self, ProfileScreen.profile_logout)
        sleep(5)
        App.click(self, ProfileScreen.profile_exit)

    @pytest.mark.login
    @pytest.mark.skip(reason="https://medsi.youtrack.cloud/youtrack/issue/SM-892")
    @pytest.mark.sign_up
    def test_negative_registration(self):
        """
        Simple login
        Validate registration form each field and warning messages
        """
        self.logger.info("Negative registration")
        patient = self.NEGATIVE_REG_PATIENT.get_clone()
        self.logger.info("patient.phone = " + patient.phone)
        #
        Common.skip_intro(self)
        App.send_keys(self, SignInPhoneScreen.phone_input, patient.phone)
        App.tap_by_coordinates(self, x=163, y=319)
        App.click(self, SignInPhoneScreen.next_button)
        App.send_keys(self, SignInPasswordScreen.password_input, patient.password)
        App.tap_by_coordinates(self, x=163, y=319)
        if App.is_exist(self, SignInPasswordScreen.register_button):
            App.click(self, SignInPasswordScreen.register_button)
        else:
            App.click(self, SignInPasswordScreen.signin_button)
        code = App.get_activation_code(self, patient.phone).split(":")[1].strip()
        App.send_keys(self, SendSmsCodeScreen.code_frame, code)
        # Test registration form
        FillNewClientDataScreen.fillFormNegative(self, patient)
        App.click(self, FillNewClientDataScreen.iam_new_client_option)
        App.click(self, FillNewClientDataScreen.submit_button)
        App.wait_until_exists(self, FillNewClientDataScreen.empty_name_warning)
        App.wait_until_exists(self, FillNewClientDataScreen.empty_2nd_name_warning)
        App.wait_until_exists(self, FillNewClientDataScreen.empty_3rd_name_warning)
        App.send_keys(self, FillNewClientDataScreen.name_input, FirstName.INVALID_SPECIAL_SYMBOL)
        App.send_keys(self, FillNewClientDataScreen.surname_input, SecondName.INVALID_SPECIAL_SYMBOL)
        App.send_keys(self, FillNewClientDataScreen.middle_name_input, MiddleName.INVALID_SPECIAL_SYMBOL)
        App.click(self, FillNewClientDataScreen.submit_button)
        # https://medsi.myjetbrains.com/youtrack/issue/SM-235
        App.assert_size(self, FillNewClientDataScreen.name_invalid_warning, "equal to 3")
        App.click(self, FillNewClientDataScreen.back_button)
        FillNewClientDataScreen.fillForm(self, patient)
        App.click(self, FillNewClientDataScreen.submit_button)
        sleep(10)
        App.click(self, FillNewClientDataScreen.submit_button)
        App.wait_until_exists(self, FillNewClientDataScreen.bday_too_young)