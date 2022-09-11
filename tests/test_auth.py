from src.screens.ios.login_screen import LoginScreen
from src.screens.ios.welcome import WelcomeTutorialScreen


class TestAuthorization:

    def test_auth(self, driver):
        welcome_screen = WelcomeTutorialScreen(driver)
        welcome_screen.skip_tutorial_button()
        login_screen = LoginScreen(driver)
        login_screen.click_to_login_btn()

