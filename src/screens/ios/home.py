from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App
from src.screens.ios.bottom_menu import BottomMenuScreen


class HomeScreen(App):
    """
    Home screen locators
    """

    main_header = (MobileBy.ACCESSIBILITY_ID, 'Главная')
    # doctors_bottom = (MobileBy.ACCESSIBILITY_ID, 'Врачи')
    doctors_bottom = (MobileBy.XPATH, '//XCUIElementTypeTabBar/XCUIElementTypeButton[@name="Врачи"]')
    online_consultation = (MobileBy.ACCESSIBILITY_ID, "Онлайн-консультация")
    analysis_button = (MobileBy.ACCESSIBILITY_ID, "Сдать анализы")

    carousel_maintenance = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Ведутся технические работы"]')
    carousel_liposuction = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Скидка 15% на липосакцию"]')
    carousel_motherschool = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Школа мам Бесплатный курс "]')

    carousel_image_close = (MobileBy.ACCESSIBILITY_ID, "ic stories close button")
    carousel_image_enabled = (MobileBy.XPATH, '//XCUIElementTypeImage[@enabled="true"]')
    carousel_image_disabled = (MobileBy.XPATH, '//XCUIElementTypeImage[@enabled="false"]')
    carousel_mywallet = (MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Мой кошелёк")]')
    carousel_specificdoctor = (MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Врачи узкого профиля на дому")]')
    carousel_pharmacy = (MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Аптека в SmartMed")]')

    def get_app_main_page(self):
        App.click(self, BottomMenuScreen.home_option)
        App.wait_until_exists(self, HomeScreen.main_header)

    def verify_image_shown(self):
        App.wait_until_exists(self, HomeScreen.carousel_image_enabled)
        assert len(App.elements(self, HomeScreen.carousel_image_enabled)) == 1

    def verify_image_hidden(self):
        App.wait_until_exists(self, HomeScreen.carousel_image_enabled)
        assert len(App.elements(self, HomeScreen.carousel_image_enabled)) > 1

    def __init__(self, driver):
        super().__init__()

