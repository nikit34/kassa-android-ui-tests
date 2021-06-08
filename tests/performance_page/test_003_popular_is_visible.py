from time import sleep
import pytest
from screens.FeaturerMoviesPage import MoviesPage
from locators.featurer_performance_locators import PerformancePageLocators
from screens.FeaturerPerformancesPage import PerformancePage


# @pytest.mark.usefixtures('driver')
# class TestMoviePage:
#     def test_popular_performances_are_visible(self, driver):
#         '''На экране присутствует блок Популярно сейчас '''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*PerformancePageLocators.events, text='Театры')
#         self.performance_page = PerformancePage(driver)
#         self.performance_page.set_custom_wait(10)
#         sleep(5)
#         self.performance_page.act.swipe(50, 80, 50, 20)
#         self.performance_page.act.swipe(50, 60, 50, 40)
#         sleep(1)
#         self.performance_page.matching_text(*PerformancePageLocators.title, pattern='Популярно сейчас')
#         self.performance_page.find_element(*PerformancePageLocators.compilation_img)
#         self.performance_page.find_element(*PerformancePageLocators.event_title)
#         self.performance_page.find_element(*PerformancePageLocators.event_genre)
