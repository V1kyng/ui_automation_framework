import time
import pytest
from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.model.AppDataModel import Doctor
from src.model.AppDataModel import Specialist
from src.screens.android.calendar import CalendarScreen
from src.screens.android.doctors import DoctorsScreen
from src.screens.android.patients import PatientScreen
from src.screens.android.specialist import SpecialistScreen
from src.model.AppDataModel import Patient
from src.screens.android.home import HomeScreen


class TestSearchDoctor(Driver):

    LOGIN_PATIENT = Patient(phone="8888887766", password="00000000")
    DOCTOR_NAME_NEGATIVE = Doctor(name="Гавриш")
    DOCTOR_NAME_POSITIVE = Doctor(name="Иванов")
    SPECIALIST_NAME_POSITIVE = Specialist(name="Гавриш")
    SPECIALIST_NAME_NEGATIVE = Specialist(name="ххх")
    # FULL_DOCTOR_NAME = ('Гавриш Никита Викторович', 'Иванов Федор', 'Гаврилов Антон Григорьевич', 'Егоршева Наталия (МТС)', 'Бледнова Ольга Сергеевна', 'Емельянова Екатерина Сергеевна')
    FULL_DOCTOR_NAME_1 = Doctor(name="Гавриш Никита Викторович")
    FULL_DOCTOR_NAME_2 = Doctor(name="Иванов Федор")
    FULL_DOCTOR_NAME_3 = Doctor(name="Гаврилов Антон Григорьевич")
    FULL_DOCTOR_NAME_4 = Doctor(name="Гаджимурадов Абдула Гаджимурадович")
    FULL_DOCTOR_NAME_5 = Doctor(name="Бледнова Ольга Сергеевна")
    FULL_DOCTOR_NAME_6 = Doctor(name="Емельянова Екатерина Сергеевна")

    @pytest.mark.search
    def test_search_doctor_for_consultation(self):
        """
        Search_doctor for  consultation
        """
        self.logger.info("Search doctor for consultation")
        App.wait_until_exists(self, HomeScreen.online_consultation)
        App.click(self, HomeScreen.online_consultation)
        App.click(self, PatientScreen.patient_from_list)
        if App.is_exist(self, SpecialistScreen.dont_know_exactly) == True:
            App.click(self, SpecialistScreen.dont_know_exactly)
        else:
            App.swipe_top_to_bottom(self)
            time.sleep(2)
            if App.is_exist(self, SpecialistScreen.dont_know_exactly) == True:
                App.click(self, SpecialistScreen.dont_know_exactly)
            else:
                App.swipe_top_to_bottom(self)
                App.click(self, SpecialistScreen.dont_know_exactly)
        App.wait_until_exists(self, CalendarScreen.calendar_right_arrow)
        App.click(self, CalendarScreen.calendar_right_arrow)
        App.click(self, CalendarScreen.date_is_monday)
        App.click(self, SpecialistScreen.search_bar)
        doctor = self.DOCTOR_NAME_NEGATIVE
        for i in range(len(doctor.name) - 2):
            App.send_keys(self, SpecialistScreen.search_bar, doctor.name)
            time.sleep(2)
            App.wait_until_exists(self, SpecialistScreen.doctor_name, expected=True, n=2)
            doctor.name = doctor.name[:-1]
        doctor = self.DOCTOR_NAME_POSITIVE
        App.send_keys(self, SpecialistScreen.search_bar, doctor.name)
        App.wait_until_exists(self, SpecialistScreen.doctor_name)
        if App.element(self, SpecialistScreen.doctor_name).text == self.FULL_DOCTOR_NAME_2.name:
            for i in range(len(doctor.name) - 2):
                doctor.name = doctor.name[:-1]
                App.send_keys(self, SpecialistScreen.search_bar, doctor.name)
                App.wait_until_exists(self, SpecialistScreen.doctor_name)
                App.wait_until_text_exists(self, SpecialistScreen.doctor_name, self.FULL_DOCTOR_NAME_2.name)
        App.click(self, SpecialistScreen.search_bar)
        # Любой доступный врач убран из-за дублирования расписаний из-за видов приема
        # App.send_keys(self, SpecialistScreen.search_bar, "И")
        # App.wait_until_exists(self, SpecialistScreen.doctor_name)
        # assert App.element(self, SpecialistScreen.doctor_name).text == 'Любой доступный врач'
        # App.click(self, SpecialistScreen.doctor_name)
        # App.swipe_top_to_bottom(self)

    def __init__(self, driver):
        super().__init__(driver)

    @pytest.mark.search
    def test_search_doctor_by_name_in_clinic(self):
        # for i in range(4):
        #     App.click(self, CommonScreen.code_zero)
        self.logger.info("Search doctor by name in clinic")
        App.wait_until_exists(self, HomeScreen.doctors_bottom)
        App.click(self, HomeScreen.doctors_bottom)
        App.click(self, DoctorsScreen.cliniks)
        if App.is_exist(self, DoctorsScreen.popup_order_consultation, expected=True, n=2) == True:
            App.click(self, DoctorsScreen.popup_order_consultation)
        App.click(self, SpecialistScreen.search_edit)
        App.send_keys(self, SpecialistScreen.search_edit, 'клинико')
        App.click(self, DoctorsScreen.center_on_belarusskaya)
        App.click(self, DoctorsScreen.sign_up_for_an_appointment_with)
        App.click(self, PatientScreen.patient_from_list)
        App.click(self, SpecialistScreen.dont_know_exactly)
        App.wait_until_exists(self, CalendarScreen.calendar_right_arrow)
        App.click(self, CalendarScreen.calendar_right_arrow)
        App.click(self, CalendarScreen.date_is_monday)
        App.click(self, SpecialistScreen.search_bar)
        specialist = self.SPECIALIST_NAME_POSITIVE
        App.send_keys(self, SpecialistScreen.search_bar, specialist.name)
        if (App.element(self, SpecialistScreen.doctor_name).text) == self.FULL_DOCTOR_NAME_1.name:
            for i in range(len(specialist.name) - 4):
                specialist.name = specialist.name[:-1]
                App.send_keys(self, SpecialistScreen.search_bar, specialist.name)
                time.sleep(2)
                App.wait_until_text_exists(self, SpecialistScreen.doctor_name, self.FULL_DOCTOR_NAME_1.name)
        specialist = self.SPECIALIST_NAME_NEGATIVE
        App.send_keys(self, SpecialistScreen.search_bar, specialist.name)
        assert App.is_exist(self, SpecialistScreen.doctor_name) == False

    @pytest.mark.search
    def test_search_doctor_by_name_in_doctors(self):
        # TestAuth.test_login(self)
        self.logger.info("Search doctor by name in doctors")
        App.wait_until_exists(self, HomeScreen.doctors_bottom)
        App.click(self, HomeScreen.doctors_bottom)
        App.click(self, DoctorsScreen.all_doctors)
        App.click(self, SpecialistScreen.search_by_fio)
        specialist = self.SPECIALIST_NAME_POSITIVE
        App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name)
        time.sleep(1)
        if App.element(self, DoctorsScreen.doctor_fio).text == self.FULL_DOCTOR_NAME_1.name:
            for i in range(len(specialist.name) - 4):
                specialist.name = specialist.name[:-1]
                App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name)
                App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name)
                time.sleep(2)
                App.wait_until_text_exists(self, DoctorsScreen.doctor_fio, self.FULL_DOCTOR_NAME_3.name)
        App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name)
        App.wait_until_text_exists(self, DoctorsScreen.doctor_fio, self.FULL_DOCTOR_NAME_4.name)
        App.click(self, SpecialistScreen.search_by_fio)
        specialist = self.SPECIALIST_NAME_NEGATIVE
        App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name)
        assert App.is_exist(self, DoctorsScreen.doctor_not_found) == True

    @pytest.mark.search
    def test_search_doctor_for_offline_consultation(self):
        # for i in range(4):
        #     App.click(self, CommonScreen.code_zero)
        # time.sleep(6)
        self.logger.info("Search doctor for offline consultation")
        App.wait_until_exists(self, HomeScreen.offline_consultation)
        App.click(self, HomeScreen.offline_consultation)
        App.click(self, PatientScreen.patient_from_list)
        App.click(self, SpecialistScreen.dont_know_exactly)
        App.click(self, SpecialistScreen.search_edit)
        App.send_keys(self, SpecialistScreen.search_edit, 'клинико')
        App.click(self, DoctorsScreen.center_on_belarusskaya)
        App.click(self, DoctorsScreen.sign_up_for_an_appointment_with)
        # time.sleep(3)
        App.wait_until_exists(self, CalendarScreen.calendar_right_arrow)
        App.click(self, CalendarScreen.calendar_right_arrow)
        App.click(self, CalendarScreen.date_is_monday)
        App.click(self, SpecialistScreen.search_bar)
        specialist = self.SPECIALIST_NAME_POSITIVE
        App.send_keys(self, SpecialistScreen.search_bar, specialist.name)
        time.sleep(2)
        App.wait_until_text_exists(self, SpecialistScreen.doctor_name, self.FULL_DOCTOR_NAME_1.name)
        App.send_keys(self, SpecialistScreen.search_bar, specialist.name + 'ь')
        time.sleep(2)
        assert (App.is_exist(self, SpecialistScreen.doctor_name)) == False
        App.send_keys(self, SpecialistScreen.search_bar, "")
        #
        # долго ищет пустую строку. time.sleep(3) или больше
        #
        time.sleep(1)
        App.swipe_top_to_bottom(self)
        App.swipe_top_to_bottom(self)
        assert (App.is_exist(self, SpecialistScreen.view_group5)) == True
        time.sleep(1)
        App.is_displayed(self, SpecialistScreen.view_group5)
        App.swipe_bottom_to_top(self)
        time.sleep(1)
        App.swipe_bottom_to_top(self)
        assert App.is_exist(self, PatientScreen.patient_user_name) == True
        App.click(self, CalendarScreen.calendar_right_arrow)
        App.click(self, SpecialistScreen.search_bar)
        App.send_keys(self, SpecialistScreen.search_bar, "бле")
        time.sleep(2)
        App.wait_until_text_exists(self, SpecialistScreen.doctor_name, self.FULL_DOCTOR_NAME_5.name)
