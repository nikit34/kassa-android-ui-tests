from time import sleep

import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.EventDetailsPage import EventsDetailsPage
from locators.movies_locators import MoviesPageLocators
from locators.events_details_locators import EventsDetailsPageLocators


@pytest.mark.usefixtures('driver')
class TestEventDetailsPage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.events_details_locators = EventsDetailsPageLocators()

    def test_001(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.movies_locators.event_name)
        with allure.step('EventsDetailsPage'):
            self.event_details_page = EventsDetailsPage(driver)
            self.event_details_page.set_custom_wait(20)
            self.event_details_page.find_element(*self.events_details_locators.title)
            self.event_details_page.find_element(*self.events_details_locators.like_button)
            self.event_details_page.find_element(*self.events_details_locators.description)
            self.event_details_page.find_element(*self.events_details_locators.back_button)
            self.event_details_page.find_element(*self.events_details_locators.btn_shedule_ticket)

    def test_002(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.movies_locators.event_name)
        with allure.step('EventsDetailsPage'):
            self.event_details_page = EventsDetailsPage(driver)
            self.event_details_page.set_custom_wait(20)
            self.event_details_page.find_element(*self.events_details_locators.title)
            self.event_details_page.click(*self.events_details_locators.back_button)
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.find_element(*self.movies_locators.movies_title)

    def test_003(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            self.movies_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            self.movies_page.click(*self.movies_locators.img_event)
        with allure.step('EventDetailsPage'):
            self.event_details_page = EventsDetailsPage(driver)
            self.event_details_page.set_custom_wait(20)
            self.event_details_page.find_element(*self.events_details_locators.description)

    def test_004(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            sleep(5)
            self.movies_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            old_event_title = self.movies_page.find_element(*self.movies_locators.event_title).text
            self.movies_page.click(*self.movies_locators.event_title)
        with allure.step('EventsDetailsPage'):
            self.events_details_page = EventsDetailsPage(driver)
            self.events_details_page.set_custom_wait(20)
            self.events_details_page.matching_text(*self.events_details_locators.title, equal=True, pattern=old_event_title)

