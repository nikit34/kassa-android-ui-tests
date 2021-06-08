from datetime import datetime
import os
import pytest
import allure
from time import sleep

from screens.FeaturerMoviesPage import MoviesPage
from screens.SeatSelectionPage import SeatSelectionPage
from screens.InfoPage import InfoPage
from screens.CheckOutPage import CheckOutPage
from locators.seat_selection_locators import SeatSelectionLocators
from locators.checkout_locators import CheckoutPageLocators
from locators.info_locators import InfoPageLocators
#
#
# @pytest.mark.usefixtures('driver_noCache')
# class TestPerformancePage:
#     def test_seat_selections_are_opened(self, driver):
#         '''Выбор места открыт'''
#         now = datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
#         path = os.getcwd() + f'/screenshots/session_{now}.png'
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.waiting_main()
#         self.movie_page.pass_popup()
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
#         driver.get_screenshot_as_file(path)
#         allure.attach.file(path, attachment_type=allure.attachment_type.PNG)
#         self.seat_selection_page.select_seat(path)
#         self.seat_selection_page.matching_text(*SeatSelectionLocators.continue_btn, pattern='Продолжить')
#         os.remove(path)
#         self.seat_selection_page.click(*SeatSelectionLocators.continue_btn)
#         self.check_out_page = CheckOutPage(driver)
#         self.check_out_page.set_custom_wait(10)
#         self.check_out_page.find_element(*CheckoutPageLocators.total_price)
#         self.check_out_page.matching_text(*CheckoutPageLocators.continue_btn, pattern='Продолжить')
