from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException

from locators.info_locators import InfoPageLocators
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout
from app.check_api import CheckAPI


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

    def recognize_page(self, dbg_api):
        type_page = []
        for line in dbg_api.read_buffer(read_mapi=True):
            if CheckAPI.check_single_page_url('/creations/movie/', line=line, num_after=6):
                content = dbg_api.get_content_response(line)
                try:
                    if content['ageRestriction'] >= 18:
                        type_page.append('ageRestriction')
                except KeyError as error:
                    print('key \"ageRestriction\" is not exist: ', error)
            if CheckAPI.check_single_page_url('/hall/', line=line, num_after=8):
                content = dbg_api.get_content_response(line)
                try:
                    if 'covidNotification' in content:
                        type_page.append('covidNotification')
                except KeyError as error:
                    print('key \"covidNotification\" is not exist: ', error)
                try:
                    if 'infoAbout3DGlasses' in content:
                        type_page.append('infoAbout3DGlasses')
                except KeyError as error:
                    print('key \"infoAbout3DGlasses\" is not exist: ', error)
        return type_page


