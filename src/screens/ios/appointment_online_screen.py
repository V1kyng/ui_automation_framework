from appium.webdriver.common.mobileby import MobileBy
import datetime

from src.helpers.app import App
from src.helpers.ios.date_time import DateTimeHelper


class AppointmentOnlineScreen(App):
    """
    online appointment tests screen locators
    """

    def swipe_top_to_bottom_until_visible(self, locator):
        for i in range(5):
            App.swipe_top_to_bottom(self)
            if App.is_exist(self, locator):
                break

    def choose_next_date(self):
        weekday = datetime.datetime.today().weekday()
        if weekday == 6:
            App.swipe_right_to_left(self, startx=290, starty=278, endx=200, endy=278)
            App.wait_until_exists(self, MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_next_day())
            App.click(self, MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_next_day())
        else:
            App.click(self, MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_next_day())

    loading = (MobileBy.ACCESSIBILITY_ID, "Выберите специалиста")
    choose_therapist = (MobileBy.ACCESSIBILITY_ID, "Терапевт")
    choose_otolaryngologist = (MobileBy.ACCESSIBILITY_ID, "Лор")
    choose_current_date = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_current_day())
    # choose_next_date = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_next_day())
    choose_date_negative = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_past_day())
    # choose_time = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_round_time())
    choose_nearest_time = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell["
                                           "5]//XCUIElementTypeStaticText")
    choose_next_time = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell["
                                        "5]//XCUIElementTypeStaticText[3]")

    all_clear_button = (MobileBy.ACCESSIBILITY_ID, "Все понятно")
    information = (MobileBy.ACCESSIBILITY_ID, "публичной оферты")
    go_back_button = (MobileBy.ACCESSIBILITY_ID, "Back")
    checkbox = (MobileBy.ACCESSIBILITY_ID, "ic no check")
    # cart_not_exist = (MobileBy.ACCESSIBILITY_ID, "Выберите способ оплаты")
    pay_button = (MobileBy.ACCESSIBILITY_ID, "Оплатить")
    add_to_calendar = (MobileBy.ACCESSIBILITY_ID, "Закрыть")
    allow_access_to_calendar = (MobileBy.ACCESSIBILITY_ID, "OK")
    event_added = (MobileBy.ACCESSIBILITY_ID, "ОК")
    success = (MobileBy.ACCESSIBILITY_ID, "Заявка отправлена")
    allow_access_to_microphone = (MobileBy.XPATH, "//XCUIElementTypeWindow[10]//XCUIElementTypeScrollView["
                                                  "2]//XCUIElementTypeOther//XCUIElementTypeOther"
                                                  "//XCUIElementTypeOther[3]//XCUIElementTypeButton")
    allow_access_to_camera = (MobileBy.ACCESSIBILITY_ID, "Ok")
