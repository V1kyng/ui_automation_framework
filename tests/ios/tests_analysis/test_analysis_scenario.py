import pytest

from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.screens.ios.home import HomeScreen
from src.screens.ios.patient import PatientScreen
from src.screens.ios.analysis_screen import AnalysisScreen
from src.screens.ios.bank_card_screen import BankCardScreen


class TestAnalysisScenario(Driver):
    @pytest.mark.xfail(reason="TM-694")
    @pytest.mark.laboratory
    def test_analysis_happy_path(self):
        App.swipe_top_to_bottom(self)
        App.click(self, HomeScreen.analysis_button)
        App.click(self, PatientScreen.patient_from_list)
        if App.is_exist(self, AnalysisScreen.all_clear):
            App.click(self, AnalysisScreen.all_clear)
        App.click(self, AnalysisScreen.search_field)
        App.send_keys(self, AnalysisScreen.search_field, AnalysisScreen.SEARCH_REQUEST)
        App.click(self, AnalysisScreen.add_first_item)
        App.swipe_top_to_bottom(self)
        App.click(self, AnalysisScreen.add_second_item)
        App.click(self, AnalysisScreen.cancel_button)
        App.click(self, AnalysisScreen.basket_button)
        App.is_displayed(self, AnalysisScreen().basket_check_item(2))
        App.is_displayed(self, AnalysisScreen.trash)
        App.is_displayed(self, AnalysisScreen.first_item)
        App.is_displayed(self, AnalysisScreen.second_item)
        App.is_displayed(self, AnalysisScreen.choose_clinic)
        App.swipe_right_to_left(self, startx=300, starty=97, endx=0, endy=97)
        App.is_displayed(self, AnalysisScreen.delete_by_swipe)
        App.click(self, AnalysisScreen.delete_by_swipe)
        App.is_displayed(self, AnalysisScreen().basket_check_item(1))
        App.is_displayed(self, AnalysisScreen.choose_clinic)
        App.click(self, AnalysisScreen.trash)
        App.click(self, AnalysisScreen.trash_cancel_delete)
        App.is_displayed(self, AnalysisScreen().basket_check_item(1))
        App.click(self, AnalysisScreen.choose_clinic)
        App.click(self, AnalysisScreen.to_list_option)
        App.click(self, AnalysisScreen.clinic_search_field)
        App.send_keys(self, AnalysisScreen.clinic_search_field, AnalysisScreen.CLINIC_SEARCH_REQUEST)
        App.click(self, AnalysisScreen.clinic_search_result)
        App.click(self, AnalysisScreen.choose_clinic)
        App.click(self, AnalysisScreen.date)
        App.click(self, AnalysisScreen.choose_date_button)
        App.click(self, BankCardScreen.information)
        App.click(self, BankCardScreen.go_back_button)
        App.click(self, BankCardScreen.pay_button)

        # test fail of invoice has been not generated
        # TODO when bug fixed
        App.wait_until_exists(self, HomeScreen.main_header)
        App.is_displayed(self, HomeScreen.analysis_button)
