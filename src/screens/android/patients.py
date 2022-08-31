from appium.webdriver.common.mobileby import MobileBy

from src.helpers.app import App


class PatientScreen(App):
    """
    Choose family member
    """

    patient_from_list = (MobileBy.ID, "ru.mts.smartmed.dev:id/patient_chooser_name")
    patient_all_row = (MobileBy.ID, "ru.mts.smartmed.dev:id/linearLayout3")
    patient_exactly_name = (MobileBy.ID, "ru.mts.smartmed.dev:id/patient_list_text")
    patient_user_name = (MobileBy.ID, "ru.mts.smartmed.dev:id/allInformationUserName")
    patient_profile_name = (MobileBy.ID, "ru.mts.smartmed.dev:id/user_name_menu") # root_user

