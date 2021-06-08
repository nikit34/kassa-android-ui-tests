from .action import Action
from .base import Page, Wait
from locators.popup_locators import PopupLocators
from locators.tickets_locators import TicketsPageLocators


class TicketsPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.act = Action(driver)

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def is_ticket_visible(self):
        self.find_element(*TicketsPageLocators.info_btn)
        self.find_element(*TicketsPageLocators.ticket_carousel)

    def check_popup(self):
        self.find_element(*PopupLocators.next_btn)
        self.find_element(*PopupLocators.header)
        self.find_element(*PopupLocators.description)

    def pass_popup(self):
        try:
            self.click(*PopupLocators.next_btn)
        except AssertionError as error:
            error.args = ('popup is not worked')
            pass