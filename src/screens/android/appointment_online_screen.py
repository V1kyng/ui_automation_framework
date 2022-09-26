from appium.webdriver.common.mobileby import MobileBy
import datetime

from src.helpers.app import App
from src.helpers.ios.date_time import DateTimeHelper


class AppointmentOnlineScreen(App):
    """
    online appointment tests screen locators
    """

    specialist = (MobileBy.ID, "ru.mts.smartmed.dev:id/title")
    first_specialist = (MobileBy.XPATH, "//android.view.ViewGroup[1]/android.widget.TextView[1]")

    choose_therapist = (MobileBy.XPATH, "//android.widget.TextView[1][@text='Терапевт']")
    choose_otolaryngologist = (MobileBy.XPATH, "//android.widget.TextView[1][@text='Лор']")
    current_date = (MobileBy.XPATH, f"//android.widget.TextView[@text='{DateTimeHelper().get_current_day()}']")  # для андроида такой же хелпер?
    date_negative = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_past_day())  # для андроида такой же хелпер?
    nearest_time = (MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.TextView")
    next_time = (MobileBy.XPATH, "//android.widget.FrameLayout[2]/android.widget.TextView")

    all_clear_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/continue_button")
    information = (MobileBy.ID, "ru.mts.smartmed.dev:id/agreement_label")
    go_back_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/left_item")
    checkbox = (MobileBy.ID, "ru.mts.smartmed.dev:id/agreement_icon")
    # cart_not_exist = (MobileBy.ACCESSIBILITY_ID, "Выберите способ оплаты")
    pay_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/pay_button")
    add_to_calendar = (MobileBy.ID, "ru.mts.smartmed.dev:id/chat_add_to_calendar")
    allow_access_to_calendar = (
    MobileBy.ACCESSIBILITY_ID, "OK")  # в инспекторе на андроиде не открывается системное меню
    event_added = (MobileBy.ACCESSIBILITY_ID, "ОК")  # нет в андроиде в записи на онлайн
    success = (MobileBy.ACCESSIBILITY_ID, "Заявка отправлена")  # пока без этого локатора
    allow_access_to_microphone = (MobileBy.XPATH, "//XCUIElementTypeWindow[10]//XCUIElementTypeScrollView["
                                                  "2]//XCUIElementTypeOther//XCUIElementTypeOther"
                                                  "//XCUIElementTypeOther[3]//XCUIElementTypeButton")  # это в какой момент?
    allow_access_to_camera = (MobileBy.ACCESSIBILITY_ID, "Ok")  # это в какой момент?

    def swipe_to_element(self, locator):  # TODO stabilize
        element = self.find_visible_elem(locator=locator, timeout=1)
        while not element:
            self.driver.swipe(start_x=75, start_y=500, end_x=75,
                              end_y=0, duration=100)
            element = self.find_visible_elem(locator)

    def choose_specialist(self):
        btn = self.find_clickable_element(self.choose_therapist)
        btn.click()

    def choose_next_date(self):
        weekday = datetime.datetime.today().weekday()
        # if weekday == 6:  # handle sunday
        #     self.find_element((MobileBy.ID, "ru.mts.smartmed.devnochuck:id/arrowRightImageView")).click()
        #     self.find_element((MobileBy.XPATH, f"//android.widget.TextView[@text='{DateTimeHelper().get_next_day()}']"))
        #     self.find_clickable_element((MobileBy.XPATH, f"//android.widget.TextView[@text='{DateTimeHelper().get_next_day()}']")).click()
        # else:
        self.find_clickable_element((MobileBy.XPATH, f"//android.widget.TextView[@text='{DateTimeHelper().get_next_day()}']")).click()

    def choose_time_slot(self):
        print("inside choose_time_slot")
        btn = self.find_text(self.nearest_time)
        print("element is here")
        print("element is here")
        print("element is here")
        btn.click()

    def all_clear_button_click(self):
        self.find_clickable_element(self.all_clear_button).click()

    def check_information(self):
        self.find_clickable_element(self.information).click()
        self.find_clickable_element(self.go_back_button).click()

    def check_pay_button(self):
        self.find_clickable_element(self.pay_button)
