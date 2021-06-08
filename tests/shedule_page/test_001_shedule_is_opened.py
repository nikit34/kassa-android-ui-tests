import pytest
from screens.FeaturerMoviesPage import MoviesPage
from screens.ShedulePage import ShedulePage
from locators.shedule_locators import ShedulePageLocators
from locators.featurer_movies_locators import MoviesPageLocators


# @pytest.mark.usefixtures('driver')
# class TestShedulePage:
#     def test_shedule_page_is_opened(self, driver):
#         '''Кнопка быстрой покупки открывает экран расписания'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*MoviesPageLocators.fastbuy_ticket_id)
#         self.shedule_page = ShedulePage(driver)
#         self.shedule_page.set_custom_wait(10)
#         self.shedule_page.pass_allow_photo_media()
#         self.shedule_page.find_element(*ShedulePageLocators.event_name)
#         self.shedule_page.find_element(*ShedulePageLocators.back_bar_button)
#         self.shedule_page.find_element(*ShedulePageLocators.map_button)
#         self.shedule_page.find_element(*ShedulePageLocators.sheduler_place_name)
#         self.shedule_page.find_element(*ShedulePageLocators.sheduler_place_address)
#         self.shedule_page.find_element(*ShedulePageLocators.sheduler_geo_location_button)
