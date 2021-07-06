import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.ShedulePage import ShedulePage
from locators.shedule_locators import ShedulePageLocators
from locators.movies_locators import MoviesPageLocators


@pytest.mark.usefixtures('driver')
class TestShedulePage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.shedule_locators = ShedulePageLocators()

    def test_001(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.movies_locators.fastbuy_ticket_id)
        with allure.step('ShedulePage'):
            self.shedule_page = ShedulePage(driver)
            self.shedule_page.set_custom_wait(20)
            self.shedule_page.find_element(*self.shedule_locators.event_name)
            self.shedule_page.find_element(*self.shedule_locators.back_bar_button)
            self.shedule_page.find_element(*self.shedule_locators.map_button)
            self.shedule_page.find_element(*self.shedule_locators.sheduler_place_name)
            self.shedule_page.find_element(*self.shedule_locators.sheduler_place_address)
            self.shedule_page.find_element(*self.shedule_locators.sheduler_geo_location_button)
            self.shedule_page.find_element(*self.shedule_locators.filters)
            self.shedule_page.find_element(*self.shedule_locators.search_field)