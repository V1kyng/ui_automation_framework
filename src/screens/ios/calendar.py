from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class CalendarScreen(App):
    """
    Home screen locators
    """

    calendar_right_arrow = (MobileBy.XPATH, '//XCUIElementTypeTable//XCUIElementTypeButton[2]')
    date_is_monday = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[8]')
    date_is_tuesday = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[9]')


    def __init__(self, driver):
        super().__init__()