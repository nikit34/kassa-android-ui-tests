import pytest
import os
import allure
from time import sleep
from datetime import datetime

from screens.MoviesPage import MoviesPage
from screens.SeatSelectionPage import SeatSelectionPage
from screens.CheckOutPage import CheckOutPage
from screens.InfoPage import InfoPage
from locators.info_locators import InfoPageLocators
from locators.seat_selection_locators import SeatSelectionLocators
from locators.checkout_locators import CheckoutPageLocators


# @pytest.mark.usefixtures('driver')
# class TestPerformancePage:
#     def test_seat_selections_are_opened(self, driver):
#         '''Выбор места открыт'''
#         now = datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
#         path = os.getcwd() + f'/screenshots/session_{now}.png'
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
#         driver.get_screenshot_as_file(path)
#         allure.attach.file(path, attachment_type=allure.attachment_type.PNG)
#         self.seat_selection_page.select_seat(path)
#         os.remove(path)
#         self.seat_selection_page.click(*SeatSelectionLocators.continue_btn)
#         self.check_out_page = CheckOutPage(driver)
#         self.check_out_page.set_custom_wait(10)
#         self.check_out_page.find_element(*CheckoutPageLocators.total_price)
#         self.check_out_page.find_element(*CheckoutPageLocators.continue_btn)
