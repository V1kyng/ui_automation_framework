from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App
from src.screens.android.bottom_menu import BottomMenuScreen
from src.screens.android.common import CommonScreen


class HomeScreen:
    """
    Home screen locators
    """

    main_header = (MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="Главная"]')
    online_consultation = (MobileBy.ID, "ru.mts.smartmed.dev:id/dashboard_order_consultation_layout")
    offline_consultation = (MobileBy.ID, "ru.mts.smartmed.dev:id/dashboard_order_clinic_layout")
    doctors_bottom = (MobileBy.ID, "ru.mts.smartmed.dev:id/bottom_menu_doctors")

    def get_app_main_page(self):
        App.click(self, BottomMenuScreen.home_option)
        App.wait_until_exists(self, HomeScreen.main_header)
