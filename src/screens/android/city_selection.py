from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class CitySelectionScreen(App):
    """
    city selection screen 
    """
    def __init__(self):
        super().__init__()

    spb_city = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Санкт-Петербург')]")
    moscow_city = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Москва')]")
    continue_button = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Далее')]")
