from random import randrange
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

    def test_theaters_page_is_opened(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            old_name_event = self.movies_page.find_element(*self.movies_locators.event_name).text
            self.movies_page.click_tab(1)
        with allure.step('TheatersPage'):
            self.theaters_page = TheatersPage(driver)
            self.theaters_page.set_custom_wait(20)
            self.theaters_page.click(*self.theaters_locators.events)
            self.theaters_page.matching_text(*self.theaters_locators.event_name, equal=False, pattern=old_movie_title)

    def test_check_feature_content(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.theaters_locators.events)
        theaters_base_canvas = self.movies_page.find_element(*self.theaters_locators.carousel_rv)
        theaters_base_canvas_row = self.movies_page.find_element(*self.theaters_locators.single_session_view)

        random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
        while True:
            current_check = random_num % 4

            if current_check == 0:
                theaters_base_canvas.find_element(*self.theaters_locators.event_name)
            elif current_check == 1:
                theaters_base_canvas_row.find_element(*self.theaters_locators.session_min_price)
            elif current_check == 2:
                theaters_base_canvas_row.find_element(*self.theaters_locators.session_day_of_month)
            elif current_check == 3:
                theaters_base_canvas_row.find_element(*self.theaters_locators.session_day_of_week_hour_minutes)

            random_num //= 4
            if random_num == 0:
                break
            self.movies_page.act.swipe(80, 30, 20, 30)

    def test_popular_theaterss_are_visible(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.theaters_locators.events)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.matching_text(*self.theaters_locators.title, pattern='Популярно сейчас')
        self.movies_page.find_element(*self.theaters_locators.compilation_img)
        self.movies_page.find_element(*self.theaters_locators.event_title)
        self.movies_page.find_element(*self.theaters_locators.event_genre)

