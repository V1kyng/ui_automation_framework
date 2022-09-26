from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SignInPhoneScreen(App):
    """
    Send phone number
    """
    phone_input = (MobileBy.IOS_PREDICATE, "type == 'XCUIElementTypeTextField'")
    # phone_input = (MobileBy.XPATH, "//XCUIElementTypeOther/XCUIElementTypeTextField")
    next_button = (MobileBy.ACCESSIBILITY_ID, "Далее")
    clear_button = (MobileBy.ACCESSIBILITY_ID, "ic clear button")
