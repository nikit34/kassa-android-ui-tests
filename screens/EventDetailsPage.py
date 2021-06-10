from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout
from locators.popup_locators import PopupLocators


class EventsDetailsPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.popup_locators = PopupLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

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

    def pass_allow_photo_media(self):
        try:
            self.click(*self.popup_locators.permission_allow_btn)
        except AssertionError:
            pass
