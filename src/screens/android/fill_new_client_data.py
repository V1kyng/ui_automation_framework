from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class FillNewClientDataScreen(App):
    """
    fill new client data
    """
    client_type_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_type_text')
    iam_new_client_option = (MobileBy.ID, 'ru.mts.smartmed.dev:id/card1')
    iam_existing_client_option = (MobileBy.ID, 'ru.mts.smartmed.dev:id/card2')
    i_have_voluntary_health_insurance = (MobileBy.ID, 'ru.mts.smartmed.dev:id/card3')
    surname_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_second_name_text')
    name_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_name_text')
    middle_name_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_patronymic_text')
    no_middle_name_checkbox = (MobileBy.ID, 'ru.mts.smartmed.dev:id/patronymic_check_box')
    no_middle_name_checkbox_description = (MobileBy.ID, 'ru.mts.smartmed.dev:id/check_box_description')
    sex_input = (MobileBy.ID, 'ru.mts.smartmed.dev:id/profile_settings_gender_text')
    sex_option_male = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Мужской')]")
    sex_option_female = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Женский')]")
    bday_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/profile_settings_birthday_text")
    email_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/profile_settings_email_text")
    address_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/profile_settings_address_text")
    submit_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/profile_accept_icon")

    # warning messages
    email_incorrect_format_warning = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Неверный формат')]")
    incorrect_bday_warning = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Укажите корректную дату рождения')]")
    yearly_bday_warning = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Дата не должна быть раньше 01.01.1900')]")
    empty_bday_warning = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Введите дату рождения')]")
    empty_2nd_name_warning = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Введите фамилию')]")
    empty_name_warning = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Введите имя')]")
    empty_3rd_name_warning = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Введите отчество')]")
    name_invalid_warning = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Поле может содержать буквы кириллицы или латиницы, цифры, дефис, пробел')]")
    bday_too_young = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'Регистрация в приложении разрешена только пользователям от 18 лет.')]")

    # def fillForm(self, patient):
    #     App.click(self, FillNewClientDataScreen.client_type_input)
    #     if patient.client_type == ClientType.NEW:
    #         App.click(self, FillNewClientDataScreen.iam_new_client_option)
    #     elif patient.client_type == ClientType.EXISTING:
    #             App.click(self, FillNewClientDataScreen.iam_existing_client_option)
    #     elif patient.client_type == ClientType.VOLUNTARY_HEALTH_INSURANCE:
    #         App.click(self, FillNewClientDataScreen.i_have_voluntary_health_insurance)
    #
    #     App.click(self, FillNewClientDataScreen.sex_input)
    #     if patient.sex == Sex.FEMALE:
    #         App.click(self, FillNewClientDataScreen.sex_option_female)
    #     else:
    #         App.click(self, FillNewClientDataScreen.sex_option_male)
    #     App.send_keys(self, FillNewClientDataScreen.bday_input, patient.bday)
    #     App.send_keys(self, FillNewClientDataScreen.email_input, patient.email)
    #     App.send_keys(self, FillNewClientDataScreen.name_input, patient.name)
    #     App.send_keys(self, FillNewClientDataScreen.surname_input, patient.surname)
    #     App.send_keys(self, FillNewClientDataScreen.middle_name_input, patient.middle_name)
    #     App.send_keys(self, FillNewClientDataScreen.address_input, patient.address)
