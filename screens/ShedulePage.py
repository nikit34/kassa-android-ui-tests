from .action import Action
from .base import Page, Wait
from locators.popup_locators import PopupLocators


class ShedulePage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.act = Action(driver)

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def pass_allow_photo_media(self):
        try:
            self.click(*PopupLocators.permission_allow_btn)
        except AssertionError:
            pass

