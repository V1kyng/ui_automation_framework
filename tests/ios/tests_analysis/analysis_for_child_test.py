import pytest

from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.screens.ios.home import HomeScreen
from src.screens.ios.patient import PatientScreen
from src.screens.ios.analysis_screen import AnalysisScreen
from src.screens.ios.bank_card_screen import BankCardScreen

SEARCH_REQUEST = 'гем'
CLINIC_SEARCH_REQUEST = 'мит'
SEARCH_REQUEST_NEGATIVE = 'yyyyyyyy'


class TestAnalysisScreen(Driver):
    @pytest.mark.skip(reason="bug")
    @pytest.mark.laboratory
    def test_button_pay_not_available_without_checkbox(self):
        App.swipe_top_to_bottom(self)
        App.click(self, HomeScreen.analysis_button)
        App.click(self, PatientScreen.third_patient_from_list)
        if App.is_exist(self, AnalysisScreen.all_clear):
            App.click(self, AnalysisScreen.all_clear)
        App.click(self, AnalysisScreen.search_field)
        App.send_keys(self, AnalysisScreen.search_field, SEARCH_REQUEST)
        App.click(self, AnalysisScreen.add_first_item)
        App.click(self, AnalysisScreen.cancel_button)
        App.click(self, AnalysisScreen.basket_button)
        App.click(self, AnalysisScreen.choose_clinic)
        App.click(self, AnalysisScreen.to_list_option)
        App.click(self, AnalysisScreen.clinic_search_field)
        App.send_keys(self, AnalysisScreen.clinic_search_field, CLINIC_SEARCH_REQUEST)
        App.click(self, AnalysisScreen.clinic_search_result)
        App.click(self, AnalysisScreen.choose_clinic)
        App.click(self, AnalysisScreen.date)
        App.click(self, AnalysisScreen.choose_date_button)
        # App.click(self, MedTestsScreen.information_checkbox)  #  TODO when bug fixed
        App.click(self, BankCardScreen.pay_button)
        App.wait_until_exists(self, HomeScreen.main_header)
        App.is_displayed(self, HomeScreen.medical_tests_button)
