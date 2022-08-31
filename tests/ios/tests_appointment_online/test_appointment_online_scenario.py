import pytest

from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.screens.ios.home import HomeScreen
from src.screens.ios.appointment_online_screen import AppointmentOnlineScreen
from src.screens.ios.patient import PatientScreen


class AppointmentOnlineScreenTest(Driver):
    @pytest.mark.online
    def test_appointment_online_happy_path(self):
        self.logger.info("appointment online happy path start")
        App.click(self, HomeScreen.online_consultation)
        App.click(self, PatientScreen.second_patient_from_list)
        App.wait_until_clickable(self, AppointmentOnlineScreen.loading)
        AppointmentOnlineScreen.swipe_top_to_bottom_until_visible(self, AppointmentOnlineScreen.choose_otolaryngologist)
        App.click(self, AppointmentOnlineScreen.choose_otolaryngologist)
        App.wait_until_clickable(self, AppointmentOnlineScreen.choose_nearest_time)
        App.click(self, AppointmentOnlineScreen.choose_nearest_time)
        App.click(self, AppointmentOnlineScreen.all_clear_button)
        App.click(self, AppointmentOnlineScreen.information)
        App.click(self, AppointmentOnlineScreen.go_back_button)
        App.click(self, AppointmentOnlineScreen.pay_button)
        App.click(self, AppointmentOnlineScreen.add_to_calendar)
        App.is_displayed(self, AppointmentOnlineScreen.success)
