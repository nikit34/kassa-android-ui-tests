import pytest

from screens.FeaturerMoviesPage import MoviesPage
from screens.EventDetailsPage import EventsDetailsPage
from locators.featurer_movies_locators import MoviesPageLocators
from locators.events_details_locators import EventsDetailsPageLocators

#
# @pytest.mark.usefixtures('driver')
# class TestEventDetailsPage:
#     def test_check_event_details(self, driver):
#         '''Event details показывается после закрытия расписания'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*MoviesPageLocators.event_name)
#         self.event_details_page = EventsDetailsPage(driver)
#         self.event_details_page.set_custom_wait(15)
#         self.event_details_page.pass_allow_photo_media()
#         self.event_details_page.find_element(*EventsDetailsPageLocators.like_button)
#         self.event_details_page.find_element(*EventsDetailsPageLocators.description)
#         self.event_details_page.find_element(*EventsDetailsPageLocators.back_button)
#         self.event_details_page.find_element(*EventsDetailsPageLocators.event_trailer)
