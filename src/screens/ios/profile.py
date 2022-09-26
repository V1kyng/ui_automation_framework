from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App
from src.screens.ios.fill_new_client_data import FillNewClientDataScreen


class ProfileScreen(FillNewClientDataScreen):
    """
    Home screen locators
    """

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
