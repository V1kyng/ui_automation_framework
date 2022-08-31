from appium.webdriver.common.mobileby import MobileBy
from src.helpers.app import App
from src.helpers.ios.date_time import DateTimeHelper


class AnalysisScreen(App):
    """
    analysis tests screen locators
    """
    SEARCH_REQUEST = 'гем'
    CLINIC_SEARCH_REQUEST = 'мит'
    SEARCH_REQUEST_NEGATIVE = 'yyyyyyyy'

    @staticmethod
    def basket_check_item_counter(x: int) -> tuple:
        """
        check number of items in basket screen
        :param x: int (number of items for checking)
        :return: locator (MobileBy.ACCESSIBILITY_ID, string)
        """
        finals = "ов"
        if x == 1:
            result = "{} анализ".format(x)
        else:
            result = "{} анализ{}".format(x, finals)
        return MobileBy.ACCESSIBILITY_ID, result

    def basket_check_price(self, x: int):
        # get sum of items price
        items_price = 0
        for i in range(x):
            empty_str = ''
            locator = (MobileBy.XPATH,
                       "//XCUIElementTypeTable//XCUIElementTypeCell[{}]//XCUIElementTypeStaticText[2]".format(i + 1))
            element = App.element(self, locator=locator)
            for m in element.text:
                if m.isdigit():
                    empty_str = empty_str + m
            items_price = int(items_price) + int(empty_str)
        print(items_price)
        # get basket sum
        basket_sum_locator = (MobileBy.XPATH, "//XCUIElementTypeOther[2]//XCUIElementTypeOther//XCUIElementTypeOther"
                                              "//XCUIElementTypeOther/XCUIElementTypeOther//XCUIElementTypeOther"
                                              "//XCUIElementTypeStaticText[1]")
        basket_sum_web_element = App.element(self, locator=basket_sum_locator)
        empty_str2 = ''
        for m in basket_sum_web_element.text:
            if m.isdigit():
                empty_str2 = empty_str2 + m
        basket_sum = int(empty_str2)
        print(basket_sum)
        assert items_price == basket_sum, "sum of items not equal to basket sum"

    all_clear = (MobileBy.ACCESSIBILITY_ID, "Всё понятно")
    search_field = (MobileBy.ACCESSIBILITY_ID, "Название анализа")
    add_first_item = (MobileBy.ACCESSIBILITY_ID, "Добавить")

    add_second_item = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell["
                                       "2]//XCUIElementTypeButton//XCUIElementTypeStaticText")
    add_third_item = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell["
                                      "3]//XCUIElementTypeButton//XCUIElementTypeStaticText")
    first_item_price = "//XCUIElementTypeTable//XCUIElementTypeCell[1]//XCUIElementTypeStaticText[2]"
    second_item_price = "//XCUIElementTypeTable//XCUIElementTypeCell[2]//XCUIElementTypeStaticText[2]"
    third_item_price = "//XCUIElementTypeTable//XCUIElementTypeCell[3]//XCUIElementTypeStaticText[2]"
    # basket_sum = "/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther" \
    #              "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[1] "
    cancel_button = (MobileBy.ACCESSIBILITY_ID, "Cancel")
    basket_button = (MobileBy.ACCESSIBILITY_ID, "Корзина")
    close_basket_screen = (MobileBy.ACCESSIBILITY_ID, "ic close calendar")
    first_item = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell[1]//XCUIElementTypeStaticText[1]")
    second_item = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell[2]//XCUIElementTypeStaticText[1]")
    delete_by_swipe = (MobileBy.ACCESSIBILITY_ID, "Delete")
    trash = (MobileBy.ACCESSIBILITY_ID, "ic delete")
    trash_cancel_delete = (MobileBy.ACCESSIBILITY_ID, "Оставить")
    trash_delete = (MobileBy.ACCESSIBILITY_ID, "Удалить")
    choose_clinic = (MobileBy.ACCESSIBILITY_ID, "Выбрать клинику")
    to_list_option = (MobileBy.ACCESSIBILITY_ID, "Список")
    clinic_search_field = (MobileBy.ACCESSIBILITY_ID, "Поиск клиники")
    clinic_search_result = (MobileBy.ACCESSIBILITY_ID, "Клиника на Дмитровском шоссе")
    any_clinic_search_result = (MobileBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell")
    date = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_current_day())
    negative_date = (MobileBy.ACCESSIBILITY_ID, DateTimeHelper().get_past_day())
    choose_date_button = (MobileBy.ACCESSIBILITY_ID, "Выбрать дату")

    # information_checkbox = (MobileBy.ACCESSIBILITY_ID, "") # TODO find locator after bug fix

    # first_item X=0 Y=97 width=390 height= 128 (X=304 - price)
    # second_item X=0 Y=224 width=390 height= 128 (X=304 - price)
