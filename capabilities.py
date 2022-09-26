import os

from src.data.capabilities_data_gen import (AndroidCapDataGen, IosCapDataGen,
                                            BsCapDataGen)


class Capabilities:
    COMMAND_EXECUTOR = {
        "bs": "http://hub-cloud.browserstack.com/wd/hub",
        "not_bs": "http://127.0.0.1:4723/wd/hub"
    }
    CURRENT_EXECUTOR = ""

    @staticmethod
    def wda_port() -> int:
        if os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
            return 8101
        else:
            return 8100

    def get_android_capabilities(self, device: str) -> dict:
        if device != 'bs':
            self.CURRENT_EXECUTOR = self.COMMAND_EXECUTOR["not_bs"]
            caps = AndroidCapDataGen()
            return caps.get_android_caps()

        elif device == "bs":
            self.CURRENT_EXECUTOR = self.COMMAND_EXECUTOR["bs"]
            caps = BsCapDataGen(app="bs://ebc838b43169950561cc647e09424ae3e8c1d300",
                                device="Samsung Galaxy S20",
                                os_version="10.0",
                                project="Medsi Autotest",
                                build="browserstack-build-1",
                                name="Medsi autotest"
                                )
            return caps.get_bs_caps()

    def get_ios_capabilities(self, device: str) -> dict:
        if device != "bs":
            self.CURRENT_EXECUTOR = self.COMMAND_EXECUTOR["not_bs"]
            caps = IosCapDataGen()
            return caps.get_ios_caps()

        elif device == "bs":
            self.CURRENT_EXECUTOR = self.COMMAND_EXECUTOR["bs"]
            caps = BsCapDataGen(app="bs://016076603f7989b6017a4324e1d664ee3c52d23b",
                                device="iPhone 13",
                                os_version="15.5",
                                project="Medsi Autotest",
                                build="Python iOS",
                                name="Medsi iOS tests",
                                )
            return caps.get_bs_caps()

    def get_capabilities(self, device: str, app: str) -> dict:
        """
        :param device:
        :param app:
        :return:
        """
        if app == "android" and device != "bs":
            return self.get_android_capabilities(device=device)
        if app == "android" and device == "bs":
            return self.get_android_capabilities(device=device)

        if app == "ios" and device != "bs":
            return self.get_ios_capabilities(device=device)
        if app == "ios" and device == "bs":
            return self.get_ios_capabilities(device=device)
