from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class WelcomeTutorialScreen(App):
    """
    welcome screen
    """

    def __init__(self, driver):
        super().__init__()

    skip_tutorial_button = (MobileBy.ACCESSIBILITY_ID, "Пропустить")
    text_area = (MobileBy.ACCESSIBILITY_ID, "ic_region_tutorial_welcome_smartmed")
    next_tutorial_button = (MobileBy.ACCESSIBILITY_ID, "Далее")