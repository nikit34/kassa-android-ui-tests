from datetime import datetime
import os
from time import sleep

import allure
import pytest

from locators.checkout_locators import CheckoutPageLocators
from screens.MoviesPage import MoviesPage
from screens.InfoPage import InfoPage
from screens.SeatSelectionPage import SeatSelectionPage
from locators.seat_selection_locators import SeatSelectionLocators
from locators.info_locators import InfoPageLocators


@pytest.mark.usefixtures('driver')
class TestTheatersPage:
    @classmethod
    def setup_class(cls):
        cls.info_locators = InfoPageLocators()
        cls.seat_selection_locators = SeatSelectionLocators()
        cls.checkout_locators = CheckoutPageLocators()

    def test_seat_selections_are_opened(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            if not self.info_page.not_displayed(*self.info_locators.btn_tv_covid_term):
                self.info_page.act.swipe(50, 80, 50, 20)
                self.info_page.click(*self.info_locators.btn_cb_covid_term)
                self.info_page.find_element(*self.info_locators.btn_covid_cancel)
                self.info_page.click(*self.info_locators.btn_covid_next)
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(20)
            sleep(5)
            self.seat_selection_page.find_element(*self.seat_selection_locators.hall_scheme)
            self.seat_selection_page.find_element(*self.seat_selection_locators.place_name)
            self.seat_selection_page.find_element(*self.seat_selection_locators.place_session_price)
            self.seat_selection_page.find_element(*self.seat_selection_locators.place_session_tag)
            self.seat_selection_page.find_element(*self.seat_selection_locators.place_session_time)
            self.seat_selection_page.find_element(*self.seat_selection_locators.place_sessions_rv)
            self.seat_selection_page.find_element(*self.seat_selection_locators.back_button)
            self.seat_selection_page.not_displayed(*self.seat_selection_locators.btn_continue)

