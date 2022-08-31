from time import sleep

import pytest

from src.helpers.app import App
from src.helpers.appiumdriver import Driver
from src.model.AppDataModel import Patient
from src.screens.ios.home import HomeScreen


class MainScreenTest(Driver):
    LOGIN_PATIENT = Patient(phone="8888887766", password="00000000", name="Vbb Ghhj")

    @pytest.mark.carousel
    def test_carousel_swipe(self):
        """
        verify carousel swipe
        """
        self.logger.info("Carousel test")
        App.wait_until_exists(self, HomeScreen.carousel_maintenance)
        # content unstable
        # App.wait_until_exists(self, HomeScreen.carousel_liposuction)
        # App.wait_until_exists(self, HomeScreen.carousel_motherschool)
        App.swipe_percent(self, 0.9, 0.25, 0.720, 0.25)
        App.wait_until_not_visible(self, HomeScreen.carousel_maintenance)
        App.swipe_percent(self, 0.720, 0.25, 0.900, 0.25)
        App.wait_until_exists(self, HomeScreen.carousel_maintenance)

    @pytest.mark.carousel
    def test_carousel_click(self):
        """
        verify carousel click and close
        """
        self.logger.info("Carousel test")
        App.wait_until_clickable(self, HomeScreen.carousel_maintenance)
        App.tap(self, HomeScreen.carousel_maintenance)
        sleep(2)
        App.is_displayed(self, HomeScreen.carousel_image_close)
        App.click(self, HomeScreen.carousel_image_close)
        App.is_displayed(self, HomeScreen.main_header)
