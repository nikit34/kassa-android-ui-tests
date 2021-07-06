import random
from time import sleep
from random import randrange
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from templates.base import Wait
from templates.error import base_error
from templates.statistic import RecordTimeout
from templates.action import Action
from .OnboardingPage import OnboardingPage
from locators.movies_locators import MoviesPageLocators
from locators.popup_locators import PopupLocators
from locators.nointernet_locators import NoInternetPageLocators
from locators.info_locators import InfoPageLocators


class MoviesPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.movies_locators = MoviesPageLocators()
        self.popup_locators = PopupLocators()
        self.info_locators = InfoPageLocators()
        self.nointernet_locators = NoInternetPageLocators()

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
            base_error(self.driver, *locator, crash_site='click_elem', msg='No session buttons found')
        self.click_elem(sessions[_number_session])
        if not self.not_displayed(*self.info_locators.btn_tickets_ended):
            self.click(*self.info_locators.btn_tickets_ended)
            if len(sessions) <= _number_session + 1:
                self.select_session(_number_session=0, _number_slide=_number_slide+1)
            else:
                self.select_session(_number_session=_number_session+1, _number_slide=_number_slide)

    def pass_connection_popup(self):
        last_timeout = self.get_last_wait()
        self.set_custom_wait(5)
        try:
            self.click(*self.nointernet_locators.btn_reload)
        except NoSuchElementException:
            pass
        self.set_custom_wait(last_timeout)

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

    def check_carousel(self):
        movie_base_canvas = self.find_element(*self.movies_locators.carousel_rv)
        movie_base_canvas_row = self.find_element(*self.movies_locators.list_session_view)

        random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
        while True:
            current_check = random_num % 4

            if current_check == 0:
                movie_base_canvas.find_element(*self.movies_locators.event_name)
            elif current_check == 1:
                movie_base_canvas.find_element(*self.movies_locators.place_label)
            elif current_check == 2:
                movie_base_canvas_row.find_element(*self.movies_locators.session_date)
            elif current_check == 3:
                movie_base_canvas_row.find_element(*self.movies_locators.session_price)

            random_num //= 4
            if random_num == 0:
                break
            self.act.swipe(80, 30, 20, 30)
