import time

from appium.webdriver.common.mobileby import MobileBy
import datetime

from src.helpers.app import App
from src.helpers.ios.date_time import DateTimeHelper


class AppointmentOnlineScreen(App):
    """
    online appointment tests screen locators
    """
    specialist = (MobileBy.ACCESSIBILITY_ID, "Выберите специалиста")
    first_specialist = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell[2]")
    choose_therapist = (MobileBy.ACCESSIBILITY_ID, "Терапевт")
    choose_otolaryngologist = (MobileBy.ACCESSIBILITY_ID, "Лор")
    current_date = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_current_day())
    # choose_next_date = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_next_day())
    date_negative = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_past_day())
    # choose_time = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_round_time())
    get_next_week = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell["
                                     "3]//XCUIElementTypeButton[2]")
    nearest_time = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell["
                                    "5]//XCUIElementTypeStaticText")
    next_time = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell["
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

    def scroll_to(self, locator):  # TODO stabilize
        if self.find_visible_elem(self.first_specialist):
            for i in range(5):
                self.driver.swipe(start_x=75, start_y=500, end_x=75,
                                  end_y=0, duration=100)
                if self.find_element(locator):
                    break

    def choose_specialist(self, locator):
        btn = self.find_clickable_element(locator)
        btn.click()

    def choose_next_date(self):
        weekday = datetime.datetime.today().weekday()
        if weekday == 6:  # handle sunday
            time.sleep(2)
            self.swipe_after_load_element(start_x=290, start_y=278, end_x=200, end_y=278, duration=100,
                                          waiting_elem=self.current_date)
            self.find_text(
                (MobileBy.ACCESSIBILITY_ID, DateTimeHelper.get_day_after_tomorrow(DateTimeHelper()))).click()
        else:
            self.find_clickable_element((MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_day_after_tomorrow())).click()

    def choose_time_slot(self):
        self.find_clickable_element(self.nearest_time).click()

    def all_clear_button_click(self):
        self.find_clickable_element(self.all_clear_button).click()

    def check_information(self):
        self.find_clickable_element(self.information).click()
        self.find_clickable_element(self.go_back_button).click()

    def check_pay_button(self):
        self.find_clickable_element(self.pay_button)
