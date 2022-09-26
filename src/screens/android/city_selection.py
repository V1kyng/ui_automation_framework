from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class CitySelectionScreen(App):
    """
    city selection screen 
    """

    spb_city = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Санкт-Петербург')]")
    moscow_city = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Москва')]")
    continue_button = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Далее')]")

    def select_city(self):
        self.find_clickable_element(self.moscow_city).click()
        self.find_clickable_element(self.continue_button).click()
