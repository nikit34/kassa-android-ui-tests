from time import sleep
import allure
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

    def test_001(self, driver):
        with allure.step('MoviesPage'):
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

    def test_002(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.find_element(*self.movies_locators.movies_title)
            self.movies_page.check_carousel()

    def test_003(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.movies_locators.fastbuy_ticket_id)
        with allure.step('ShedulePage'):
            self.shedule_page = ShedulePage(driver)
            self.shedule_page.set_custom_wait(20)
            self.shedule_page.find_element(*self.shedule_locators.event_name)

    def test_004(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(2)
            self.movies_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            self.movies_page.not_displayed(*self.movies_locators.feature_app_bar)
            self.movies_page.not_displayed(*self.movies_locators.tabs_rv)

    def test_005(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click_random(*self.movies_locators.img_popular_movies, 2)
        with allure.step('EventsDetailsPage'):
            self.event_detail_page = EventsDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.find_element(*self.events_details_locators.description)

    def test_006(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 20, 50, 80)
            sleep(1)
            self.movies_page.find_element(*self.movies_locators.feature_app_bar)
            self.movies_page.find_element(*self.movies_locators.tabs_rv)

    def test_007(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            self.movies_page.find_element(*self.movies_locators.favorite_container)
            self.movies_page.find_element(*self.movies_locators.text_location)
            self.movies_page.find_element(*self.movies_locators.text_underground)

    def test_008(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.movies_locators.fastbuy_ticket_id)
        with allure.step('ShedulePage'):
            self.shedule_page = ShedulePage(driver)
            self.shedule_page.set_custom_wait(20)
            self.shedule_page.click(*self.shedule_locators.back_button)
        with allure.step('EventsDetailsPage'):
            self.event_details_page = EventsDetailsPage(driver)
            self.event_details_page.set_custom_wait(20)
            self.event_details_page.find_element(*self.events_details_locators.description)

    def test_009(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(2)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movies_page.click(*self.movies_locators.arrow_right)
            self.movies_page.find_element(*self.shedule_locators.event_name)

    def test_010(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movies_page.matching_text(*self.movies_locators.movies_title, pattern='Популярное')

    def test_011(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            self.movies_page.matching_text(*self.movies_locators.movies_title, pattern='Уже в продаже')

    def test_from_premier_into_event_details(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movies_page.click(*self.movies_locators.movies_title)
            self.movies_page.click(*self.movies_locators.event_name)
        with allure.step('EventsDetailsPage'):
            self.events_details_page = EventsDetailsPage(driver)
            self.events_details_page.set_custom_wait(20)
            self.events_details_page.find_element(*self.events_details_locators.title)

    def test_premiers_are_available_(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movies_page.click(*self.movies_locators.arrow_right)
        with allure.step('ShedulePage'):
            self.schedule_page = ShedulePage(driver)
            self.schedule_page.set_custom_wait(20)
            self.schedule_page.click(*self.shedule_locators.fastbuy_ticket_id)
            self.schedule_page.find_element(*self.shedule_locators.session_sheet)

    def test_close_premier_schedule_sheet_from_carousel(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movies_page.click(*self.movies_locators.arrow_right)
            self.movies_page.click(*self.movies_locators.fastbuy_ticket_id)
        with allure.step('ShedulePage'):
            self.schedule_page = ShedulePage(driver)
            self.schedule_page.set_custom_wait(20)
            self.schedule_page.click(*self.shedule_locators.back_bar_button)
        with allure.step('EventsDetailsPage'):
            self.event_details_page = EventsDetailsPage(driver)
            self.event_details_page.set_custom_wait(20)
            self.event_details_page.find_element(*self.events_details_locators.title)

    def test_close_premier_schedule_sheet_from_carousel_(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.movies_locators.img_popular_movies)
        with allure.step('MoviesPage'):
            self.event_detail_page = EventsDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.pass_allow_photo_media()
            self.event_detail_page.find_element(*self.events_details_locators.title)
            self.event_detail_page.click(*self.events_details_locators.back_button)
        with allure.step('MoviesPage'):
            self.movies_page.find_element(*self.movies_locators.list_session_view)


