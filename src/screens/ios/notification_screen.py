from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class NotificationScreen(App):
    """
    Allow notification screen
    """

    def __init__(self, driver):
        super().__init__()

    skipNotificationButton = (MobileBy.ACCESSIBILITY_ID, "Don’t Allow")
    permitNotificationButton = (MobileBy.ACCESSIBILITY_ID, "Allow")
    skipNotificationButtonRu = (MobileBy.ACCESSIBILITY_ID, "Отмена")
    skipNotificationSettingsRu = (MobileBy.ACCESSIBILITY_ID, "Отменить")
    # skipNotificationButtonRuX = (MobileBy.XPATH, '//XCUIElementTypeAlert//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton')
    skipNotificationButtonRuX = (MobileBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton')