import pytest
import allure
from random import randrange

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

    def test_concerts_page_is_opened(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(15)
            old_name_event = self.movies_page.find_element(*self.movies_locators.event_name).text
            self.movies_page.click_tab(2)
        with allure.step('ConcertsPage'):
            self.concerts_page = ConcertsPage(driver)
            self.concerts_page.matching_text(*self.concerts_locators.event_name, equal=False, pattern=old_name_event)
            self.concerts_page.matching_text(*self.concerts_locators.title, pattern='Популярное')

    def test_check_feature_content(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(15)
        concert_base_canvas = self.movies_page.find_element(*self.concerts_locators.carousel_rv)
        concert_base_canvas_row = self.movies_page.find_element(*self.concerts_locators.single_session_view)

        random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
        while True:
            current_check = random_num % 3

            if current_check == 0:
                concert_base_canvas.find_element(*self.concerts_locators.event_name)
            if current_check == 1:
                concert_base_canvas_row.find_element(*self.concerts_locators.session_price)
            elif current_check == 2:
                concert_base_canvas_row.find_element(*self.concerts_locators.session_date)

            random_num //= 4
            if random_num == 0:
                break
            self.concert_page.act.swipe(80, 30, 20, 30)
