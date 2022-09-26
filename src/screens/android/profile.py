from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App
from src.screens.android.fill_new_client_data import FillNewClientDataScreen


class ProfileScreen(FillNewClientDataScreen):
    """
    Home screen locators
    """
    phone_text = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_phone_text')
    logout_button = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_logout_item')
    name_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_first_name_text')
    surname_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_last_name_text')
    middle_name_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_patronymic_text')
    sex_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_gender_text')
    bday_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_birthday_text')
    email_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_email_text')
    address_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_address_text')
    profile_logout  = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_logout_item') # Выйти из профиля
    profile_exit = (MobileBy.ID, 'android:id/button1') # Выйти

    def verify_user_data(self, patient):
        assert App.element(self, ProfileScreen.name_input).text == patient.name, \
            f"{App.element(self, ProfileScreen.name_input).text} vs {patient.name}"
        assert App.element(self, ProfileScreen.surname_input).text == patient.surname, \
            f"{App.element(self, ProfileScreen.surname_input).text} vs {patient.surname}"
        assert App.element(self, ProfileScreen.middle_name_input).text == patient.middle_name, \
            f"{App.element(self, ProfileScreen.middle_name_input).text} vs {patient.middle_name}"
        assert App.element(self, ProfileScreen.sex_input).text == patient.sex, \
            f"{App.element(self, ProfileScreen.sex_input).text} vs {patient.sex}"
        assert App.element(self, ProfileScreen.bday_input).text == patient.bday_words, \
            f"{App.element(self, ProfileScreen.bday_input).text} vs {patient.bday_words}"
        assert App.element(self, ProfileScreen.phone_text).text == patient.phone_pretty, \
            f"{App.element(self, ProfileScreen.phone_text).text} vs {patient.phone_pretty}"
        assert App.element(self, ProfileScreen.email_input).text == patient.email, \
            f"{App.element(self, ProfileScreen.email_input).text} vs {patient.email}"
        assert App.element(self, ProfileScreen.address_input).text == patient.address, \
            f"{App.element(self, ProfileScreen.address_input).text} vs {patient.address}"
        



