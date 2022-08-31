from ui_framework.src.helpers.app import App
from src.screens.ios.allow_location import AllowLocationScreen
from src.screens.ios.notification_screen import NotificationScreen
from src.screens.ios.signin_button import SignInButtonScreen
from src.screens.ios.welcome import WelcomeTutorialScreen


class Common(App):

    def skip_intro(self):
        if App.is_exist(self, AllowLocationScreen.skipLocationButton):
            App.click(self, AllowLocationScreen.skipLocationButton)
        if App.is_exist(self, WelcomeTutorialScreen.skip_tutorial_button):
            App.click(self, WelcomeTutorialScreen.skip_tutorial_button)
        if App.is_exist(self, SignInButtonScreen.button):
            App.click(self, SignInButtonScreen.button)

    def skip_notifications(self):
        if App.is_exist(self, NotificationScreen.permitNotificationButton):
            App.click(self, NotificationScreen.permitNotificationButton)
        if App.is_exist(self, NotificationScreen.skipNotificationButtonRu):
            App.click(self, NotificationScreen.skipNotificationButtonRu)
        if App.is_exist(self, NotificationScreen.skipNotificationSettingsRu):
            App.click(self, NotificationScreen.skipNotificationSettingsRu)
        if App.is_exist(self, NotificationScreen.skipNotificationButton):
            App.click(self, NotificationScreen.skipNotificationButton)
