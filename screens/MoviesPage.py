import random
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from templates.base import Wait
from templates.statistic import RecordTimeout
from templates.action import Action
from .OnboardingPage import OnboardingPage
from locators.movies_locators import MoviesPageLocators
from locators.popup_locators import PopupLocators


class MoviesPage(Page, Wait):
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
            onboarding.set_custom_wait(15)
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

    def select_session(self):
        sessions = self.driver.find_elements(*self.movies_locators.session_date)
        for session in sessions:
            try:
                session.click()
                if self.not_displayed(*self.movies_locators.right_btn):
                    break
            except AssertionError:
                if self.matching_text(*self.movies_locators.title_tv, pattern='Билеты закончились'):
                    self.click(*self.movies_locators.right_btn, text='Понятно')
            except StaleElementReferenceException as error:
                print(f'No available sessions found: {error}')

    def pass_allow_photo_media(self):
        try:
            self.click(*self.popup_locators.permission_allow_btn)
        except AssertionError:
            pass

