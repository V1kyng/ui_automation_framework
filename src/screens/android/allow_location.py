from appium.webdriver.common.mobileby import MobileBy
from src.helpers.app import App



class AllowLocationScreen(App):
    """
    location screen locators
    """
    def __init__(self):
        super().__init__()

    skipLocationButton = (MobileBy.ID, "ru.mts.smartmed.dev:id/permission_location_skip")
    permitLocationButton = (MobileBy.ID, "ru.mts.smartmed.dev:id/permission_location_request_button")