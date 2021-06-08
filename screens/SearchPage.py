from .action import Action
from .base import Page, Wait


class SearchPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.act = Action(driver)

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)


