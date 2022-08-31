from time import sleep
import pytest
from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.model.AppDataModel import Patient
from src.screens.android.allow_location import AllowLocationScreen
from src.screens.android.bottom_menu import BottomMenuScreen
from src.screens.android.city_selection import CitySelectionScreen
from src.screens.android.common import CommonScreen
from src.screens.android.fill_new_client_data import FillNewClientDataScreen
from src.screens.android.home import HomeScreen
from src.screens.android.login import LoginScreen
from src.screens.android.more_option import MoreOptionScreen
from src.screens.android.profile import ProfileScreen
from src.screens.android.promo_views import PromoScreen
from src.screens.android.signin_button import SignInButtonScreen
from src.screens.android.signin_password import SignInPasswordScreen
from src.screens.android.signin_phone import SignInPhoneScreen
from src.screens.android.welcome import WelcomeTutorialScreen
from src.model.MedsiConstants import ClientType, Sex, BDay, EMPTY, Email, FirstName, SecondName, MiddleName


class TestAuth(Driver):
    NEGATIVE_REG_PATIENT = Patient(password="00000000", name="Vasya", surname="Pupkin",
                                   middle_name="Petrovich", client_type=ClientType.NEW, sex=Sex.MALE,
                                   bday=BDay.VALID_FIRST_AVAILABLE_NUMBERS, email=Email.VALID, address="1311313 131313 131313")
    POSITIVE_REG_PATIENT = Patient(password="00000000", name="Vasya", surname="Pupkin",
                                   middle_name="Petrovich", client_type=ClientType.NEW, sex=Sex.MALE,
                                   bday=BDay.VALID_FIRST_AVAILABLE_NUMBERS, bday_words=BDay.VALID_FIRST_AVAILABLE_WORDS,
                                   email=Email.VALID, address= "1311313 131313 131313")
    #phone="8888000058",

    def __init__(self, driver):
        super().__init__(driver)

    # @pytest.mark.login
    # def test_negative_registration(self):
    #     """
    #     Simple login
    #     Validate registration form each field and warning messages
    #     """
    #     self.logger.info("Negative registration")
    #     patient = self.NEGATIVE_REG_PATIENT
    #     self.logger.info(patient.phone)
    #     if App.is_exist(self, AllowLocationScreen.skipLocationButton) == True:
    #         App.click(self, AllowLocationScreen.skipLocationButton)
    #         App.click(self, CitySelectionScreen.spb_city)
    #         App.click(self, CitySelectionScreen.continue_button)
    #         App.click(self, WelcomeTutorialScreen.skip_tutorial_button)
    #     App.click(self, SignInButtonScreen.button)
    #     App.wait_until_clickable(self, SignInPhoneScreen.phone_input)
    #     App.click(self, SignInPhoneScreen.phone_input)
    #     # print("\n\n" + patient.phone + "\n\n")
    #     App.send_keys(self, SignInPhoneScreen.phone_input, patient.phone)
    #     App.click(self, SignInPhoneScreen.next_button)
    #     App.click(self, SignInPasswordScreen.new_password_input)
    #     App.wait_until_clickable(self, SignInPasswordScreen.new_password_input)
    #     App.send_keys(self, SignInPasswordScreen.new_password_input, patient.password)
    #     # App.send_keys(self, SignInPasswordScreen.password_input, patient.password)
    #     App.click(self, SignInPasswordScreen.signin_button)
    #     code = App.get_activation_code(self, patient.phone).split(":")[1].strip()
    #     self.logger.error(f"\n\nCODE = '{code}'\n\n")
    #     App.send_key_events(self, code)
    #     # Test registration form
    #     for client_type in ClientType.CLIENT_TYPE_LIST:
    #         App.click(self, FillNewClientDataScreen.client_type_input)
    #         if client_type == ClientType.NEW:
    #             App.click(self, FillNewClientDataScreen.iam_new_client_option)
    #         elif client_type == ClientType.EXISTING:
    #             App.click(self, FillNewClientDataScreen.iam_existing_client_option)
    #         elif client_type == ClientType.VOLUNTARY_HEALTH_INSURANCE:
    #             App.click(self, FillNewClientDataScreen.i_have_voluntary_health_insurance)
    #         for sex in Sex.SEX_LIST:
    #             App.click(self, FillNewClientDataScreen.sex_input)
    #             if sex == Sex.FEMALE:
    #                 App.click(self, FillNewClientDataScreen.sex_option_female)
    #             elif sex == Sex.MALE:
    #                 App.click(self, FillNewClientDataScreen.sex_option_male)
    #             for bday in BDay.INVALID_DATE_LIST:
    #                 App.send_keys(self, FillNewClientDataScreen.bday_input, bday)
    #                 App.click(self, FillNewClientDataScreen.submit_button)
    #                 if bday == EMPTY:
    #                     App.wait_until_exists(self, FillNewClientDataScreen.empty_bday_warning)
    #                 elif bday == BDay.INVALID_YEAR_EARLY:
    #                     App.wait_until_exists(self, FillNewClientDataScreen.yearly_bday_warning)
    #                 else:
    #                     App.wait_until_exists(self, FillNewClientDataScreen.incorrect_bday_warning)
    #             for email in Email.INVALID_EMAIL_LIST:
    #                 App.send_keys(self, FillNewClientDataScreen.email_input, email)
    #                 App.click(self, FillNewClientDataScreen.submit_button)
    #                 App.wait_until_exists(self, FillNewClientDataScreen.email_incorrect_format_warning)
    #     App.wait_until_exists(self, FillNewClientDataScreen.empty_name_warning)
    #     App.wait_until_exists(self, FillNewClientDataScreen.empty_2nd_name_warning)
    #     # App.wait_until_exists(self, FillNewClientDataScreen.empty_3rd_name_warning)
    #     App.wait_until_exists(self, FillNewClientDataScreen.name_invalid_warning)
    #
    #     App.send_keys(self, FillNewClientDataScreen.name_input, FirstName.INVALID_SPECIAL_SYMBOL)
    #     App.send_keys(self, FillNewClientDataScreen.surname_input, SecondName.INVALID_SPECIAL_SYMBOL)
    #     App.send_keys(self, FillNewClientDataScreen.middle_name_input, MiddleName.INVALID_SPECIAL_SYMBOL)
    #     App.click(self, FillNewClientDataScreen.submit_button)
    #     # https://medsi.myjetbrains.com/youtrack/issue/SM-235
    #     # App.assert_size(self, FillNewClientDataScreen.name_invalid_warning, "equal to 3")
    #     FillNewClientDataScreen.fillForm(self, self.POSITIVE_REG_PATIENT)
    #     App.send_keys(self, FillNewClientDataScreen.bday_input, BDay.INVALID_TOO_YOUNG)
    #     App.click(self, FillNewClientDataScreen.submit_button)
    #     sleep(2)
    #     App.click(self, FillNewClientDataScreen.submit_button)
    #     App.click(self, FillNewClientDataScreen.submit_button)
    #     App.wait_until_exists(self, FillNewClientDataScreen.bday_too_young)


    # @pytest.mark.login
    # def test_positive_registration_new_data_verification(self):
    #     self.logger.info("Positive registration")
    #     patient = self.POSITIVE_REG_PATIENT.get_clone()
    #     if App.is_exist(self, AllowLocationScreen.skipLocationButton) == True:
    #         App.click(self, AllowLocationScreen.skipLocationButton)
    #         App.click(self, CitySelectionScreen.spb_city)
    #         App.click(self, CitySelectionScreen.continue_button)
    #         App.click(self, WelcomeTutorialScreen.skip_tutorial_button)
    #     else:
    #         pass
    #     App.click(self, SignInButtonScreen.button)
    #     App.click(self, SignInPhoneScreen.phone_input)
    #     App.send_keys(self, SignInPhoneScreen.phone_input, patient.phone)
    #     print("\n\n\n PHONE = " + patient.phone + "\n\n\n")
    #     App.click(self, SignInPhoneScreen.next_button)
    #     App.send_keys(self, SignInPasswordScreen.new_password_input, patient.password)
    #     # App.send_keys(self, SignInPasswordScreen.password_input, patient.password)
    #     App.click(self, SignInPasswordScreen.signin_button)
    #     code = App.get_activation_code(self, patient.phone).split(":")[1].strip()
    #     self.logger.info(f"\n\nCODE = '{code}'\n\n")
    #     App.send_key_events(self, code)
    #     FillNewClientDataScreen.fillForm(self, patient)
    #     App.click(self, FillNewClientDataScreen.submit_button)
    #     sleep(10)
    #     App.click(self, FillNewClientDataScreen.submit_button)
    #     for i in range(4):
    #         App.click(self, CommonScreen.code_zero)
    #     sleep(2)
    #     for i in range(4):
    #         App.click(self, CommonScreen.code_zero)
    #     sleep(2)
    #     App.click(self, WelcomeTutorialScreen.not_use_fingerprint)
    #     App.wait_until_exists(self, PromoScreen.November25Years.image)
    #     App.click(self, PromoScreen.November25Years.close_view)
    #     App.wait_until_exists(self, HomeScreen.main_header)
    #     App.click(self, BottomMenuScreen.more_option)
    #     App.click(self, MoreOptionScreen.root_user)
    #     App.wait_until_exists(self, ProfileScreen.phone_text)
    #     sleep(30)
    #     ProfileScreen.verify_user_data(self, patient)
    #     LoginScreen.profile_logout(self)
