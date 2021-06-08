import random
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from .base import Page, Wait
from .action import Action
from .OnboardingPage import OnboardingPage
from locators.featurer_movies_locators import MoviesPageLocators
from locators.popup_locators import PopupLocators


class MoviesPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.act = Action(driver)

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
        self.find_element(*PopupLocators.next_btn)
        self.find_element(*PopupLocators.header)
        self.find_element(*PopupLocators.description)

    def pass_popup(self):
        try:
            self.click(*PopupLocators.next_btn)
        except AssertionError as error:
            error.args = ('popup is not worked')
            pass

    def click_random(self, *locator, border=2):
        rand_index = random.randint(0, border)
        elements = self.driver.find_elements(*locator[:2])
        elements[rand_index].click()

    def select_session(self):
        sessions = self.driver.find_elements(*MoviesPageLocators.session_date)
        for session in sessions:
            try:
                session.click()
                if self.not_displayed(*MoviesPageLocators.right_btn):
                    break
            except AssertionError:
                if self.matching_text(*MoviesPageLocators.title_tv, pattern='Билеты закончились'):
                    self.click(*MoviesPageLocators.right_btn, text='Понятно')
            except StaleElementReferenceException as error:
                print(f'No available sessions found: {error}')

    def pass_allow_photo_media(self):
        try:
            self.click(*PopupLocators.permission_allow_btn)
        except AssertionError:
            pass

