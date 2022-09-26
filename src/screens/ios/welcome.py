import allure

from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class WelcomeTutorialScreen(App):
    """
    welcome screen
    """

    # SKIP_TUTORIAL_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Пропустить")
    SKIP_TUTORIAL_BUTTON = (MobileBy.XPATH, "//XCUIElementTypeButton/XCUIElementTypeStaticText[@name='Пропустить']")
    text_area = (MobileBy.ACCESSIBILITY_ID, "ic_region_tutorial_welcome_smartmed")
    next_tutorial_button = (MobileBy.ACCESSIBILITY_ID, "Далее")

    def skip_tutorial_button(self):
        with allure.step("Skip tutorial button"):
            self.find_clickable_element(self.SKIP_TUTORIAL_BUTTON).click()
