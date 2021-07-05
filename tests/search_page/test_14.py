from time import sleep
import allure
import pytest

from app.debug_api import DebugAPI
from locators.common_locators import CommonLocators
from screens.SearchPage import SearchPage
from screens.MoviesPage import MoviesPage
from locators.search_locators import SearchPageLocators

#
# @pytest.mark.usefixtures('driver')
# class TestFeedPage:
#     @classmethod
#     def setup_class(cls):
#         cls.common_locators = CommonLocators()
#         cls.search_locators = SearchPageLocators()
#
#     def test_001(self, driver):
#         with allure.step('MoviesPage'):
#             self.movies_page = MoviesPage(driver)
#             self.movies_page.set_custom_wait(20)
#             self.movies_page.click(*self.common_locators.tab_search)
#         with allure.step('SearchPage'):
#             self.search_page = SearchPage(driver)
#             self.search_page.set_custom_wait(20)
#             self.search_page.check_count_btn_filters()
#             self.search_page.find_element(*self.search_locators.input_search_field)
#             self.search_page.find_element(*self.search_locators.btn_data_details_movie)
#             self.search_page.find_element(*self.search_locators.text_title_movie)
#             self.search_page.find_element(*self.search_locators.img_movie)
#
#     def test_002(self, driver):
#         dbg_api = DebugAPI.run(request=False, response=True, switch_proxy_driver=driver)
#         try:
#             with allure.step('MoviesPage'):
#                 self.movies_page = MoviesPage(driver)
#                 self.movies_page.set_custom_wait(20)
#                 sleep(4)
#                 self.movies_page.click(*self.common_locators.tab_search)
#             with allure.step('SearchPage'):
#                 self.search_page = SearchPage(driver)
#                 self.search_page.set_custom_wait(20)
#                 sleep(4)
#                 self.search_page.check_btn_filters(dbg_api, url_pattern='/creations/movie/schedule')
#         finally:
#             dbg_api.kill()
#
#     def test_003(self, driver):
#         with allure.step('MoviesPage'):
#             self.movies_page = MoviesPage(driver)
#             self.movies_page.set_custom_wait(20)
#             self.movies_page.click(*self.common_locators.tab_search)
#         with allure.step('SearchPage'):
#             self.search_page = SearchPage(driver)
#             self.search_page.set_custom_wait(20)
#             self.search_page.click_tab(1)
#             self.search_page.check_count_btn_filters()
#             self.search_page.find_element(*self.search_locators.input_search_field)
#             self.search_page.find_element(*self.search_locators.btn_data_details_movie)
#             self.search_page.find_element(*self.search_locators.text_title_movie)
#             self.search_page.find_element(*self.search_locators.img_movie)
#
#     def test_004(self, driver):
#         dbg_api = DebugAPI.run(request=False, response=True, switch_proxy_driver=driver)
#         try:
#             with allure.step('MoviesPage'):
#                 self.movies_page = MoviesPage(driver)
#                 self.movies_page.set_custom_wait(20)
#                 self.movies_page.click(*self.common_locators.tab_search)
#             with allure.step('SearchPage'):
#                 self.search_page = SearchPage(driver)
#                 self.search_page.set_custom_wait(20)
#                 sleep(3)
#                 self.search_page.click_tab(1)
#                 sleep(4)
#                 self.search_page.check_btn_filters(dbg_api, url_pattern='/creations/performance/schedule')
#         finally:
#             dbg_api.kill()
#
#     def test_005(self, driver):
#         with allure.step('MoviesPage'):
#             self.movies_page = MoviesPage(driver)
#             self.movies_page.set_custom_wait(20)
#             self.movies_page.click(*self.common_locators.tab_search)
#         with allure.step('SearchPage'):
#             self.search_page = SearchPage(driver)
#             self.search_page.set_custom_wait(20)
#             self.search_page.click_tab(2)
#             self.search_page.check_count_btn_filters()
#             self.search_page.find_element(*self.search_locators.input_search_field)
#             self.search_page.find_element(*self.search_locators.btn_data_details_movie)
#             self.search_page.find_element(*self.search_locators.text_title_movie)
#             self.search_page.find_element(*self.search_locators.img_movie)
#
#     def test_006(self, driver):
#         dbg_api = DebugAPI.run(request=False, response=True, switch_proxy_driver=driver)
#         try:
#             with allure.step('MoviesPage'):
#                 self.movies_page = MoviesPage(driver)
#                 self.movies_page.set_custom_wait(20)
#                 self.movies_page.click(*self.common_locators.tab_search)
#             with allure.step('SearchPage'):
#                 self.search_page = SearchPage(driver)
#                 self.search_page.set_custom_wait(20)
#                 sleep(3)
#                 self.search_page.click_tab(2)
#                 sleep(4)
#                 self.search_page.check_btn_filters(dbg_api, url_pattern='/creations/concert/schedule')
#         finally:
#             dbg_api.kill()
#
#     def test_007(self, driver):
#         with allure.step('MoviesPage'):
#             self.movies_page = MoviesPage(driver)
#             self.movies_page.set_custom_wait(20)
#             self.movies_page.click(*self.common_locators.tab_search)
#         with allure.step('SearchPage'):
#             self.search_page = SearchPage(driver)
#             self.search_page.set_custom_wait(20)
#             self.search_page.click_tab(3)
#             self.search_page.check_count_btn_filters()
#             self.search_page.find_element(*self.search_locators.input_search_field)
#             self.search_page.find_element(*self.search_locators.btn_data_details_movie)
#             self.search_page.find_element(*self.search_locators.text_title_movie)
#             self.search_page.find_element(*self.search_locators.img_movie)
#
#     def test_008(self, driver):
#         dbg_api = DebugAPI.run(request=False, response=True, switch_proxy_driver=driver)
#         try:
#             with allure.step('MoviesPage'):
#                 self.movies_page = MoviesPage(driver)
#                 self.movies_page.set_custom_wait(20)
#                 self.movies_page.click(*self.common_locators.tab_search)
#             with allure.step('SearchPage'):
#                 self.search_page = SearchPage(driver)
#                 self.search_page.set_custom_wait(20)
#                 sleep(4)
#                 self.search_page.click_tab(3)
#                 sleep(4)
#                 self.search_page.check_btn_filters(dbg_api, url_pattern='/creations/event/schedule')
#         finally:
#             dbg_api.kill()