from src.screens.ios.home import HomeScreen
from src.screens.ios.login_screen import LoginScreen
from src.screens.ios.welcome import WelcomeTutorialScreen
from src.utils import get_activation_code
from src.data.patient import Patient


def ios_authorization(driver):
    welcome_screen = WelcomeTutorialScreen(driver)
    driver.switch_to.alert.dismiss()
    welcome_screen.skip_tutorial_button()
    login_screen = LoginScreen(driver)
    login_screen.click_to_login_btn()
    login_screen.fill_phone_number()
    login_screen.fill_password_field()
    code = get_activation_code(Patient.PHONE)
    login_screen.enter_sms_code(code)
    login_screen.enter_login_pin()
    login_screen.dont_allow_notification()
    home_screen = HomeScreen(driver)
    driver.terminate_app("ru.medsi.smartmed.dev")
    driver.launch_app()
    login_screen.enter_pin()
    home_screen.skip_notifications()
