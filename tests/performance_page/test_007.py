from random import randrange
from time import sleep
import pytest

from screens.MoviesPage import MoviesPage
from locators.performance_locators import PerformancePageLocators
from locators.movies_locators import MoviesPageLocators


@pytest.mark.usefixtures('driver')
class TestPerformancePage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.performance_locators = PerformancePageLocators()

    def test_performance_page_is_opened(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.find_element(*self.movies_locators.event_name)
        old_movie_title = self.movies_page.find_element(*self.movies_locators.movies_title).text
        self.movies_page.click(*self.performance_locators.events, text='Театры')
        self.movies_page.matching_text(*self.performance_locators.event_name, equal=False, pattern=old_movie_title)

    def test_check_feature_content(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.performance_locators.events, text='Театры')
        performance_base_canvas = self.performance_page.find_element(*self.performance_locators.carousel_rv)
        performance_base_canvas_row = self.performance_page.find_element(*self.performance_locators.single_session_view)

        random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
        while True:
            current_check = random_num % 4

            if current_check == 0:
                performance_base_canvas.find_element(*self.performance_locators.event_name)
            elif current_check == 1:
                performance_base_canvas_row.find_element(*self.performance_locators.session_min_price)
            elif current_check == 2:
                performance_base_canvas_row.find_element(*self.performance_locators.session_day_of_month)
            elif current_check == 3:
                performance_base_canvas_row.find_element(*self.performance_locators.session_day_of_week_hour_minutes)

            random_num //= 4
            if random_num == 0:
                break
            self.movies_page.act.swipe(80, 30, 20, 30)

    def test_popular_performances_are_visible(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.performance_locators.events, text='Театры')
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.matching_text(*self.performance_locators.title, pattern='Популярно сейчас')
        self.movies_page.find_element(*self.performance_locators.compilation_img)
        self.movies_page.find_element(*self.performance_locators.event_title)
        self.movies_page.find_element(*self.performance_locators.event_genre)

