import time

from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class HomeScreen(App):
    """
    Home screen locators
    """

    main_header = (MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="Главная"]')
    online_consultation = (MobileBy.ID, "ru.mts.smartmed.dev:id/dashboard_order_consultation_layout")
    doctors_bottom = (MobileBy.ID, "ru.mts.smartmed.dev:id/bottom_menu_doctors")

    def click_to_appointment_online(self):
        time.sleep(4)
        btn = self.find_clickable_element(self.online_consultation)
        btn.click()
