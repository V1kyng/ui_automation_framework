import os

import pytest
from appium import webdriver as appium_driver

from logger import get_logger
from ui_framework.capabilities import Capabilities

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


def init_driver_session(app, device):
    logger.info("Driver session setup")
    logger.info("Configuring desired capabilities")
    capabilities = Capabilities()
    desired_caps = {}
    driver = None

    logger.info("Initiating Appium driver")
    if os.getenv('PYTEST_XDIST_WORKER'):
        capabilities.get_xdist_capabilities(app, device)

    elif app == 'ios':
        logger.debug("Prepare IOS capabilities")
        desired_caps = capabilities.get_ios_capabilities(device)

    elif app == 'android':
        logger.debug("Prepare Android capabilities")
        desired_caps = capabilities.get_android_capabilities(device)

    if device == "bs":
        logger.debug("Connecting to browserstack")
        print("Connecting to browserstack")

        driver = appium_driver.Remote(
            command_executor="http://hub-cloud.browserstack.com/wd/hub",
            desired_capabilities=desired_caps)
        logger.debug("Connection success")
        print("Connection success")

    elif device != "bs":
        driver = appium_driver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    logger.info("Initiated successfully")

    driver.implicitly_wait(5)
    print("Driver setup success")
    return driver


@pytest.fixture(scope='session', autouse=True)
def driver_setup(request, app, device):
    driver = init_driver_session(app, device)
    yield driver
    print("Driver quit")
    status_str = "failed" if request.node.testsfailed else "passed"
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": '
        '{"status":"' + status_str + '", "reason":"Reason"}}'
    )
    logger.info("driver quit")
    driver.quit()


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
