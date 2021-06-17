import pytest
from random import randrange

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
        self.movie_page = MoviesPage(driver)
        self.movie_page.set_custom_wait(15)
        old_name_event = self.movie_page.find_element(*self.movies_locators.event_name).text
        self.movie_page.click(*self.concerts_locators.tab, text='Концерты')
        self.movie_page.matching_text(*self.concerts_locators.event_name, equal=False, pattern=old_name_event)
        self.movie_page.matching_text(*self.concerts_locators.title, pattern='Топовые концерты')

    def test_check_feature_content(self, driver):
        self.movie_page = MoviesPage(driver)
        self.movie_page.set_custom_wait(15)
        self.movie_page.click(*self.concerts_locators.tab, text='Концерты')
        self.movie_page.set_custom_wait(15)
        concert_base_canvas = self.movie_page.find_element(*self.concerts_locators.carousel_rv)
        concert_base_canvas_row = self.movie_page.find_element(*self.concerts_locators.single_session_view)

        random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
        while True:
            current_check = random_num % 4

            if current_check == 0:
                concert_base_canvas.find_element(*self.concerts_locators.event_name)
            if current_check == 1:
                concert_base_canvas_row.find_element(*self.concerts_locators.session_min_price)
            elif current_check == 2:
                concert_base_canvas_row.find_element(*self.concerts_locators.session_day_of_month)
            elif current_check == 3:
                concert_base_canvas_row.find_element(*self.concerts_locators.session_day_of_week_hour_minutes)

            random_num //= 4
            if random_num == 0:
                break
            self.concert_page.act.swipe(80, 30, 20, 30)
