from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class HomeScreen(App):
    """
    Home screen locators
    """

    main_header = (MobileBy.ACCESSIBILITY_ID, 'Главная')
    doctors_bottom = (MobileBy.XPATH, '//XCUIElementTypeTabBar/XCUIElementTypeButton[@name="Врачи"]')
    online_consultation = (MobileBy.ACCESSIBILITY_ID, "Онлайн-консультация")
    analysis_button = (MobileBy.ACCESSIBILITY_ID, "Сдать анализы")
    notification = (MobileBy.ACCESSIBILITY_ID, "Больше не показывать")
    # notification = (MobileBy.XPATH, "//XCUIElementTypeAlert//XCUIElementTypeScrollView["
    #                                 "2]//XCUIElementTypeOther//XCUIElementTypeOther[3]//XCUIElementTypeButton["
    #                                 "@name='Больше не показывать']")
    information_popup = (MobileBy.ACCESSIBILITY_ID, "Информация")

    carousel_maintenance = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Ведутся технические работы"]')
    carousel_liposuction = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Скидка 15% на липосакцию"]')
    carousel_motherschool = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Школа мам Бесплатный курс "]')

    carousel_image_close = (MobileBy.ACCESSIBILITY_ID, "ic stories close button")
    carousel_image_enabled = (MobileBy.XPATH, '//XCUIElementTypeImage[@enabled="true"]')
    carousel_image_disabled = (MobileBy.XPATH, '//XCUIElementTypeImage[@enabled="false"]')
    carousel_mywallet = (MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Мой кошелёк")]')
    carousel_specificdoctor = (MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Врачи узкого профиля на дому")]')
    carousel_pharmacy = (MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Аптека в SmartMed")]')

    def go_to_online_consultation(self):
        self.find_visible_elem(self.online_consultation).click()

    def find_main_header(self):
        assert self.find_element(self.main_header)

    def skip_notifications(self):
        btn = self.find_clickable_element(self.notification)
        btn.click()

