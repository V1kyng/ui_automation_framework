from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App
from src.model.AppDataModel import Patient
from src.model.MedsiConstants import ClientType, Sex, BDay, EMPTY, Email


class FillNewClientDataScreen(App):
    """
    fill new client data
    """
    iam_new_client_option = (MobileBy.ACCESSIBILITY_ID, 'Я новый клиент')
    iam_existing_client_option = (MobileBy.ACCESSIBILITY_ID, 'Я уже был в Медси')
    i_have_voluntary_health_insurance = (MobileBy.ACCESSIBILITY_ID, 'У меня есть ДМС')
    surname_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField')
    name_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
    middle_name_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField')
    no_middle_name_checkbox = (MobileBy.ACCESSIBILITY_ID, 'ic checkbox square')
    no_middle_name_checkbox_description = (MobileBy.ACCESSIBILITY_ID, 'По паспорту без отчества')
    sex_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
    bday_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
    email_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[7]/XCUIElementTypeTextField')
    address_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeTextField')
    submit_button = (MobileBy.ACCESSIBILITY_ID, 'Готово')
    back_button = (MobileBy.ACCESSIBILITY_ID, 'Back')
    datePickerWheel = (MobileBy.XPATH, "//XCUIElementTypePickerWheel")

    # warning messages
    email_incorrect_format_warning = (MobileBy.ACCESSIBILITY_ID, "Проверьте указанный email")
    empty_bday_warning = (MobileBy.ACCESSIBILITY_ID, "Выберите дату рождения")
    empty_2nd_name_warning = (MobileBy.ACCESSIBILITY_ID, "Введите фамилию")
    empty_name_warning = (MobileBy.ACCESSIBILITY_ID, "Введите имя")
    empty_3rd_name_warning = (MobileBy.ACCESSIBILITY_ID, "Введите отчество")
    name_invalid_warning = (MobileBy.ACCESSIBILITY_ID, "Поле может содержать буквы кириллицы или латиницы, цифры, дефис, пробел")
    bday_too_young = (MobileBy.ACCESSIBILITY_ID, "Регистрация в приложении разрешена только пользователям от 18 лет.")

    def __init__(self, driver):
        super().__init__()


    def setSex(self, patient: Patient):
        App.element(self, FillNewClientDataScreen.datePickerWheel).set_value(patient.sex)

    def setBDay(self, patient: Patient):
        date_picker_wheels_list = App.elements(self, FillNewClientDataScreen.datePickerWheel)
        bday_list = patient.bday.split(' ')
        date_picker_wheels_list[0].set_value(bday_list[0])
        date_picker_wheels_list[1].set_value(bday_list[1])
        date_picker_wheels_list[2].set_value(bday_list[2])
        
    def fillForm(self, patient: Patient):
        if patient.client_type == ClientType.NEW:
            App.click(self, FillNewClientDataScreen.iam_new_client_option)
        elif patient.client_type == ClientType.EXISTING:
            App.click(self, FillNewClientDataScreen.iam_existing_client_option)
        elif patient.client_type == ClientType.VOLUNTARY_HEALTH_INSURANCE:
            App.click(self, FillNewClientDataScreen.i_have_voluntary_health_insurance)
        App.send_keys(self, FillNewClientDataScreen.address_input, patient.address)
        App.send_keys(self, FillNewClientDataScreen.email_input, patient.email)
        App.click(self, FillNewClientDataScreen.sex_input)
        FillNewClientDataScreen.setSex(self, patient)
        App.click(self, FillNewClientDataScreen.bday_input)
        FillNewClientDataScreen.setBDay(self, patient)
        App.send_keys(self, FillNewClientDataScreen.name_input, patient.name)
        App.send_keys(self, FillNewClientDataScreen.surname_input, patient.surname)
        App.send_keys(self, FillNewClientDataScreen.middle_name_input, patient.middle_name)


    def fillFormNegative(self, patient: Patient):
        for client_type in ClientType.CLIENT_TYPE_LIST:
            if client_type == ClientType.NEW:
                App.click(self, FillNewClientDataScreen.iam_new_client_option)
            elif client_type == ClientType.EXISTING:
                App.click(self, FillNewClientDataScreen.iam_existing_client_option)
            elif client_type == ClientType.VOLUNTARY_HEALTH_INSURANCE:
                App.click(self, FillNewClientDataScreen.i_have_voluntary_health_insurance)
            App.click(self, FillNewClientDataScreen.sex_input)
            FillNewClientDataScreen.setSex(self, patient)
            App.click(self, FillNewClientDataScreen.submit_button)
            App.wait_until_exists(self, FillNewClientDataScreen.empty_bday_warning)
            for email in Email.INVALID_EMAIL_LIST:
                App.click(self, FillNewClientDataScreen.email_input)
                App.send_keys(self, FillNewClientDataScreen.email_input, email)
                App.click(self, FillNewClientDataScreen.submit_button)
                App.wait_until_exists(self, FillNewClientDataScreen.email_incorrect_format_warning)
            App.click(self, FillNewClientDataScreen.back_button)