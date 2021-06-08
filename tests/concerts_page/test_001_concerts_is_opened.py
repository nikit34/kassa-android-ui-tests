import pytest

from screens.FeaturerMoviesPage import MoviesPage
from screens.FeaturerConcertsPage import ConcertsPage
from locators.featurer_movies_locators import MoviesPageLocators
from locators.featurer_concerts_locators import ConcertsPageLocators

#
#
# @pytest.mark.usefixtures('driver')
# class TestConcertsPage:
#     def test_concerts_page_is_opened(self, driver):
#         '''Вкладка Концерты открыта'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         old_name_event = self.movie_page.find_element(*MoviesPageLocators.event_name).text
#         self.concerts_page = ConcertsPage(driver)
#         self.concerts_page.set_custom_wait(15)
#         self.concerts_page.click(*ConcertsPageLocators.tab, text='Концерты')
#         self.concerts_page.matching_text(*ConcertsPageLocators.event_name, equal=False, pattern=old_name_event)
#         self.concerts_page.matching_text(*ConcertsPageLocators.title, pattern='Топовые концерты')
