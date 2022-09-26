import os
import time

import pytest
from appium import webdriver as appium_driver

from capabilities import Capabilities
from logger import get_logger
from src.helpers.android.android_authorization import android_authorization
from src.helpers.ios.ios_authorization import ios_authorization

logger = get_logger()


def android_device_name() -> str:
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
        return 'emulator-5554'
    elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return 'emulator-5556'
    else:
        return 'emulator-5554'


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--app', action='store', default="ios", help="Choose App: ios or android")
    parser.addoption('--device', action='store', default="emulator", help="Choose Device: simulator / emulator / real "
                                                                          "device / bs")


@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


def driver_setup(app: str, device: str):
    logger.info("Driver session setup")
    logger.info("Configuring desired capabilities")
    capabilities = Capabilities()
    logger.info("Initiating Appium driver")

    desired_caps = capabilities.get_capabilities(device=device,
                                                 app=app)
    driver = appium_driver.Remote(
        command_executor=capabilities.CURRENT_EXECUTOR,
        desired_capabilities=desired_caps)

    logger.info("Driver setup success")
    return driver


@pytest.fixture(scope='session', autouse=True)
def driver(request, app, device):
    driver = driver_setup(app=app, device=device)
    yield driver
    print("Driver quit")
    status_str = "failed" if request.node.testsfailed else "passed"
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": '
        '{"status":"' + status_str + '", "reason":"Reason"}}'
    )

    logger.info("driver quit")
    driver.quit()


@pytest.fixture(autouse=True, scope="session")
def authorization(driver, app):
    if app == "ios":
        ios_authorization(driver)
    else:
        android_authorization(driver)


@pytest.fixture(autouse=True, scope="function")
def terminate_app(driver, app):
    yield
    if app == "ios":
        from src.screens.ios.login_screen import LoginScreen
    else:
        from src.screens.android.login import LoginScreen
        time.sleep(2)
    login_screen = LoginScreen(driver)
    driver.terminate_app("ru.medsi.smartmed.dev")
    driver.launch_app()
    login_screen.enter_pin()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    item.report = outcome.get_result()


@pytest.fixture(scope='session')
def mark_bs_tests(request):
    yield
    if request.node.report.failed:
        print(f"Used device IS \n \n bs \n fail!")
    else:
        print(f"Used device IS \n \n bs \n passed!")
