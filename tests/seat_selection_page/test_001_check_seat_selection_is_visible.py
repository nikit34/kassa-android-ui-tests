from time import sleep
import pytest

from screens.FeaturerMoviesPage import MoviesPage
from screens.InfoPage import InfoPage
from screens.SeatSelectionPage import SeatSelectionPage
from locators.seat_selection_locators import SeatSelectionLocators
from locators.info_locators import InfoPageLocators

#
# @pytest.mark.usefixtures('driver')
# class TestPerformancePage:
#     def test_seat_selections_are_opened(self, driver):
#         '''Выбор места открыт'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.select_session()
#         if not self.movie_page.not_displayed(*InfoPageLocators.tv_covid_term_btn):
#             self.info_page = InfoPage(driver)
#             self.info_page.act.swipe(50, 80, 50, 20)
#             self.info_page.click(*InfoPageLocators.cb_covid_term_btn)
#             self.info_page.find_element(*InfoPageLocators.covid_cancel_btn)
#             self.info_page.click(*InfoPageLocators.covid_next_btn)
#         self.seat_selection_page = SeatSelectionPage(driver)
#         self.seat_selection_page.set_custom_wait(10)
#         sleep(5)
#         self.seat_selection_page.find_element(*SeatSelectionLocators.hall_scheme)
#         self.seat_selection_page.find_element(*SeatSelectionLocators.place_name)
#         self.seat_selection_page.find_element(*SeatSelectionLocators.place_session_price)
#         self.seat_selection_page.find_element(*SeatSelectionLocators.place_session_tag)
#         self.seat_selection_page.find_element(*SeatSelectionLocators.place_session_time)
#         self.seat_selection_page.find_element(*SeatSelectionLocators.place_sessions_rv)
#         self.seat_selection_page.find_element(*SeatSelectionLocators.back_button)
#         self.seat_selection_page.not_displayed(*SeatSelectionLocators.continue_btn)
