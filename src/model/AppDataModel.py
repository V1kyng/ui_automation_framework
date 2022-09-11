import json
import os

# from src.model.MedsiConstants import BDay, ClientType, Email, Sex

# PHONE_FILE_PATH = f'{os.popen("pwd").read().rstrip()}/data/unused_phone.json'
PHONE_FILE_PATH = os.path.abspath('./src/data/unused_phone.json')


class Patient:

    def __init__(self, phone="", password="", name="", surname="",
                 middle_name="", client_type="", sex="", bday="",
                 email="", address="", bday_words="", android=True, phone_pretty=""):
        self.phone = phone
        self.password = password
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.client_type = client_type
        self.sex = sex
        self.bday = bday
        self.email = email
        self.address = address
        self.sec_code = "0000"
        self.bday_words = bday_words
        self.phone_pretty = phone_pretty
        self.is_androd = android

        if not self.phone:
            with open(PHONE_FILE_PATH) as json_file:
                json_data = json.load(json_file)
                if android:
                    platform_key = "android"
                else:
                    platform_key = "ios"
                self.phone = json_data[platform_key]["regular"]
                json_data[platform_key]["regular"] = str(int(json_data[platform_key]["regular"]) + 1)[0:10]
                self.phone_pretty = json_data[platform_key]["pretty"]
                json_data[platform_key]["pretty"] = "+7 (" + json_data[platform_key]["regular"][0:3] + ") " + \
                                                    json_data[platform_key]["regular"][3:6] + "-" + \
                                                    json_data[platform_key]["regular"][6:8] + "-" + \
                                                    json_data[platform_key]["regular"][8:10]
            with open(PHONE_FILE_PATH, 'w') as outfile:
                json.dump(json_data, outfile)

    def get_clone(self):
        return Patient(phone=self.phone, password=self.password, name=self.name, surname=self.surname,
                       middle_name=self.middle_name, client_type=self.client_type, sex=self.sex, bday=self.bday,
                       email=self.email, address=self.address, bday_words=self.bday_words, android=self.is_androd,
                       phone_pretty=self.phone_pretty)


class Doctor:
    def __init__(self, name=""):
        self.name = name


class Specialist:
    def __init__(self, name=""):
        self.name = name


if __name__ == '__main__':
    NEGATIVE_REG_PATIENT = Patient(password="00000000", name="Vasya", surname="Pupkin",
                                   middle_name="Petrovich", client_type="ClientType.NEW", sex="Sex.MALE",
                                   bday="BDay.INVALID_TOO_YOUNG_FOR_IOS", email="Email.VALID",
                                   address="1311313 131313 131313", android=True)
