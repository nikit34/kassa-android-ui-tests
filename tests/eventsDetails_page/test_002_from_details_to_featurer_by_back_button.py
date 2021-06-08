import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.EventDetailsPage import EventsDetailsPage
from locators.featurer_movies_locators import MoviesPageLocators
from locators.events_details_locators import EventsDetailsPageLocators


#
# @pytest.mark.usefixtures('driver')
# class TestEventDetailsPage:
#     def test_closing_events_details_by_back_button_(self, driver):
#         '''Выход из Event details через кнопку назад'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*MoviesPageLocators.event_name)
#         self.event_details_page = EventsDetailsPage(driver)
#         self.event_details_page.set_custom_wait(10)
#         self.event_details_page.find_element(*EventsDetailsPageLocators.title)
#         self.event_details_page.click(*EventsDetailsPageLocators.back_button)
#         self.movie_page.find_element(*MoviesPageLocators.movies_title)
