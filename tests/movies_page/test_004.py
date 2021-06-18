from random import randrange
from time import sleep

import pytest

from locators.events_details_locators import EventsDetailsPageLocators
from locators.movies_locators import MoviesPageLocators
from locators.shedule_locators import ShedulePageLocators
from screens.EventDetailsPage import EventsDetailsPage
from screens.MoviesPage import MoviesPage
from locators.common_locators import CommonLocators
from screens.ShedulePage import ShedulePage


@pytest.mark.usefixtures('driver')
class TestMoviePage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.movies_locators = MoviesPageLocators()
        cls.events_details_locators = EventsDetailsPageLocators()
        cls.shedule_locators = ShedulePageLocators()

    def test_tab_movie_is_selected_when_app_opened(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        tab_trend = self.movies_page.find_element(*self.common_locators.tab_trend)
        assert tab_trend.is_selected(), f'invalid state: {tab_trend}'
        tab_search = self.movies_page.find_element(*self.common_locators.tab_search)
        assert not tab_search.is_selected(), f'invalid state: {tab_search}'
        tab_ticket = self.movies_page.find_element(*self.common_locators.tab_ticket)
        assert not tab_ticket.is_selected(), f'invalid state: {tab_ticket}'
        tab_places = self.movies_page.find_element(*self.common_locators.tab_places)
        assert not tab_places.is_selected(), f'invalid state: {tab_places}'
        tab_profile = self.movies_page.find_element(*self.common_locators.tab_profile)
        assert not tab_profile.is_selected(), f'invalid state: {tab_profile}'

    def test_check_feature_content(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.find_element(*self.movies_locators.movies_title)
        movie_base_canvas = self.movies_page.find_element(*self.movies_locators.carousel_rv)
        movie_base_canvas_row = self.movies_page.find_element(*self.movies_locators.list_session_view)

        random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
        while True:
            current_check = random_num % 4

            if current_check == 0:
                movie_base_canvas.find_element(*self.movies_locators.event_name)
            elif current_check == 1:
                movie_base_canvas.find_element(*self.movies_locators.place_label)
            elif current_check == 2:
                movie_base_canvas_row.find_element(*self.movies_locators.session_date)
            elif current_check == 3:
                movie_base_canvas_row.find_element(*self.movies_locators.session_price)

            random_num //= 4
            if random_num == 0:
                break
            self.movies_page.act.swipe(80, 30, 20, 30)

    def test_fastbuy_button_is_working(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.movies_locators.fastbuy_ticket_id)
        self.shedule_page = ShedulePage(driver)
        self.shedule_page.set_custom_wait(20)
        self.shedule_page.find_element(*self.shedule_locators.event_name)

    def test_hiding_eventstabs_after_swipe_down(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(2)
        self.movies_page.act.swipe(50, 80, 50, 20)
        sleep(1)
        self.movies_page.not_displayed(*self.movies_locators.feature_app_bar)
        self.movies_page.not_displayed(*self.movies_locators.tabs_rv)

    def test_top_movies_are_visible(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.find_element(*self.movies_locators.event_img)

    def test_top_movie_is_opened_from_featurer(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click_random(*self.movies_locators.event_img, 3)
        self.event_detail_page = EventsDetailsPage(driver)
        self.event_detail_page.set_custom_wait(20)
        self.event_detail_page.find_element(*self.events_details_locators.description)

    def test_hide_and_show_up_headers_tabs(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 20, 50, 80)
        sleep(1)
        self.movies_page.find_element(*self.movies_locators.feature_app_bar)
        self.movies_page.find_element(*self.movies_locators.tabs_rv)

    def test_popular_movies_are_visible(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.find_element(*self.movies_locators.compilation_img)
        self.movies_page.find_element(*self.movies_locators.favorite_container)

    def test_premiers_are_available(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 55, 50, 45)
        sleep(1)
        self.movies_page.matching_text(*self.movies_locators.movies_title, pattern='Скоро в кино')
        self.movies_page.find_element(*self.movies_locators.carousel_rv)

    def test_flop_into_popular_movie(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.click(*self.movies_locators.compilation_img)
        self.movies_page.pass_allow_photo_media()
        self.movies_page.find_element(*self.events_details_locators.btn_shedule_ticket)

    def test_closing_schedule_to_event_detail(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.movies_locators.fastbuy_ticket_id)
        self.shedule_page = ShedulePage(driver)
        self.shedule_page.set_custom_wait(15)
        self.shedule_page.pass_allow_photo_media()
        self.shedule_page.click(*self.shedule_locators.back_button)
        self.event_details_page = EventsDetailsPage(driver)
        self.event_details_page.set_custom_wait(15)
        self.event_details_page.find_element(*self.events_details_locators.description)

    def test_popular_movies_are_visible(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 80, 50, 20)
        sleep(1)
        self.movies_page.click(*self.movies_locators.event_title)
        self.movies_page.find_element(*self.events_details_locators.btn_shedule_ticket)

    def test_popular_movies_are_visible_(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(2)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.click(*self.movies_locators.arrow_right)
        self.movies_page.find_element(*self.shedule_locators.event_name)

    def test_popular_movies_are_visible__(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 80, 50, 20)
        sleep(1)
        self.movies_page.click(*self.movies_locators.event_title)
        self.movies_page.find_element(*self.events_details_locators.description)

    def test_premiers_are_available(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.matching_text(*self.movies_locators.movies_title, pattern='Скоро в кино')
        self.movies_page.click(*self.movies_locators.movies_title)
        self.movies_page.find_element(*self.movies_locators.event_name)

    def test_from_premier_into_event_details(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.click(*self.movies_locators.movies_title)
        self.movies_page.click(*self.movies_locators.event_name)
        self.events_details_page = EventsDetailsPage(driver)
        self.movies_page.set_custom_wait(15)
        self.events_details_page.find_element(*self.events_details_locators.title)

    def test_premiers_are_available_(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.click(*self.movies_locators.arrow_right)
        self.schedule_page = ShedulePage(driver)
        self.schedule_page.set_custom_wait(20)
        self.schedule_page.click(*self.shedule_locators.fastbuy_ticket_id)
        self.schedule_page.find_element(*self.shedule_locators.session_sheet)

    def test_close_premier_schedule_sheet_from_carousel(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        sleep(5)
        self.movies_page.act.swipe(50, 80, 50, 20)
        self.movies_page.act.swipe(50, 60, 50, 40)
        sleep(1)
        self.movies_page.click(*self.movies_locators.arrow_right)
        self.movies_page.click(*self.movies_locators.fastbuy_ticket_id)
        self.schedule_page = ShedulePage(driver)
        self.schedule_page.set_custom_wait(20)
        self.schedule_page.click(*self.shedule_locators.back_bar_button)
        self.event_details_page = EventsDetailsPage(driver)
        self.event_details_page.find_element(*self.events_details_locators.title)

    def test_close_premier_schedule_sheet_from_carousel_(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.movies_locators.event_img)
        self.event_detail_page = EventsDetailsPage(driver)
        self.event_detail_page.set_custom_wait(20)
        self.event_detail_page.pass_allow_photo_media()
        self.event_detail_page.find_element(*self.events_details_locators.title)
        self.event_detail_page.click(*self.events_details_locators.back_button)
        self.movies_page.find_element(*self.movies_locators.list_session_view)


