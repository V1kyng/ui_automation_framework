from appium import webdriver

#from settings import IOS_BS_DESIRED_CAPS


class RemoteDriver():
    driver = webdriver.Remote(
        command_executor="http://hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=IOS_BS_DESIRED_CAPS
    )
