from appium.webdriver.common.mobileby import MobileBy
from src.helpers.app import App



class DoctorsScreen(App):
    """
    Doctors screen locators
    """

    cliniks = (MobileBy.ACCESSIBILITY_ID, 'Клиники')
    center_on_belarusskaya = (MobileBy.ACCESSIBILITY_ID, "Клинико-диагностический центр на Белорусской")
    sign_up_for_an_appointment_with = (MobileBy.ACCESSIBILITY_ID, 'Записаться на приём')
    all_doctors = (MobileBy.ACCESSIBILITY_ID, 'Все врачи')
    doctor_fio = (MobileBy.XPATH, '//XCUIElementTypeTable//XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]')
    doctor_fio_gag = (MobileBy.ACCESSIBILITY_ID, 'Гаджимурадов Абдула Гаджимурадович')
    doctor_fio_empty_in_consultation = (MobileBy.XPATH, '//XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]')
    doctor_fio_empty = (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]')

    def __init__(self, driver):
        super().__init__()