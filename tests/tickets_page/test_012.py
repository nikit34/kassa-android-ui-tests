import pytest
from locators.tickets_locators import TicketsPageLocators
from screens.MoviesPage import MoviesPage
from screens.TicketsPage import TicketsPage
from locators.common_locators import CommonLocators


@pytest.mark.usefixtures('driver')
class TestTicketsPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.tickets_locators = TicketsPageLocators()

    def test_tickets_tab_are_opened(self, driver):
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(20)
        self.movies_page.click(*self.common_locators.tab_ticket)
        self.tickets_page = TicketsPage(driver)
        self.tickets_page.set_custom_wait(20)
        self.tickets_page.pass_popup()
        self.tickets_page.matching_text(*self.tickets_locators.return_btn, pattern='На главную')
