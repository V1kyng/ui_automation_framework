import time

from appium.webdriver.common.touch_action import TouchAction

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.utils import is_out_of_timer


class App:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """
        Method for find element with WebDriverWait inside
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return element

        except TimeoutException as ex:
            raise ex

    def find_text(self, locator, timeout=20):
        """
        Method for find element with WebDriverWait on
         wait text present
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element

        except TimeoutException as ex:
            raise ex

    def find_visible_elem(self, locator, timeout=10):
        """
        Method for find element with WebDriverWait on
         wait text present
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element

        except TimeoutException as ex:
            print("Element not found", ex)

    def until_element_invisible(self, locator):
        """
        Method for find element with WebDriverWait on
        wait invisible of element
        """
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element(locator)
            )
            return element

        except TimeoutException as ex:
            print(ex)

    def find_clickable_element(self, locator):
        """
        Method for click to button with
        according condition
        """
        try:
            element = WebDriverWait(driver=self.driver, timeout=5).until(
                EC.element_to_be_clickable(locator)
            )
            return element

        except TimeoutException as ex:
            raise ex

    def tap_by_coordinates(self, x, y):
        time.sleep(2)
        actions = TouchAction(self.driver)
        actions.tap(x=x, y=y).perform()

    def click_to_element(self, locator):
        """
        locate an element by polling if element not found
        maximum poll #2 with approx. ~10 secs
        """
        time.sleep(0.5)
        self.find_element(locator).click()

    def set_field(self, locator: tuple, value: str):
        """
        Method for fill value into field
        """
        element = self.find_text(locator)
        element.send_keys(value)

    def swipe_after_load_element(self, start_x=75,
                                 start_y=0, end_x=75,
                                 end_y=100, duration=200, waiting_elem=None):
        if self.find_element(waiting_elem):
            time.sleep(2)
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
