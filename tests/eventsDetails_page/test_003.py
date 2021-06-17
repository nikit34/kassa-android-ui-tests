import pytest

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

    def test_check_event_details(self, driver):
        self.movie_page = MoviesPage(driver)
        self.movie_page.set_custom_wait(15)
        self.movie_page.click(*self.movies_locators.event_name)
        self.event_details_page = EventsDetailsPage(driver)
        self.event_details_page.set_custom_wait(15)
        self.event_details_page.pass_allow_photo_media()
        self.event_details_page.find_element(*self.events_details_locators.like_button)
        self.event_details_page.find_element(*self.events_details_locators.description)
        self.event_details_page.find_element(*self.events_details_locators.back_button)
        self.event_details_page.find_element(*self.events_details_locators.event_trailer)

    def test_closing_events_details_by_back_button_(self, driver):
        self.movie_page = MoviesPage(driver)
        self.movie_page.set_custom_wait(15)
        self.movie_page.click(*self.movies_locators.event_name)
        self.event_details_page = EventsDetailsPage(driver)
        self.event_details_page.set_custom_wait(10)
        self.event_details_page.find_element(*self.events_details_locators.title)
        self.event_details_page.click(*self.events_details_locators.back_button)
        self.movie_page.find_element(*self.movies_locators.movies_title)