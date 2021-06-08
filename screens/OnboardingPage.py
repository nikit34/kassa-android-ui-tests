from .base import Page, Wait
from locators.onboarding_locators import OnboardingPageLocators


class OnboardingPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def skip_onboarding(self):
        self.click(*OnboardingPageLocators.go_button)
        self.click(*OnboardingPageLocators.select_city_button)
        self.click(*OnboardingPageLocators.city)

    def check_city_list(self):
        cities = self.driver.find_elements(*OnboardingPageLocators.city)
        if not cities:
            self.input('моск', *OnboardingPageLocators.input_field)
        assert cities[0].text == 'Москва', f'{cities[0].text} is not relevant result of search'

