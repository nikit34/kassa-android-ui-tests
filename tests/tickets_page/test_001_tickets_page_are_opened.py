import pytest
from locators.tickets_locators import TicketsPageLocators
from screens.FeaturerMoviesPage import MoviesPage
from screens.TicketsPage import TicketsPage
from locators.common_locators import CommonLocators


# @pytest.mark.usefixtures('driver')
# class TestTicketsPage:
#     def test_tickets_tab_are_opened(self, driver):
#         '''Открыта вкладка Билеты'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*CommonLocators.tab_ticket)
#         self.tickets_page = TicketsPage(driver)
#         self.tickets_page.set_custom_wait(10)
#         self.tickets_page.pass_popup()
#         self.tickets_page.matching_text(*TicketsPageLocators.return_btn, pattern='На главную')
