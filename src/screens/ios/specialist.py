from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SpecialistScreen(App):
    """
    Specialist screen locators
    """

    dont_know_exactly = (MobileBy.ACCESSIBILITY_ID, "Точно не знаю")
    search_edit = (MobileBy.ACCESSIBILITY_ID, "Найти")
    search_bar = (MobileBy.ACCESSIBILITY_ID, "Введите ФИО врача")
    search_by_fio = (MobileBy.ACCESSIBILITY_ID, "Поиск по ФИО")
    doctor_name = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]')
    doctor_name_in_clinic = (MobileBy.XPATH, '//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]')
    doctor_name_positive = (MobileBy.ACCESSIBILITY_ID, "Иванов Федор")
    first_row_doctor_name = (MobileBy.ACCESSIBILITY_ID, "Любой доступный врач")
    view_group2 = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[position()=2]')
    view_group5 = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[position()=5]')
    view_group6 = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[6]')