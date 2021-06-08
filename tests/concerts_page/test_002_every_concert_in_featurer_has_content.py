import pytest
from random import randrange

from screens.FeaturerMoviesPage import MoviesPage
from screens.FeaturerConcertsPage import ConcertsPage
from locators.featurer_concerts_locators import ConcertsPageLocators

#
#
# @pytest.mark.usefixtures('driver')
# class TestConcertsPage:
#     def test_check_feature_content(self, driver):
#         '''Каждый event имеет название/описание + время, тег, цену'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*ConcertsPageLocators.tab, text='Концерты')
#         self.concert_page = ConcertsPage(driver)
#         self.concert_page.set_custom_wait(15)
#         concert_base_canvas = self.concert_page.find_element(*ConcertsPageLocators.carousel_rv)
#         concert_base_canvas_row = self.concert_page.find_element(*ConcertsPageLocators.single_session_view)
#
#         random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
#         while True:
#             current_check = random_num % 4
#
#             if current_check == 0:
#                 concert_base_canvas.find_element(*ConcertsPageLocators.event_name)
#             if current_check == 1:
#                 concert_base_canvas_row.find_element(*ConcertsPageLocators.session_min_price)
#             elif current_check == 2:
#                 concert_base_canvas_row.find_element(*ConcertsPageLocators.session_day_of_month)
#             elif current_check == 3:
#                 concert_base_canvas_row.find_element(*ConcertsPageLocators.session_day_of_week_hour_minutes)
#
#             random_num //= 4
#             if random_num == 0:
#                 break
#             self.concert_page.act.swipe(80, 30, 20, 30)
