from appium.webdriver.common.mobileby import MobileBy
from src.helpers.app import App


class BankCardScreen(App):
    card_number_field = (MobileBy.ACCESSIBILITY_ID, "0000 0000 0000 0000")
    validity_month = (MobileBy.ACCESSIBILITY_ID, "MM")
    validity_year = (MobileBy.ACCESSIBILITY_ID, "ГГ")
    cvv = (MobileBy.XPATH, "//XCUIElementTypeWebView//XCUIElementTypeOther//XCUIElementTypeOther["
                           "7]//XCUIElementTypeTextField")
    owner = (MobileBy.ACCESSIBILITY_ID, "IVAN IVANOV")
    pay_button = (MobileBy.ACCESSIBILITY_ID, "Оплатить")
    validation_password = (MobileBy.ACCESSIBILITY_ID, "********")
    information_checkbox = (MobileBy.ACCESSIBILITY_ID, "ic no check")
    information = (MobileBy.ACCESSIBILITY_ID, "публичной оферты")
    go_back_button = (MobileBy.ACCESSIBILITY_ID, "Back")

    # feature "choose a payment method"
    payment_method = (MobileBy.ACCESSIBILITY_ID, "Способ оплаты")
    #payment_method = (MobileBy.XPATH,"XCUIElementTypeTable//XCUIElementTypeCell[6]//XCUIElementTypeOther//XCUIElementTypeOther")
    rolling_menu = (MobileBy.ACCESSIBILITY_ID, "Выберите способ оплаты")
    new_card = (MobileBy.ACCESSIBILITY_ID, "Новая карта")
    first_card = (MobileBy.XPATH, "XCUIElementTypeTable[2]//XCUIElementTypeCell[2]//XCUIElementTypeStaticText")
    second_card = (MobileBy.XPATH, "XCUIElementTypeTable[2]//XCUIElementTypeCell[3]//XCUIElementTypeStaticText")
