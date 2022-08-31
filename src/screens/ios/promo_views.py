from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class PromoScreen(App):
    """
    Promo screen locators
    """

    class November25Years():
        image = (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeImage')
        close_button = (MobileBy.ACCESSIBILITY_ID, '✕')

    close_button = (MobileBy.ACCESSIBILITY_ID, '✕')

    def __init__(self, driver):
        super().__init__()