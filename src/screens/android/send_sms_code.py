from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SendSmsCodeScreen(App):
    """
    send sms code screen
    """
    NUMERIC_KEYBOARD = {"0": 7, "1": 8, "2": 9, "3": 10, "4": 11, "5": 12, "6": 13, "7": 14, "8": 15, "9": 16}
    skip_location_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/permission_location_skip")
    # code_frame = (MobileBy.XPATH, "//android.widget.LinearLayout[@resource-id='ru.mts.smartmed.dev:id/linDottedChars"
    #                               "']/android.widget.FrameLayout")
    code_frame = (MobileBy.XPATH, "/ hierarchy / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.view.ViewGroup / android.view.ViewGroup / android.widget.FrameLayout / android.widget.FrameLayout / android.view.ViewGroup / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.LinearLayout / \
      android.widget.FrameLayout[1]")

    def enter_sms_code(self, code):
        self.driver.implicitly_wait(5)
        for char in code:
            self.driver.keyevent(self.NUMERIC_KEYBOARD[char])

