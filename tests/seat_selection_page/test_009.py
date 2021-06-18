from datetime import datetime
import os
from time import sleep

import allure
import pytest

from locators.checkout_locators import CheckoutPageLocators
from screens.CheckOutPage import CheckOutPage
from screens.MoviesPage import MoviesPage
from screens.InfoPage import InfoPage
from screens.SeatSelectionPage import SeatSelectionPage
from locators.seat_selection_locators import SeatSelectionLocators
from locators.info_locators import InfoPageLocators


@pytest.mark.usefixtures('driver')
class TestPerformancePage:
    @classmethod
    def setup_class(cls):
        cls.info_locators = InfoPageLocators()
        cls.seat_selection_locators = SeatSelectionLocators()
        cls.checkout_locators = CheckoutPageLocators()

    def test_seat_selections_are_opened(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.select_session()
        if not self.movies_page.not_displayed(*self.info_locators.tv_covid_term_btn):
            self.info_page = InfoPage(driver)
            self.info_page.act.swipe(50, 80, 50, 20)
            self.info_page.click(*self.info_locators.cb_covid_term_btn)
            self.info_page.find_element(*self.info_locators.covid_cancel_btn)
            self.info_page.click(*self.info_locators.covid_next_btn)
        self.seat_selection_page = SeatSelectionPage(driver)
        self.seat_selection_page.set_custom_wait(15)
        sleep(5)
        self.seat_selection_page.find_element(*self.seat_selection_locators.hall_scheme)
        self.seat_selection_page.find_element(*self.seat_selection_locators.place_name)
        self.seat_selection_page.find_element(*self.seat_selection_locators.place_session_price)
        self.seat_selection_page.find_element(*self.seat_selection_locators.place_session_tag)
        self.seat_selection_page.find_element(*self.seat_selection_locators.place_session_time)
        self.seat_selection_page.find_element(*self.seat_selection_locators.place_sessions_rv)
        self.seat_selection_page.find_element(*self.seat_selection_locators.back_button)
        self.seat_selection_page.not_displayed(*self.seat_selection_locators.continue_btn)


@pytest.mark.usefixtures('driver_noCache')
class TestPerformancePage:
    def test_seat_selections_are_opened(self, driver):
        now = datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
        path = os.getcwd() + f'/screenshots/session_{now}.png'
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.waiting_main()
        self.movies_page.pass_popup()
        self.movies_page.select_session()
        if not self.movies_page.not_displayed(*self.info_locators.tv_covid_term_btn):
            self.info_page = InfoPage(driver)
            self.info_page.act.swipe(50, 80, 50, 20)
            self.info_page.click(*self.info_locators.cb_covid_term_btn)
            self.info_page.find_element(*self.info_locators.covid_cancel_btn)
            self.info_page.click(*self.info_locators.covid_next_btn)
        self.seat_selection_page = SeatSelectionPage(driver)
        self.seat_selection_page.set_custom_wait(15)
        sleep(5)
        driver.get_screenshot_as_file(path)
        allure.attach.file(path, attachment_type=allure.attachment_type.PNG)
        self.seat_selection_page.select_seat(path)
        self.seat_selection_page.matching_text(*self.seat_selection_locators.continue_btn, pattern='Продолжить')
        os.remove(path)
        self.seat_selection_page.click(*self.seat_selection_locators.continue_btn)
        self.check_out_page = CheckOutPage(driver)
        self.check_out_page.set_custom_wait(15)
        self.check_out_page.find_element(*self.checkout_locators.total_price)
        self.check_out_page.matching_text(*self.checkout_locators.continue_btn, pattern='Продолжить')
