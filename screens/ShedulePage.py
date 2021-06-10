from locators.popup_locators import PopupLocators
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class ShedulePage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.popup_locators = PopupLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def pass_allow_photo_media(self):
        try:
            self.click(*self.popup_locators.permission_allow_btn)
        except AssertionError:
            pass

