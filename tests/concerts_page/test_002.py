import pytest
import allure

from screens.ConcertsPage import ConcertsPage
from screens.MoviesPage import MoviesPage
from locators.movies_locators import MoviesPageLocators
from locators.concerts_locators import ConcertsPageLocators


@pytest.mark.usefixtures('driver')
class TestConcertsPage:
    @classmethod
    def setup_class(cls):
        cls.concerts_locators = ConcertsPageLocators()
        cls.movies_locators = MoviesPageLocators()

    def test_001(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            old_name_event = self.movies_page.find_element(*self.movies_locators.event_name).text
            self.movies_page.click_tab(2)
        with allure.step('ConcertsPage'):
            self.concerts_page = ConcertsPage(driver)
            self.concerts_page.set_custom_wait(20)
            self.concerts_page.matching_text(*self.concerts_locators.event_name, equal=False, pattern=old_name_event)
            self.concerts_page.matching_text(*self.concerts_locators.title, pattern='Популярное')

    def test_002(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click_tab(2)
        with allure.step('ConcertsPage'):
            self.concerts_page = ConcertsPage(driver)
            self.concerts_page.set_custom_wait(20)
            self.concerts_page.check_carousel()
