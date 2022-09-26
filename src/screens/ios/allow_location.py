from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App

class AllowLocationScreen(App):
    """
    location screen locators
    """
    skipLocationButton = (MobileBy.ACCESSIBILITY_ID, "Don’t Allow")
    permitLocationButton = (MobileBy.ACCESSIBILITY_ID, "Allow")
