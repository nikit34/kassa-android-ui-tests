import pytest
import allure
from time import sleep

from screens.MoviesPage import MoviesPage
from screens.SeatSelectionPage import SeatSelectionPage
from screens.CheckOutPage import CheckOutPage
from screens.InfoPage import InfoPage
from locators.seat_selection_locators import SeatSelectionLocators
from locators.checkout_locators import CheckoutPageLocators
from locators.info_locators import InfoPageLocators
from app.debug_api import DebugAPI


@pytest.mark.usefixtures('driver')
class TestTheatersPage:
    @classmethod
    def setup_class(cls):
        cls.seat_selection_locators = SeatSelectionLocators()
        cls.checkout_locators = CheckoutPageLocators()
        cls.info_locators = InfoPageLocators()

    def test_001(self, driver):
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(20)
            self.seat_selection_page.skip_seat_selection()
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('CheckOutPage'):
            self.check_out_page = CheckOutPage(driver)
            self.check_out_page.set_custom_wait(20)
            self.check_out_page.find_element(*self.checkout_locators.text_total_price)
            self.check_out_page.find_element(*self.checkout_locators.text_event_title)
            self.check_out_page.find_element(*self.checkout_locators.btn_continue)

    def test_002(self, driver):
        with allure.step('MoviesPage'):
            dbg_api = DebugAPI.run(request=False, response=True, switch_proxy_driver=False)
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.select_session()
            sleep(2)
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            if 'ageRestriction' in self.info_page.recognize_page(dbg_api):
                self.info_page.find_element(*self.info_locators.btn_cancel)
                self.info_page.click(*self.info_locators.btn_accept_years)
            if 'covidNotification' in self.info_page.recognize_page(dbg_api):
                self.info_page.pass_without_info()
            dbg_api.kill()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(20)
            self.seat_selection_page.skip_seat_selection(dbg_select_seat=False)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('CheckOutPage'):
            self.check_out_page = CheckOutPage(driver)
            self.check_out_page.set_custom_wait(20)
            sleep(2)
            self.check_out_page.act.swipe(50, 60, 50, 40)
            self.check_out_page.input('n.permyakov@rambler-co.ru', *self.checkout_locators.input_email)
            self.check_out_page.input('9779918074', *self.checkout_locators.input_phone)
            self.check_out_page.click(*self.checkout_locators.btn_continue)
