import time

import pytest

from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.model.AppDataModel import Doctor
from src.model.AppDataModel import Specialist
from src.screens.ios.calendar import CalendarScreen
from src.screens.ios.doctors import DoctorsScreen
from src.screens.ios.home import HomeScreen
from src.screens.ios.patient import PatientScreen
from src.screens.ios.specialist import SpecialistScreen


class TestSearchDoctor(Driver):

    # LOGIN_PATIENT = Patient(phone="8888887766", password="00000000")
    DOCTOR_NAME_NEGATIVE = Doctor(name="Гавриш")
    DOCTOR_NAME_POSITIVE = Doctor(name="Иванов")
    # DOCTOR_NAME_POSITIVE = Doctor(name="Глушкова")
    SPECIALIST_NAME_POSITIVE = Specialist(name="Гавриш")
    SPECIALIST_NAME_NEGATIVE = Specialist(name="ххх")
    # FULL_DOCTOR_NAME = ('Гавриш Никита Викторович', 'Иванов Федор', 'Гаврилов Антон Григорьевич', 'Егоршева Наталия (МТС)', 'Бледнова Ольга Сергеевна', 'Емельянова Екатерина Сергеевна')
    FULL_DOCTOR_NAME_1 = Doctor(name="Гавриш Никита Викторович")
    FULL_DOCTOR_NAME_2 = Doctor(name="Иванов Федор")
    # FULL_DOCTOR_NAME_2 = Doct or(name="Глушкова Анна")
    FULL_DOCTOR_NAME_3 = Doctor(name="Гаврилов Антон Григорьевич")
    FULL_DOCTOR_NAME_4 = Doctor(name="Гаджимурадов Абдула Гаджимурадович")
    FULL_DOCTOR_NAME_5 = Doctor(name="Бледнова Ольга Сергеевна")
    FULL_DOCTOR_NAME_6 = Doctor(name="Емельянова Екатерина Сергеевна")


    @pytest.mark.skip(reason="https://medsi.youtrack.cloud/youtrack/issue/SM-893")
    def test_search_doctor_by_name_in_clinic(self):
        App.wait_until_exists(self, HomeScreen.doctors_bottom)
        App.click(self, HomeScreen.doctors_bottom)
        App.click(self, DoctorsScreen.cliniks)
        App.click(self, SpecialistScreen.search_edit)
        App.send_keys(self, SpecialistScreen.search_edit, 'клинико')
        App.click(self, DoctorsScreen.center_on_belarusskaya)
        App.click(self, DoctorsScreen.sign_up_for_an_appointment_with)
        App.click(self, PatientScreen.patient_all_row)
        App.click(self, SpecialistScreen.dont_know_exactly)
        App.wait_until_exists(self, CalendarScreen.calendar_right_arrow)
        App.click(self, CalendarScreen.calendar_right_arrow)
        App.click(self, CalendarScreen.date_is_tuesday)
        App.click(self, SpecialistScreen.search_bar)
        specialist = self.SPECIALIST_NAME_POSITIVE
        App.send_keys(self, SpecialistScreen.search_bar, specialist.name)
        doctor_fn = self.FULL_DOCTOR_NAME_1
        App.wait_until_exists(self, SpecialistScreen.doctor_name_in_clinic)
        if (App.element(self, SpecialistScreen.doctor_name_in_clinic).text) == doctor_fn.name:
            for i in range(len(specialist.name)-4):
                specialist.name = specialist.name[:-1]
                App.send_keys(self, SpecialistScreen.search_bar, specialist.name)
                time.sleep(2)
                assert (App.element(self, SpecialistScreen.doctor_name_in_clinic).text) == doctor_fn.name
        specialist = self.SPECIALIST_NAME_NEGATIVE
        App.send_keys(self, SpecialistScreen.search_bar, specialist.name)
        # assert App.is_exist(self, SpecialistScreen.doctor_name) == False
        assert (App.element(self, SpecialistScreen.doctor_name_in_clinic).text) == "Извините, по вашему запросу ничего не найдено"

    @pytest.mark.skip(reason="https://medsi.youtrack.cloud/youtrack/issue/SM-893")
    def test_search_doctor_for_consultation(self):
        """
        Search_doctor for  consultation issue25
        """
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
        App.click(self, CalendarScreen.date_is_tuesday)
        App.click(self, SpecialistScreen.search_bar)
        doctor = self.DOCTOR_NAME_NEGATIVE
        for i in range(len(doctor.name)-2):
            App.send_keys(self, SpecialistScreen.search_bar, doctor.name)
            time.sleep(2)
            # assert App.is_exist(self, SpecialistScreen.doctor_name, expected=True, n=2) == False
            App.wait_until_exists(self, DoctorsScreen.doctor_fio_empty_in_consultation)
            assert (App.element(self, DoctorsScreen.doctor_fio_empty_in_consultation).text) == "Извините, по вашему запросу ничего не найдено"
            doctor.name = doctor.name[:-1]
        doctor = self.DOCTOR_NAME_POSITIVE
        App.send_keys(self, SpecialistScreen.search_bar, doctor.name)
        App.wait_until_exists(self, SpecialistScreen.doctor_name_in_clinic)
        doctor_fn = self.FULL_DOCTOR_NAME_2
        if (App.element(self, SpecialistScreen.doctor_name_in_clinic).text) == doctor_fn.name:
            for i in range(len(doctor.name)-2):
                doctor.name = doctor.name[:-1]
                App.send_keys(self, SpecialistScreen.search_bar, doctor.name)
                time.sleep(2)
                assert (App.element(self, SpecialistScreen.doctor_name_in_clinic).text) == doctor_fn.name
        else:
            assert "We can not find doctor Иванов Федор" == doctor_fn.name
        # doctor.name = doctor.name[:1]
        # App.send_keys(self, SpecialistScreen.search_bar, doctor.name)
        # App.wait_until_exists(self, SpecialistScreen.first_row_doctor_name)
        # assert (App.element(self, SpecialistScreen.first_row_doctor_name).text) == 'Любой доступный врач'
        # App.click(self, SpecialistScreen.first_row_doctor_name)
        # App.swipe_top_to_bottom(self)

    @pytest.mark.skip(reason="https://medsi.youtrack.cloud/youtrack/issue/SM-893")
    def test_search_doctor_by_name_in_doctors(self):
        App.wait_until_exists(self, HomeScreen.doctors_bottom)
        App.click(self, HomeScreen.doctors_bottom)
        App.click(self, DoctorsScreen.all_doctors)
        App.click(self, SpecialistScreen.search_by_fio)
        specialist = self.SPECIALIST_NAME_POSITIVE
        doctor_fn = self.FULL_DOCTOR_NAME_1
        App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name)
        App.wait_until_exists(self, SpecialistScreen.doctor_name)
        # if (App.element(self, SpecialistScreen.doctor_name).text) == doctor_fn.name:
        #     doctor_fn = self.FULL_DOCTOR_NAME_3
        #     for i in range(len(specialist.name)-4):
        #         specialist.name = specialist.name[:-1]
        #         App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name)
        #         time.sleep(2)
        #         assert (App.element(self, DoctorsScreen.doctor_fio).text) == doctor_fn.name
        # App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name[0])
        # doctor_fn = self.FULL_DOCTOR_NAME_4
        # #Переделать асерт на первый элемент списка
        # assert (App.element(self, DoctorsScreen.doctor_fio_gag).text) == doctor_fn.name
        # App.click(self, SpecialistScreen.search_by_fio)
        # specialist = self.SPECIALIST_NAME_NEGATIVE
        # App.send_keys(self, SpecialistScreen.search_by_fio, specialist.name)
        # time.sleep(2)
        # assert (App.element(self, DoctorsScreen.doctor_fio_empty).text) == "Извините, по вашему запросу ничего не найдено"