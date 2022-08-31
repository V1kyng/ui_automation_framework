from appium.webdriver.common.mobileby import MobileBy
from src.helpers.app import App



class SpecialistScreen(App):
    """
    Specialist screen locators
    """

    dont_know_exactly = (
    MobileBy.XPATH, '//android.widget.LinearLayout[1]/android.widget.TextView[@text="Точно не знаю"]')
    search_bar = (MobileBy.ID, "ru.mts.smartmed.dev:id/searchBarEditText")
    search_edit = (MobileBy.ID, "ru.mts.smartmed.dev:id/searchEditText")
    search_by_fio = (MobileBy.ID, "ru.mts.smartmed.dev:id/item_search_by_fio_edit_text")
    all_specialist_screen = (MobileBy.ID, "ru.mts.smartmed.dev:id/recyclerSpecializations")
    doctor_name = (MobileBy.ID, "ru.mts.smartmed.dev:id/doctorNameTextView")
    # doctor_name = (MobileBy.XPATH, '//android.view.ViewGroup[1]/android.widget.TextView[1]')
    view_group2 = (MobileBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    view_group4 = (MobileBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]')
    view_group5 = (MobileBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]')
    view_group6 = (MobileBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]')
