import time

import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from conftest import get_logger


def keyword_check(kwargs):
    kc = {}
    if 'index' in kwargs: kc['index'] = 'elements'
    if 'index' not in kwargs: kc['index'] = 'element'
    return ''.join(kc.values())

TIMEOUT_SEC = 20

NUMERIC_KEYBOARD = {"0": 7, "1": 8, "2": 9, "3": 10, "4": 11, "5": 12, "6": 13, "7": 14, "8": 15, "9": 16}


class App:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """
        Method for find element with WebDriverWait inside
        """
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element

        except NoSuchElementException as e:
            print(e)

    def click_to_element(self, locator):
        """
        locate an element by polling if element not found
        maximum poll #2 with approx. ~10 secs
        """
        try:
            element = self.find_element(locator)
            element.click()

        except ElementClickInterceptedException as e:
            print(e)

    def set_field(self, locator, value):
        """
        Method for fill value into field
        """
        try:
            element = self.find_element(locator)
            element.send_keys(value)

        except NoSuchElementException as e:
            print(e)

#
#     def elements(self, locator, n=3, driver=None, xpath=""):
#         """
#         locate element list by polling if the element list is not found
#         maximum poll #2 with approx. ~10 secs
#         """
#         wait = WebDriverWait(self.driver, TIMEOUT_SEC) if not driver else WebDriverWait(driver, TIMEOUT_SEC)
#
#         x = iter(CustomCall())
#         while n > 1:
#             try:
#                 wait.until(EC.presence_of_element_located(locator))
#                 if driver:
#                     return driver.find_elements(*locator)
#                 else:
#                     return self.driver.find_elements(*locator)
#             except Exception as e:
#                 self.logger.error(f"element list failed attempt {next(x)} - {locator}")
#                 n -= 1
#                 if n == 1: raise NoSuchElementException("Could not locate element list with value: %s" % str(locator))
#
#     def is_displayed(self, locator, expected=True, n=3, driver=None, xpath=None, **kwargs):
#         """
#         assert boolean value by polling if match is not found
#         maximum poll #3 with approx. ~10 secs
#         """
#         wait = WebDriverWait(self.driver, TIMEOUT_SEC) if not driver else WebDriverWait(driver, TIMEOUT_SEC)
#
#         x = iter(CustomCall())
#         while n > 1:
#             try:
#                 if len(kwargs) == 0:
#                     if driver and xpath:
#                         wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#                         assert driver.find_element(by=By.XPATH, value=xpath).is_displayed() == expected
#                     else:
#                         wait.until(EC.visibility_of_element_located(locator))
#                         assert self.driver.find_element(*locator).is_displayed() == expected
#                 else:
#                     if driver:
#                         wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#                         assert driver.find_elements(by=By.XPATH, value=xpath).is_displayed() == expected
#                     else:
#                         wait.until(EC.visibility_of_element_located(locator))
#                         assert self.driver.find_elements(*locator)[kwargs['index']].is_displayed() == expected
#                 break
#             except Exception as e:
#                 self.logger.error(f'is_displayed failed attempt {next(x)} - {locator}')
#                 time.sleep(0.5)
#                 n -= 1
#                 if n == 1: assert False == expected
#
#     def is_exist(self, locator, expected=True, n=3, **kwargs):
#         """
#         returns boolean value by polling if match is not found or not
#         maximum poll #3 with approx. ~10 secs
#         """
#         while n > 1:
#             try:
#                 if len(kwargs) == 0 and self.driver.find_element(*locator).is_displayed() == expected:
#                     return True
#                 elif self.driver.find_elements(*locator)[kwargs['index']].is_displayed() == expected:
#                     return True
#             except Exception as e:
#                 n -= 1
#                 if n == 1: return False
#
#     def tap(self, locator, **kwargs):
#         """
#         custom wrapped single tap method
#         -> wait until display
#         -> element(s)
#         """
#         App.is_displayed(self, locator, True)
#
#         actions = TouchAction(self.driver)
#         return {
#             'element': lambda x: actions.tap(App.element(self, locator)).perform(),
#             'elements': lambda x: actions.tap(App.elements(self, locator)[kwargs['index']]).perform()
#         }[keyword_check(kwargs)]('x')
#
#     def double_tap(self, locator, n=3, **kwargs):
#         """
#         custom wrapped double tap method
#         -> wait for element until display
#         -> element(s)
#         """
#         App.is_displayed(self, locator, True, n=n)
#
#         actions = TouchAction(self.driver)
#         return {
#             'element': lambda x: actions.tap(App.element(self, locator), count=2).perform(),
#             'elements': lambda x: actions.tap(App.elements(self, locator)[kwargs['index']], count=2).perform()
#         }[keyword_check(kwargs)]('x')
#
#     def click_when_clickable(self, locator, n=3, driver=None, xpath="", **kwargs):
#         """
#         custom wrapped click method
#         -> wait for element until display
#         -> element(s)
#         """
#         if xpath:
#             locator = (By.XPATH, xpath)
#
#         App.sleep(kwargs)
#         App.wait_until_clickable(self, locator, n=n, driver=driver, xpath=xpath)
#
#         if driver and xpath:
#             return {
#                 'element': lambda x: App.element(self, locator=None, driver=driver, xpath=xpath).click(),
#                 'elements': lambda x: App.elements(self, locator=None, driver=driver, xpath=xpath)[kwargs['index']].click()
#             }[keyword_check(kwargs)]('x')
#         else:
#             return {
#                 'element': lambda x: App.element(self, locator).click(),
#                 'elements': lambda x: App.elements(self, locator)[kwargs['index']].click()
#             }[keyword_check(kwargs)]('x')
#
#     def click(self, locator, n=3, driver=None, xpath="", **kwargs):
#         """
#         custom wrapped click method
#         -> wait for element until display
#         -> element(s)
#         """
#         if xpath:
#             locator = (By.XPATH, xpath)
#
#         App.sleep(kwargs)
#         App.is_displayed(self, locator, True, n=n, driver=driver, xpath=xpath)
#
#         if driver and xpath:
#             time.sleep(2)
#             return {
#                 'element': lambda x: App.element(self, locator=None, driver=driver, xpath=xpath).click(),
#                 'elements': lambda x: App.elements(self, locator=None, driver=driver, xpath=xpath)[kwargs['index']].click()
#             }[keyword_check(kwargs)]('x')
#         else:
#             time.sleep(2)
#             return {
#                 'element': lambda x: App.element(self, locator).click(),
#                 'elements': lambda x: App.elements(self, locator)[kwargs['index']].click()
#             }[keyword_check(kwargs)]('x')
#
#     def wait_until_not_visible(self, locator, n=3, **kwargs):
#         wait = WebDriverWait(self.driver, TIMEOUT_SEC)
#         wait.until(EC.invisibility_of_element_located(locator))
#
#     def wait_until_exists(self, locator, n=3, **kwargs):
#         wait = WebDriverWait(self.driver, TIMEOUT_SEC)
#         wait.until(EC.presence_of_element_located(locator))
#
#     def wait_until_text_exists(self, locator, text):
#         wait = WebDriverWait(self.driver, TIMEOUT_SEC)
#         for i in range(TIMEOUT_SEC):
#             wait.until(EC.presence_of_element_located(locator))
#             if App.element(self, locator).text == text:
#                 return True
#             time.sleep(1)
#         return False
#
#     def wait_until_clickable(self, locator, n=3, **kwargs):
#         wait = WebDriverWait(self.driver, TIMEOUT_SEC)
#         wait.until(EC.element_to_be_clickable(locator))
#
#     def wait_until_visible(self, locator, n=3, **kwargs):
#         wait = WebDriverWait(self.driver, TIMEOUT_SEC)
#         wait.until(EC.visibility_of_element_located(locator))
#
#     def wait_until_clickable_xpath(self, locator):
#         wait = WebDriverWait(self.driver, TIMEOUT_SEC)
#         wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
#
#     @staticmethod
#     def sleep(kwargs):
#         try:
#             time.sleep(kwargs['sleep'])
#         except KeyError:
#             pass
#
#     def send_keys(self, locator, text='', driver=None, xpath=None, **kwargs):
#         """
#         custom wrapped send_keys method
#         -> wait for element until display
#         -> element(s)
#         """
#         App.is_displayed(self, locator, True, n=3, driver=driver, xpath=xpath)
#
#         if driver and xpath:
#             App.element(self, locator=None, driver=driver, xpath=xpath).clear()
#             App.element(self, locator=None, driver=driver, xpath=xpath).send_keys(text)
#         else:
#             return {
#                 'element': lambda text: App.element(self, locator=locator, driver=driver).clear() and
#                                         App.element(self, locator=locator, driver=driver).send_keys(text),
#                 'elements': lambda text: App.elements(self, locator=locator, driver=driver)[kwargs['index']].clear() and
#                                          App.elements(self, locator=locator, driver=driver)[kwargs['index']].send_keys(text)
#             }[keyword_check(kwargs)](text)
#
#     def get_screen_size(self):
#         return self.driver.get_window_size()
#
#     def back(self):
#         """
#         generally minimize app
#         """
#         self.driver.back()
#
#     def close(self):
#         self.driver.close_app()
#
#     def reset(self):
#         self.driver.reset()
#
#     def launch_app(self):
#         self.driver.launch_app()
#
#     def swipe(self, start, dest):
#         """
#         custom wrapped swipe / scroll method
#         -> wait for element until display - source and destination
#         -> element(s)
#         """
#         if type(start[1]) is not int:
#             source_element = App.element(self, start)
#         else:
#             source_element = App.elements(self, start[0])[int(start[1])]
#
#         if type(dest[1]) is not int:
#             target_element = App.element(self, dest)
#         else:
#             target_element = App.elements(self, dest[0])[int(dest[1])]
#
#         self.driver.scroll(source_element, target_element)
#
#     def tap_by_coordinates(self, x, y):
#         time.sleep(2)
#         actions = TouchAction(self.driver)
#         actions.tap(x=x, y=y).perform()
#
#     # need refactor on condition
#     def assert_text(self, locator, text, n=20, **kwargs):
#         """
#         assert element's text by polling if match is not found
#         maximum poll #20 with approx. ~10 secs
#         """
#         App.is_displayed(self, locator, True)
#
#         x = iter(CustomCall())
#         while n > 1:
#             try:
#                 if len(kwargs) == 0:
#                     assert App.element(self, locator).text == text
#                 else:
#                     assert App.elements(self, locator)[kwargs['index']].text == text
#                 break
#             except Exception as e:
#                 self.logger.error(f'assert_text failed attempt {next(x)}- {locator}')
#                 time.sleep(0.5)
#                 n -= 1
#                 if len(kwargs) == 0:
#                     if n == 1: assert App.element(self, locator).text == text
#                 else:
#                     if n == 1: assert App.elements(self, locator)[kwargs['index']].text == text
#
#     def assert_size(self, locator, param):
#         """
#         assert elements size by polling if match is found
#         maximum poll #20 with approx. ~10 secs
#         """
#         App.is_displayed(self, locator, True, index=0)
#
#         case = param.rsplit(None, 1)[0]
#         value = int(param.rsplit(None, 1)[1])
#
#         if case in ['more than', 'greater than', 'above', '>']:
#             assert App.elements(self, locator).__len__() > value
#         elif case in ['less than', 'below', '<']:
#             assert App.elements(self, locator).__len__() < value
#         elif case in ['equal to', '==']:
#             assert App.elements(self, locator).__len__() == value
#
#     def swipe_until(self, locator, start_x=375, start_y=300, end_x=40, end_y=300, duration=5000, count=2):
#         self.driver.implicitly_wait(0.5)  # waits half a second
#         for i in range(count):
#             try:
#                 self.driver.find_element(*locator).is_displayed()
#                 break
#             except Exception as e:
#                 self.driver.swipe(start_x, start_y, end_x, end_y, duration)
#
#         self.driver.implicitly_wait(5)  # waits 5 seconds
#
#     def assert_equal(self, actual, expected, n=5):
#         x = iter(CustomCall())
#         while n > 1:
#             try:
#                 assert actual == expected
#                 break
#             except Exception as e:
#                 self.logger.error(f"assert equal attempt {next(x)} - {actual} not matching {expected}")
#                 time.sleep(2)
#                 n -= 1
#                 if n == 1: assert actual == expected
#
#     def assert_equal_ab(self, actual, expected_a, expected_b, n=5):
#         x = iter(CustomCall())
#         while n > 1:
#             try:
#                 try:
#                     assert actual == expected_a
#                 except Exception as e:
#                     assert actual == expected_b
#                 break
#             except Exception as e:
#                 self.logger.error(f"assert equal attempt {next(x)} - {actual} not matching {expected_a} or {expected_b}")
#                 time.sleep(2)
#                 n -= 1
#                 if n == 1: assert actual == expected_a
#
#     @staticmethod
#     def assert_boolean(actual, expected=True):
#         assert actual == expected
#
#     def get_activation_code(self, phone):
#         # from selenium import webdriver as web_driver
#         # chrome_driver = web_driver.Chrome()
#         options = webdriver.ChromeOptions()
#         options.add_argument('--no-sandbox')
#         options.add_argument('--remote-debugging-port=9222')
#         options.add_argument('--disable-dev-shm-usage')
#         # options.add_argument('--user-data-dir=/qa')
#         options.add_argument('--headless')
#         options.add_argument('--disable-gpu')
#         options.add_argument('--profile-directory=Default')
#         # options.add_argument('--user-data-dir=' + os.environ['PWD'] + '/ChromeProfile')
#         # options.add_argument('--user-data-dir=' + (os.path.abspath(os.path.join(os.path.dirname(os.getenv("TMP")), '..', 'Google/Chrome/User Data/Default'))))
#         chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#
#         chrome_driver.get('https://predprod-dev.smartmed.pro/admin/')
#         App.click(self, locator=None, xpath="//input[@name='login-admin']", driver=chrome_driver)
#         App.send_keys(self, locator=None, xpath="//input[@name='login-admin']", text="StreamTest", driver=chrome_driver)
#         App.send_keys(self, locator=None, xpath="//input[@name='password-admin']", text="streamtest1", driver=chrome_driver)
#         App.click(self, locator=None, xpath="//input[@value='Ok']", driver=chrome_driver)
#         App.click(self, locator=None, xpath="//span[text()='СМС']", driver=chrome_driver)
#         App.send_keys(self, locator=None, xpath="//input[@id='nameInput']", text=phone, driver=chrome_driver)
#         App.click(self, locator=None, xpath="//input[@value='Получить код']", driver=chrome_driver)
#         chrome_driver.save_screenshot('C:/Users/k.pavlovskaya/PycharmProjects/medsi2/qa-automation-mobile/1.png')
#         activation_code = App.element(self, locator=None, xpath="//p[contains(text(),'Код активации:')]", driver=chrome_driver).text
#         chrome_driver.quit()
#         return activation_code
#
#     def send_key_events(self, input):
#         for char in input:
#             self.driver.keyevent(NUMERIC_KEYBOARD[char])
#
#     def get_driver(self):
#         dr = self.driver
#         return dr
#
#     def swipe_percent(self, startx_percent: float, starty_percent: float, endx_percent: float, endy_percent: float):
#         """
#         :param startx_percent: percentage of screen width
#         :param starty_percent: percentage of screen height
#         :param endx_percent: percentage of screen width
#         :param endy_percent: percentage of screen height
#         :return:
#         """
#         deviceSize = App.get_screen_size(self)
#         screenWidth = deviceSize['width']
#         screenHeight = deviceSize['height']
#
#         startx = int(screenWidth * startx_percent)
#         starty = int(screenHeight * starty_percent)
#
#         endx = int(screenWidth * endx_percent)
#         endy = int(screenHeight * endy_percent)
#
#         actions = TouchAction(self.driver)
#         actions.press(None, startx, starty).wait(100).move_to(None, endx, endy).release().perform()
#
#     def swipe_left_to_right(self):
#         """
#         custom wrapped swipe
#         """
#         deviceSize = App.get_screen_size(self)
#         screenWidth = deviceSize['width']
#         screenHeight = deviceSize['height']
#         startx = int(screenWidth * 8 / 9)
#         endx = int(screenWidth / 9)
#         starty = int(screenHeight / 2)
#         endy = int(screenHeight / 2)
#         actions = TouchAction(self.driver)
#         actions.press(None, startx, starty).wait(100).move_to(None, endx, endy).release().perform()
#
#     def swipe_right_to_left(self, startx=None, endx=None, starty=None, endy=None):
#         """
#         custom wrapped swipe
#         """
#         deviceSize = App.get_screen_size(self)
#         screenWidth = deviceSize['width']
#         screenHeight = deviceSize['height']
#         # *********** Left to Right *************
#         startx = int(screenWidth / 9) if startx is None else startx
#         endx = int(screenWidth * 8 / 9) if endx is None else endx
#         starty = int(screenHeight / 2) if starty is None else starty
#         endy = int(screenHeight / 2) if endy is None else endy
#         # *********** Right to Left *************
#         #startx2 = screenWidth / 9
#         #endx2 = screenWidth * 8 / 9
#         #starty2 = screenHeight / 2
#         #endy2 = screenHeight / 2
#         actions = TouchAction(self.driver)
#         actions.press(None, startx, starty).wait(100).move_to(None, endx, endy).release().perform()
#
#     def swipe_top_to_bottom(self):
#         """
#         custom wrapped swipe
#         """
#         deviceSize = App.get_screen_size(self)
#         screenWidth = deviceSize['width']
#         screenHeight = deviceSize['height']
#         # 470, 1400, 470, 1000, 400
#         # print(screenWidth)
#         # print(screenHeight)
#         startx = int(screenWidth / 2)
#         endx = int(screenWidth / 2)
#         starty = int(screenHeight * 5 / 9)
#         print(starty)
#         endy = int(screenHeight / 9)
#         self.driver.swipe(startx, starty, endx, endy, 1100)
#
#     def swipe_bottom_to_top(self):
#         """
#         custom wrapped swipe
#         """
#         deviceSize = App.get_screen_size(self)
#         screenWidth = deviceSize['width']
#         screenHeight = deviceSize['height']
#         # 470, 1400, 470, 1000, 400
#         # print(screenWidth)
#         # print(screenHeight)
#         startx = int(screenWidth / 2)
#         endx = int(screenWidth / 2)
#         starty = int(screenHeight / 7)
#         endy = int(screenHeight * 5 / 9)
#         print(startx, starty, endx, endy)
#         self.driver.swipe(startx, starty, endx, endy, 1100)
#
# class CustomCall:
#
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         k = self.a
#         self.a += 1
#         return k