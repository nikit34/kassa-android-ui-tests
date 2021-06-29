from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException
import json

from locators.info_locators import InfoPageLocators
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class InfoPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.act = Action(driver)

        self.info_locators = InfoPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def pass_without_info(self):
        try:
            self.click(*self.info_locators.btn_cb_covid_term)
            self.act.swipe(50, 60, 50, 40)
            self.click(*self.info_locators.btn_covid_next)
        except (NoSuchElementException, InvalidArgumentException):
            try:
                self.click(*self.info_locators.btn_covid_next)
            except (NoSuchElementException, InvalidArgumentException):
                pass
            pass

    def recognize_next_page(self, dbg_api):
        for line in dbg_api.read_buffer(read_mapi=True):
             if '/creations/movie/' in line:
                 split_line = line.split(';')
                 if len(split_line) != 5:
                     raise ValueError('response is not valid')
                 content = json.loads(split_line[4])
                 print(content)

