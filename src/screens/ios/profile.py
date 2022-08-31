from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App
from src.model.AppDataModel import Patient
from src.screens.ios.fill_new_client_data import FillNewClientDataScreen


class ProfileScreen(FillNewClientDataScreen):
    """
    Home screen locators
    """

    def __init__(self, driver):
        super().__init__(driver)

    phone_text = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeTextField')
    logout_button = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[11]/XCUIElementTypeTextField')
    surname_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
    name_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField')
    middle_name_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
    sex_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
    bday_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[7]/XCUIElementTypeTextField')
    email_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextField')
    address_input = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeTextField')
    profile_logout = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Выйти из профиля"]')
    profile_exit = (MobileBy.ACCESSIBILITY_ID, "Выйти")

    def verify_user_data(self, patient: Patient):
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

        



