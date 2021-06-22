from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class FeedPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)