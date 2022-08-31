from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SendSmsCodeScreen(App):
    """
    send sms code screen
    """
    skip_location_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/permission_location_skip")
    code_frame = (MobileBy.XPATH, "//android.widget.LinearLayout[@resource-id=\"ru.mts.smartmed.dev:id/linDottedChars\"]/*[1]")
