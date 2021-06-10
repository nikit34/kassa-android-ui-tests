from templates.base import Wait
from templates.statistic import RecordTimeout
from templates.action import Action

class InfoPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

