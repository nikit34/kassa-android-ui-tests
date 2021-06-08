import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.FeaturerPerformancesPage import PerformancePage
from locators.featurer_performance_locators import PerformancePageLocators
from random import randrange


#
# @pytest.mark.usefixtures('driver')
# class TestPerformancePage:
#     def test_check_feature_content(self, driver):
#         '''Каждый event имеет название/описание + время, тег, цену'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*PerformancePageLocators.events, text='Театры')
#         self.performance_page = PerformancePage(driver)
#         self.performance_page.set_custom_wait(10)
#         performance_base_canvas = self.performance_page.find_element(*PerformancePageLocators.carousel_rv)
#         performance_base_canvas_row = self.performance_page.find_element(*PerformancePageLocators.single_session_view)
#
#         random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
#         while True:
#             current_check = random_num % 4
#
#             if current_check == 0:
#                 performance_base_canvas.find_element(*PerformancePageLocators.event_name)
#             elif current_check == 1:
#                 performance_base_canvas_row.find_element(*PerformancePageLocators.session_min_price)
#             elif current_check == 2:
#                 performance_base_canvas_row.find_element(*PerformancePageLocators.session_day_of_month)
#             elif current_check == 3:
#                 performance_base_canvas_row.find_element(*PerformancePageLocators.session_day_of_week_hour_minutes)
#
#             random_num //= 4
#             if random_num == 0:
#                 break
#             self.performance_page.act.swipe(80, 30, 20, 30)

