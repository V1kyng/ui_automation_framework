import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import TimeoutException


class AdminPage:
    LOGIN_ADMIN = "//input[@name='login-admin']"
    PASSWORD_ADMIN = "//input[@name='password-admin']"
    OK_BTN = "//input[@value='Ok']"
    SMS_BTN = "//span[text()='СМС']"
    INPUT_PHONE_FIELD = "//input[@id='nameInput']"
    GET_CODE_BTN = "//input[@value='Получить код']"
    CODE_RESULT = "//p[contains(text(),'Код активации:')]"

    def get_activation_code(self, phone: str) -> str:
        """
        Method for getting sms code for auth
        """
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager(cache_valid_range=1).install(),
                                   options=options)
        driver.get("https://predprod-dev.smartmed.pro/admin/#/mservice/sms")
        driver.find_element(By.XPATH, self.LOGIN_ADMIN).send_keys("StreamTest")
        driver.find_element(By.XPATH, self.PASSWORD_ADMIN).send_keys("streamtest1")
        driver.find_element(By.XPATH, self.OK_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.SMS_BTN))).click()
        driver.find_element(By.XPATH, self.INPUT_PHONE_FIELD).send_keys(phone)
        driver.find_element(By.XPATH, self.GET_CODE_BTN).click()
        code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.CODE_RESULT))).text[-5:]
        driver.quit()
        return code


def get_activation_code(phone):
    admin_page = AdminPage()
    activation_code = admin_page.get_activation_code(phone)
    return activation_code


def is_out_of_timer(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        if (time.time() - begin) >= 10:
            raise TimeoutException
        return result
    return wrapper
