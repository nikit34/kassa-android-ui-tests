from locators.popup_locators import PopupLocators
from locators.tickets_locators import TicketsPageLocators
from templates.base import Wait
from templates.statistic import RecordTimeout


class TicketsPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.popup_locators = PopupLocators()
        self.tickets_locators = TicketsPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def is_ticket_visible(self):
        self.find_element(*self.tickets_locators.info_btn)
        self.find_element(*self.tickets_locators.ticket_carousel)

    def check_popup(self):
        self.find_element(*self.popup_locators.next_btn)
        self.find_element(*self.popup_locators.header)
        self.find_element(*self.popup_locators.description)

    def pass_popup(self):
        try:
            self.click(*self.popup_locators.next_btn)
        except AssertionError as error:
            error.args = ('popup is not worked')
            pass