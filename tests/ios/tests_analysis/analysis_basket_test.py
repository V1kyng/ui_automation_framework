import pytest

from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.screens.ios.home import HomeScreen
from src.screens.ios.patient import PatientScreen
from src.screens.ios.analysis_screen import AnalysisScreen
# from src.screens.ios.bank_card_screen import BankCardScreen


class TestAnalysisScreen(Driver):  # TODO same class name

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        App.swipe_top_to_bottom(self)
        App.click(self, HomeScreen.analysis_button)
        App.click(self, PatientScreen.patient_from_list)
        if App.is_exist(self, AnalysisScreen.all_clear):
            App.click(self, AnalysisScreen.all_clear)
        App.click(self, AnalysisScreen.search_field)

    @pytest.mark.laboratory
    def test_back_from_basket_to_search(self):
        App.send_keys(self, AnalysisScreen.search_field, AnalysisScreen.SEARCH_REQUEST)
        App.wait_until_exists(self, AnalysisScreen.add_first_item)
        App.click(self, AnalysisScreen.add_first_item)
        App.swipe_top_to_bottom(self)
        App.wait_until_exists(self, AnalysisScreen.add_second_item)
        App.click(self, AnalysisScreen.add_second_item)
        App.click(self, AnalysisScreen.cancel_button)
        App.click(self, AnalysisScreen.basket_button)
        App.click(self, AnalysisScreen.close_basket_screen)
        App.click(self, AnalysisScreen.basket_button)
        App.is_displayed(self, AnalysisScreen.basket_check_item_counter(2))
        AnalysisScreen.basket_check_price(self, 2)
        App.is_displayed(self, AnalysisScreen.trash)
        App.is_displayed(self, AnalysisScreen.first_item)
        App.is_displayed(self, AnalysisScreen.second_item)
        App.is_displayed(self, AnalysisScreen.choose_clinic)

    @pytest.mark.laboratory
    def test_delete_from_basket_by_swipe(self):
        App.send_keys(self, AnalysisScreen.search_field, AnalysisScreen.SEARCH_REQUEST)
        App.click(self, AnalysisScreen.add_first_item)
        App.swipe_top_to_bottom(self)
        App.click(self, AnalysisScreen.add_second_item)
        App.swipe_top_to_bottom(self)
        App.click(self, AnalysisScreen.add_third_item)
        App.click(self, AnalysisScreen.cancel_button)
        App.click(self, AnalysisScreen.basket_button)
        App.is_displayed(self, AnalysisScreen.basket_check_item_counter(3))  # check 3 items in basket
        AnalysisScreen.basket_check_price(self, 3)
        App.is_displayed(self, AnalysisScreen.trash)
        App.is_displayed(self, AnalysisScreen.first_item)
        App.is_displayed(self, AnalysisScreen.second_item)
        App.is_displayed(self, AnalysisScreen.choose_clinic)
        App.swipe_right_to_left(self, startx=300, starty=97, endx=0, endy=97)  # delete item from basket by swipe
        App.is_displayed(self, AnalysisScreen.delete_by_swipe)
        App.click(self, AnalysisScreen.delete_by_swipe)
        App.is_displayed(self, AnalysisScreen.basket_check_item_counter(2))  # check 2 items in basket left
        AnalysisScreen.basket_check_price(self, 2)
        App.swipe_right_to_left(self, startx=300, starty=97, endx=0, endy=97)  # another delete item from basket by swipe
        App.is_displayed(self, AnalysisScreen.delete_by_swipe)
        App.click(self, AnalysisScreen.delete_by_swipe)
        App.is_displayed(self, AnalysisScreen.basket_check_item_counter(1))  # check 1 item in basket left
        AnalysisScreen.basket_check_price(self, 1)
        App.is_displayed(self, AnalysisScreen.choose_clinic)

    @pytest.mark.laboratory
    def test_delete_all_items_from_basket(self):
        App.send_keys(self, AnalysisScreen.search_field, AnalysisScreen.SEARCH_REQUEST)
        App.click(self, AnalysisScreen.add_first_item)
        App.swipe_top_to_bottom(self)
        App.click(self, AnalysisScreen.add_second_item)
        App.swipe_top_to_bottom(self)
        App.click(self, AnalysisScreen.add_third_item)
        App.click(self, AnalysisScreen.cancel_button)
        App.click(self, AnalysisScreen.basket_button)
        App.is_displayed(self, AnalysisScreen.basket_check_item_counter(3))  # check 3 items in basket
        AnalysisScreen.basket_check_price(self, 3)
        App.is_displayed(self, AnalysisScreen.trash)
        App.click(self, AnalysisScreen.trash)
        App.click(self, AnalysisScreen.trash_delete)
        App.is_displayed(self, AnalysisScreen.search_field)
