import pytest

from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.screens.ios.home import HomeScreen
from src.screens.ios.appointment_online_screen import AppointmentOnlineScreen
from src.screens.ios.patient import PatientScreen
from src.screens.ios.bank_card_screen import BankCardScreen


class AppointmentOnlineScreenTest(Driver):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        App.click(self, HomeScreen.online_consultation)
        App.wait_until_clickable(self, PatientScreen.patient_from_list)
        App.click(self, PatientScreen.patient_from_list)
        App.wait_until_clickable(self, AppointmentOnlineScreen.loading)
        AppointmentOnlineScreen.swipe_top_to_bottom_until_visible(self, AppointmentOnlineScreen.choose_therapist)

    @pytest.mark.online
    def test_appointment_online(self):
        App.click(self, AppointmentOnlineScreen.choose_therapist)
        App.wait_until_clickable(self, AppointmentOnlineScreen.choose_next_time)
        App.click(self, AppointmentOnlineScreen.choose_next_time)
        App.click(self, AppointmentOnlineScreen.all_clear_button)
        App.is_displayed(self, AppointmentOnlineScreen.pay_button)

    @pytest.mark.xfail
    @pytest.mark.online
    def test_button_pay_not_available_without_checkbox(self):
        App.click(self, AppointmentOnlineScreen.choose_therapist)
        App.wait_until_clickable(self, AppointmentOnlineScreen.choose_nearest_time)
        AppointmentOnlineScreen.choose_next_date(self)
        App.wait_until_clickable(self, AppointmentOnlineScreen.choose_nearest_time)
        App.click(self, AppointmentOnlineScreen.choose_nearest_time)
        App.click(self, AppointmentOnlineScreen.all_clear_button)
        App.click(self, AppointmentOnlineScreen.checkbox)
        App.click(self, BankCardScreen.pay_button)
        App.click(self, AppointmentOnlineScreen.add_to_calendar)
        App.is_displayed(self, AppointmentOnlineScreen.success)

    @pytest.mark.skip(reason="later")  # TODO realize
    @pytest.mark.online
    def test_appointment_online_negative_date(self):
        App.click(self, AppointmentOnlineScreen.choose_therapist)
        App.wait_until_clickable(self, AppointmentOnlineScreen.choose_date_negative)

    @pytest.mark.skip(reason="until not adding fixture on DB")
    @pytest.mark.online
    def test_add_new_family_member(self):
        App.wait_until_clickable(self, HomeScreen.online_consultation)
        App.click(self, HomeScreen.online_consultation)
        App.wait_until_clickable(self, PatientScreen.patient_from_list)
        App.click(self, PatientScreen.add_new_family_member)
        App.wait_until_exists(self, PatientScreen.new_patient)
        App.click(self, PatientScreen.new_patient)
        App.click(self, PatientScreen.choose_patient_type)
        App.click(self, PatientScreen.surname)
        App.send_keys(self, PatientScreen.surname, 'Пациентка')
        App.click(self, PatientScreen.name)
        App.send_keys(self, PatientScreen.name, 'Автотест')
        App.click(self, PatientScreen.second_name)
        App.send_keys(self, PatientScreen.second_name, 'Пробная')
        App.click(self, PatientScreen.sex)
        App.send_keys(self, PatientScreen.choose_sex, 'Женский')
        App.click(self, PatientScreen.date)
        App.send_keys(self, PatientScreen.date, '12 февраля 2000')
        App.click(self, PatientScreen.name)
        App.click(self, PatientScreen.done)
        App.click(self, PatientScreen.second_patient_from_list)
