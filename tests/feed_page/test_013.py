import allure
import pytest
from time import sleep

from locators.movies_locators import MoviesPageLocators
from locators.feed_locators import FeedPageLocators
from screens.MoviesPage import MoviesPage
from screens.FeedPage import FeedPage

#
# @pytest.mark.usefixtures('driver')
# class TestFeedPage:
#     @classmethod
#     def setup_class(cls):
#         cls.movies_locators = MoviesPageLocators()
#         cls.feed_locators = FeedPageLocators()
#
#     def test_001(self, driver):
#         with allure.step('MoviesPage'):
#             self.movies_page = MoviesPage(driver)
#             self.movies_page.set_custom_wait(20)
#             sleep(5)
#             self.movies_page.act.swipe(50, 80, 50, 20)
#             self.movies_page.act.swipe(50, 60, 50, 40)
#             sleep(1)
#             self.movies_page.click(*self.movies_locators.movies_title)
#         with allure.step('FeedPage'):
#             self.feed_page = FeedPage(driver)
#             self.feed_page.set_custom_wait(20)
#             self.feed_page.find_element(*self.feed_locators.input_search)
#             self.feed_page.find_element(*self.feed_locators.btn_filters)
#             self.feed_page.find_element(*self.feed_locators.img_events)
#             self.feed_page.find_element(*self.feed_locators.btn_back)
#             self.feed_page.find_element(*self.feed_locators.btn_fast_buy)
#             self.feed_page.find_element(*self.feed_locators.btn_events_name)