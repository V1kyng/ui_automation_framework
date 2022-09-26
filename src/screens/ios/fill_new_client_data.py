from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


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
