import random
from time import sleep

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException

from templates.base import Wait
from templates.error import base_error
from templates.statistic import RecordTimeout
from templates.action import Action
from .OnboardingPage import OnboardingPage
from locators.movies_locators import MoviesPageLocators
from locators.popup_locators import PopupLocators


class MoviesPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.movies_locators = MoviesPageLocators()
        self.popup_locators = PopupLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def waiting_main(self):
        try:
            onboarding = OnboardingPage(self.driver)
            onboarding.set_custom_wait(20)
            onboarding.skip_onboarding()
        except TimeoutException as error:
            error.args += ('Page has not open', )
            raise

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

    def click_random(self, *locator, border=2):
        rand_index = random.randint(0, border)
        elements = self.driver.find_elements(*locator[:2])
        elements[rand_index].click()

    def select_session(self, _number_session=0, _number_slide=0):
        sleep(10)
        for i in range(_number_slide):
            sleep(3)
            self.act.swipe(80, 30, 20, 30)
        locator = self.movies_locators.session_date
        sessions = self.driver.find_elements(*locator)
        len_sessions = len(sessions)
        if len_sessions == 0 or len_sessions < _number_session:
            raise base_error(self.driver, ValueError, *locator, crash_site='click_elem', msg='No session buttons found')
        self.click_elem(sessions[_number_session])

    def pass_allow_photo_media(self):
        try:
            self.click(*self.popup_locators.permission_allow_btn)
        except AssertionError:
            pass

    def click_tab(self, num):
        tabs_elem = self.driver.find_elements(*self.movies_locators.tab)
        len_tabs_elem = len(tabs_elem)
        if num < len_tabs_elem:
            self.click_elem(tabs_elem[num])
        else:
            raise IndexError(f'[ERROR] num: {num} beyond limit of number of elements count: {len_tabs_elem}')