from time import sleep
import pytest
import allure

from screens.MoviesPage import MoviesPage
from locators.theaters_locators import TheatersPageLocators
from locators.movies_locators import MoviesPageLocators
from screens.TheatersPage import TheatersPage


@pytest.mark.usefixtures('driver')
class TestTheatersPage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.theaters_locators = TheatersPageLocators()

    def test_001(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            old_name_event = self.movies_page.find_element(*self.movies_locators.event_name).text
            self.movies_page.click_tab(1)
        with allure.step('TheatersPage'):
            self.theaters_page = TheatersPage(driver)
            self.theaters_page.set_custom_wait(20)
            self.theaters_page.matching_text(*self.theaters_locators.event_name, equal=False, pattern=old_name_event)

    def test_002(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click_tab(1)
        with allure.step('TheatersPage'):
            self.theaters_page = TheatersPage(driver)
            self.theaters_page.set_custom_wait(20)
            self.theaters_page.check_carousel()

    def test_003(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movies_page.matching_text(*self.theaters_locators.title, pattern='Уже в продаже')
            self.movies_page.find_element(*self.theaters_locators.event_title)
            self.movies_page.find_element(*self.theaters_locators.event_genre)

