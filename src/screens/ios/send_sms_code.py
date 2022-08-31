from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SendSmsCodeScreen(App):
    """
    send sms code screen
    """

    def __init__(self, driver):
        super().__init__()

#    skip_location_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/permission_location_skip")
    code_frame = (MobileBy.IOS_PREDICATE, "type == 'XCUIElementTypeTextField'")

