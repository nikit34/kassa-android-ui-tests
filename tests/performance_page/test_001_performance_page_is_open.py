import pytest

from screens.FeaturerMoviesPage import MoviesPage
from screens.FeaturerPerformancesPage import PerformancePage
from locators.featurer_performance_locators import PerformancePageLocators
from locators.featurer_movies_locators import MoviesPageLocators


# @pytest.mark.usefixtures('driver')
# class TestPerformancePage:
#     def test_performance_page_is_opened(self, driver):
#         '''Вкладка Спектакли открыта'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.find_element(*MoviesPageLocators.event_name)
#         old_movie_title = self.movie_page.find_element(*MoviesPageLocators.movies_title).text
#         self.movie_page.click(*PerformancePageLocators.events, text='Театры')
#         self.performance_page = PerformancePage(driver)
#         self.performance_page.set_custom_wait(15)
#         self.performance_page.matching_text(*PerformancePageLocators.event_name, equal=False, pattern=old_movie_title)
