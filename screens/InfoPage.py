from .base import Page, Wait
from .action import Action


class InfoPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()

        self.act = Action(driver)

