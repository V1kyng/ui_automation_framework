from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class SignInButtonScreen(App):
    """
    Signing button screen
    """

    button = (MobileBy.ID, "ru.mts.smartmed.dev:id/button_text")

    def click_to_login_btn(self):
        self.find_clickable_element(self.button).click()