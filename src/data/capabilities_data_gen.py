import os


class BaseCapDataGen:
    """
    BASE Capabilities for browserstack
    """
    bs_caps = {
        "browserstack.user": "mihajlichenkova_qw6BhZ",
        "browserstack.key": "y3yeqw1uQka89E1TNArL",
        "browserstack.networkLogs": "true",
        "app": None,
        "device": None,
        "os_version": None,
        "deviceOrientation": "portrait",
        "project": None,
        "build": None,
        "name": None,
        "noReset": True
    }


class AndroidCapDataGen(BaseCapDataGen):
    """
    Android capabilities for real devices and emulators
    """
    ANDROID_APK_PATH: str = os.path.abspath('./data/apps/preprod.apk')
    ANDROID_UUID: str = "b64f97c5"
    ANDROID_PLATFORM_NAME: str = "android"

    def __init__(self, platform_name="android",
                 platform_version="10.0",
                 device_name="Pixel_3a_API_29",
                 app_package="ru.mts.smartmed.dev",
                 app_activity="droid.telemed.mts.ru.telemed.ui.activities.SplashScreenActivity"):
        self.platform_name = platform_name
        self.platform_version = platform_version
        self.device_name = device_name
        self.app_package = app_package
        self.app_activity = app_activity

    def get_android_caps(self) -> dict:
        """
        :return: capabilities dict
        """
        android_caps_real_device_json = {
            "platformName": self.platform_name,
            "platformVersion": self.platform_version,
            "deviceName": self.device_name,
            "noReset": True,
            "fullReset": False,
            "app": self.ANDROID_APK_PATH,
            "appPackage": self.app_package,
            "appActivity": self.app_activity
        }
        return android_caps_real_device_json


class IosCapDataGen(BaseCapDataGen):
    """
    IOS capabilities for real devices and emulators
    """
    IOS_APP_PATH: str = os.path.abspath("./data/apps/iOS-RealDevice-NativeDemoApp-0.2.1.ipa")
    IOS_PLATFORM_NAME: str = "ios"
    IOS_UDID: str = " "

    def __init__(self, platform_name="ios",
                 platform_version="15.5",
                 device_name="iPhone X",
                 automation_name='XCUITest'
                 ):
        self.platform_name = platform_name
        self.platform_version = platform_version
        self.device_name = device_name
        self.automation_name = automation_name

    def get_ios_caps(self) -> dict:
        """
        :return: capabilities dict
        """
        android_caps_real_device_json = {
            "platformName": self.platform_name,
            "platformVersion": self.platform_version,
            "deviceName": self.device_name,
            "udid": self.IOS_UDID,  # < -- if there will be problems - there was a dict {}
            "useNewWDA": True,
            "app": self.IOS_APP_PATH,
            "automationName": self.automation_name
        }
        return android_caps_real_device_json


class BsCapDataGen(BaseCapDataGen):
    """
    This object will crate data for bs(android),
    bs(ios), bs(android xdist run).
    """

    def __init__(self, app=None,
                 device=None,
                 os_version=None,
                 project=None,
                 build=None,
                 name=None):  # TODO Think about hardcopy and softy copy
        self.app = app
        self.device = device
        self.os_version = os_version
        self.project = project
        self.build = build
        self.name = name

    def get_bs_caps(self) -> dict:
        """
        :return: browserstack capabilities dict
        """
        bs_caps = self.bs_caps
        bs_caps.update({
            "app": self.app,
            "device": self.device,
            "os_version": self.os_version,
            "project": self.project,
            "build": self.build,
            "name": self.name,
        })
        return bs_caps
