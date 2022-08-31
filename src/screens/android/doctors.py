from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class DoctorsScreen(App):
    """
    Doctors screen locators
    """

    def __init__(self):
        super().__init__()

    cliniks = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="Клиники"]')
    popup_order_consultation = (MobileBy.ID, "ru.mts.smartmed.dev:id/warning_dialog_close")
    center_on_belarusskaya = (MobileBy.XPATH,
                              '//android.widget.LinearLayout/android.widget.TextView[@text="Клинико-диагностический центр на Белорусской"]')
    sign_up_for_an_appointment_with = (MobileBy.ID, "ru.mts.smartmed.dev:id/item_clinic_info_image")
    doctor_fio = (MobileBy.ID, "ru.mts.smartmed.dev:id/item_doctor_select_list_fio_textview")
    doctor_not_found = (MobileBy.ID, "ru.mts.smartmed.dev:id/doctors_list_doctors_not_found")
    all_doctors = (MobileBy.XPATH, '//android.widget.LinearLayout[1]/android.widget.TextView[@text="Все врачи"]')
    first_doctor_in_list = (MobileBy.XPATH, '//android.widget.LinearLayout[2]/android.widget.TextView[@text="CLINIC-WithTwoDoctors(AT)-tests"]')
