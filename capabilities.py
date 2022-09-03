import os


class Capabilities:
    ANDROID_APK_PATH = os.path.abspath('./data/apps/preprod.apk')
    ANDROID_UUID = "b64f97c5"
    ANDROID_PLATFORM_NAME = "android"
    IOS_PLATFORM_NAME = "ios"
    IOS_UDID = " "

    @staticmethod
    def wda_port():
        if os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
            return 8101
        else:
            return 8100

    def get_android_capabilities(self, device):
        if device == 'real device':
            return dict(platformName="android",
                        platformVersion='10.0',
                        deviceName='Pixel_3a_API_29',
                        noReset=True,
                        fullReset=False,
                        app=self.ANDROID_APK_PATH,
                        appPackage="ru.mts.smartmed.dev",
                        appActivity="droid.telemed.mts.ru.telemed.ui.activities.SplashScreenActivity")

        elif device == 'bs':
            android_bs_desired_caps = {
                "browserstack.user": "mihajlichenkova_qw6BhZ",
                "browserstack.key": "y3yeqw1uQka89E1TNArL",
                "browserstack.networkLogs": "true",
                "app": "bs://082ce1bbbc013aef850946c7b66d33fd686b6ca6",
                "device": "Samsung Galaxy S20",
                "os_version": "10.0",
                "deviceOrientation": "PORTRAIT",
                "project": "Medsi Autotest",
                "build": "browserstack-build-1",
                "name": "Medsi autotest",
                "noReset": False,
                "autoDismissAlerts": True
            }

            return android_bs_desired_caps

    def get_ios_capabilities(self, device):
        if device == 'simulator':
            return dict(platformName="ios", platformVersion='15.5', deviceName='iPhone X',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app',
                        automationName='XCUITest')
        elif device == 'real device':
            return dict(platformName="ios", platformVersion='15.5', deviceName='iPhone X',
                        udid=f'{self.IOS_UDID}', useNewWDA=True,
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-RealDevice-NativeDemoApp-0.2.1.ipa',
                        automationName='XCUITest')
        elif device == 'bitrise':
            return dict(platformName="ios", platformVersion='15.5', deviceName='iPhone X',
                        udid='E04A6F53-4C3B-4810-B210-DD2015D0D064', useNewWDA=True,
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app',
                        automationName='XCUITest')
        elif device == 'bs':
            ios_bs_desired_caps = {
                "browserstack.user": "mihajlichenkova_qw6BhZ",
                "browserstack.key": "y3yeqw1uQka89E1TNArL",
                "browserstack.networkLogs": "true",
                "app": "bs://016076603f7989b6017a4324e1d664ee3c52d23b",
                "device": "iPhone 13",
                "os_version": "15.5",
                "project": "Medsi autotest",
                "build": "Python iOS",
                "name": "Medsi iOS tests",
                "noReset": "false",
            }
            return ios_bs_desired_caps

    def get_xdist_capabilities(self, app, device):
        if app == 'ios':
            desired_caps = {
                'deviceName': 'iPhone 13',
                'platformName': 'ios',
                'platformVersion': '15.5',
                'automationName': 'XCUITest',
                'app': f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app',
                'noReset': True
            }
            return desired_caps

        elif app == 'android' and device != "bs":
            desired_caps = {
                'platformName': 'android',
                'platformVersion': '',
                'deviceName': 'PF',
                'wdaLocalPort': self.wda_port(),
                'udid': self.ANDROID_UUID,
                'app': self.ANDROID_APK_PATH,
                'noReset': True
            }
            return desired_caps

        elif app == 'android' and device == "bs":
            desired_caps = {
                "browserstack.user": "mihajlichenkova_qw6BhZ",
                "browserstack.key": "y3yeqw1uQka89E1TNArL",
                "app": "bs://c9f51ecb838190d33c50c3af39328370c8d98442",
                "device": "Google Pixel 3",
                "os_version": "9.0",
                "project": "First Python project",
                "build": "browserstack-build-1",
                "name": "first_test"
            }
            return desired_caps
