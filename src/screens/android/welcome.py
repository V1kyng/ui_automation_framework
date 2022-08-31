from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class WelcomeTutorialScreen(App):
    """
    welcome screen
    """

    skip_tutorial_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/tutorial_region_skip")
    text_area = (MobileBy.ID, "ru.mts.smartmed.dev:id/tutorial_region_text")
    next_tutorial_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/tutorial_region_button_next")
    not_use_fingerprint = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Не использовать')]")