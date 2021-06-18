from locators.concerts_locators import ConcertsPageLocators

from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class ConcertsPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.concerts_locators = ConcertsPageLocators()