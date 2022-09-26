# MedVendorSpecialitybbdbc7cbf9ec4b499e6a1fb28cbfaa46
from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class PatientScreen(App):
    """
    Allow notification screen
    """

    patient_all_row = (MobileBy.XPATH, '//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell['
                                       '1]/XCUIElementTypeStaticText')
    patient_from_list = (MobileBy.XPATH, "/XCUIElementTypeApplication/XCUIElementTypeWindow["
                                         "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther["
                                         "2]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell")
    # patient_from_list = (MobileBy.XPATH, '//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell['
    #                                      '1]/XCUIElementTypeStaticText[2]')
    second_patient_from_list = (MobileBy.XPATH, '//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell['
                                                '2]/XCUIElementTypeStaticText[2]')
    third_patient_from_list = (MobileBy.XPATH, '//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell['
                                               '3]/XCUIElementTypeStaticText[2]')
    add_new_family_member = (MobileBy.ACCESSIBILITY_ID, "Добавить пациента")
    new_patient = (MobileBy.XPATH, '//XCUIElementTypeCell[1]//XCUIElementTypeTextField[1]')
    choose_patient_type = (MobileBy.ACCESSIBILITY_ID, "Я новый клиент")
    surname = (MobileBy.XPATH, '//XCUIElementTypeCell[2]//XCUIElementTypeTextField[1]')
    name = (MobileBy.XPATH, '//XCUIElementTypeCell[3]//XCUIElementTypeTextField[1]')
    second_name = (MobileBy.XPATH, '//XCUIElementTypeCell[4]//XCUIElementTypeTextField[1]')
    sex = (MobileBy.XPATH, '//XCUIElementTypeCell[6]//XCUIElementTypeTextField[1]')
    choose_sex = (MobileBy.XPATH, "//XCUIElementTypePickerWheel")
    date = (MobileBy.XPATH, '//XCUIElementTypeCell[7]//XCUIElementTypeTextField[1]')
    choose_date = (MobileBy.XPATH, "//XCUIElementTypePickerWheel[1]")
    # choose_month = (MobileBy.XPATH,
    # '//XCUIElementTypeDatePicker//XCUIElementTypePicker//XCUIElementTypePickerWheel[@value = "января"]')
    # choose_year = (MobileBy.XPATH, '//XCUIElementTypeDatePicker//XCUIElementTypePicker//XCUIElementTypePickerWheel[
    # @value = "1999"]')
    ready = (MobileBy.XPATH, '//XCUIElementTypeWindow[1]//XCUIElementTypeButton')
    done = (MobileBy.ACCESSIBILITY_ID, "Готово")

    def choose_first_patient(self):
        self.click_to_element(self.patient_from_list)
