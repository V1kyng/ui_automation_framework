import os
import unittest
from datetime import datetime
from time import sleep

import pytest

from conftest import get_logger
from src.helpers.business import *
from src.screens.android.home import HomeScreen as Androidmain
# ANDROID_APK_PATH = f'{os.popen("pwd").read().rstrip()}/data/apps/preprod.apk'
from src.screens.android.login import LoginScreen as AndroidLogin
from src.screens.ios.home import HomeScreen as IOSmain
from src.screens.ios.login_screen import LoginScreen as IOSLogin


class Driver(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    @pytest.fixture(autouse=True)
    def init_login(self, request, app, device, driver_setup):
        self.app = app
        self.device = device
        self.logger = get_logger()
        self.driver = driver_setup
        self.request = request
        if not self.is_auth_test(request):
            if self.app == ANDROID_PLATFORM_NAME:
                self.logger.info("Setup via standard login")
                AndroidLogin.session_login(self)
            elif self.app == IOS_PLATFORM_NAME:
                IOSLogin.session_login(self)
        yield
        self.screenshot_on_failure(True)
        if self.app == ANDROID_PLATFORM_NAME:
            self.driver.terminate_app("ru.medsi.smartmed.dev")
            self.driver.launch_app()
        elif self.app == IOS_PLATFORM_NAME:
            if self.is_auth_test(request):
                self.driver.terminate_app("ru.medsi.smartmed.dev")
                self.driver.launch_app()
            else:
                self.driver.terminate_app("ru.medsi.smartmed.dev")
                self.driver.launch_app()
                # IOSmain.get_app_main_page(self)

                # self.driver.remove_app('ru.medsi.smartmed.dev')
                # self.driver.install_app('bs://32b54949f9fde699bcff518fdb29d6473ac78539')
                # self.driver.start_activity('com.browserstack.sample', 'com.browserstack.sample.MainActivity')


    @staticmethod
    def is_auth_test(request):
        for marker in request.node.own_markers:
            if marker.name == 'login':
                return True
        return False

    @pytest.fixture(autouse=True, scope="function")
    def setup_tear_down(self, request):
        yield
        self.logger.info("Teardown")
        self.screenshot_on_failure(Driver.is_test_failed(request))

    def screenshot_on_failure(self, test_failed):
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        if test_failed:
            self.logger.error("Taking screenshot on failure")
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
            self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")
            # attach(data=self.driver.get_screenshot_as_base64())


    def return_device_type(self):
        used_app = self.app
        return used_app

    @staticmethod
    def is_test_failed(request):
        """
        :param request:
        :return: boolean
        """
        return True if request.node.report.outcome == 'failed' else False

if __name__ == '__main__':
    unittest.main()
