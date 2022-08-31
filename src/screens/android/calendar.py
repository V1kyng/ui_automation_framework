from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class CalendarScreen(App):
     """
     Calendar screen locators
     """

     def __init__(self):
          super().__init__()

     date_is_monday = (MobileBy.ID, "ru.mts.smartmed.dev:id/title_date_1_1")
     date_is_wednesday = (MobileBy.ID, "ru.mts.smartmed.dev:id/title_date_1_3")
     date_is_thursday = (MobileBy.ID, "ru.mts.smartmed.dev:id/title_date_1_4")
     date_is_friday = (MobileBy.ID, "ru.mts.smartmed.dev:id/title_date_1_5")
     calendar_right_arrow = (MobileBy.ID, "ru.mts.smartmed.dev:id/arrowRightImageView")