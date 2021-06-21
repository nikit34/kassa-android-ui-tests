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