from src.screens.ios.home import HomeScreen
from src.screens.ios.appointment_online_screen import AppointmentOnlineScreen
from src.screens.ios.patient import PatientScreen


class TestAppointmentOnline:

    def test_appointment_online(self, driver):
        home_screen = HomeScreen(driver)
        home_screen.go_to_online_consultation()
        patient_screen = PatientScreen(driver)
        patient_screen.choose_first_patient()
        appointment_online_screen = AppointmentOnlineScreen(driver)
        appointment_online_screen.scroll_to(appointment_online_screen.choose_therapist)
        appointment_online_screen.choose_specialist(appointment_online_screen.choose_therapist)
        appointment_online_screen.choose_next_date()
        appointment_online_screen.choose_time_slot()
        appointment_online_screen.all_clear_button_click()
        appointment_online_screen.check_pay_button()
        appointment_online_screen.check_information()
        appointment_online_screen.check_pay_button()

    def test_another_appointment_online(self, driver):
        home_screen = HomeScreen(driver)
        home_screen.click_to_element(home_screen.online_consultation)
        patient_screen = PatientScreen(driver)
        patient_screen.choose_first_patient()

