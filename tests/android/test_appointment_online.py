from src.screens.android.home import HomeScreen
from src.screens.android.appointment_online_screen import AppointmentOnlineScreen
from src.screens.android.patients import PatientScreen


class TestAppointmentOnline:

    def test_appointment_online(self, driver):
        home_screen = HomeScreen(driver)
        home_screen.click_to_appointment_online()
        appointment_online_screen = AppointmentOnlineScreen(driver)
        patient_screen = PatientScreen(driver)
        patient_screen.choose_first_patient()
        appointment_online_screen.swipe_to_element(appointment_online_screen.choose_therapist)
        appointment_online_screen.choose_specialist()

    def test_another_appointment_online(self, driver):
        home_screen = HomeScreen(driver)
        home_screen.click_to_element(home_screen.online_consultation)
