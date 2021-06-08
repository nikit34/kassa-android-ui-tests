import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.ShedulePage import ShedulePage
from locators.shedule_locators import ShedulePageLocators
from locators.featurer_movies_locators import MoviesPageLocators

#
# @pytest.mark.usefixtures('driver')
# class TestShedulePage:
#     def test_shedule_has_input_field(self, driver):
#         '''Инпут для ввода присутствует на экране'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*MoviesPageLocators.fastbuy_ticket_id)
#         self.shedule_page = ShedulePage(driver)
#         self.shedule_page.set_custom_wait(10)
#         self.shedule_page.find_element(*ShedulePageLocators.search_field)

