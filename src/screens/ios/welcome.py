from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class WelcomeTutorialScreen(App):
    """
    welcome screen
    """

    SKIP_TUTORIAL_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Пропустить")
    text_area = (MobileBy.ACCESSIBILITY_ID, "ic_region_tutorial_welcome_smartmed")
    next_tutorial_button = (MobileBy.ACCESSIBILITY_ID, "Далее")

    def skip_tutorial_button(self):
        self.find_element(self.SKIP_TUTORIAL_BUTTON).click()

