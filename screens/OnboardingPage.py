from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout
from locators.onboarding_locators import OnboardingPageLocators


class OnboardingPage(RecordTimeout, Wait):
    def __init__(self, driver, city='Абдулино'):
        super().__init__(driver)

        self.repeat = '0'
        self.extra_interval = 50
        self.city = city

        self.act = Action(driver)

        self.onboarding_page_locators = OnboardingPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def skip_onboarding(self):
        self.click(*self.onboarding_page_locators.go_button)
        self.click(*self.onboarding_page_locators.select_city_button)
        self.click(*self.onboarding_page_locators.city)

    def check_city_list(self):
        cities = self.driver.find_elements(*self.onboarding_page_locators.city)
        if not cities:
            self.input('моск', *self.onboarding_page_locators.input_field)
        assert cities[0].text == 'Москва', f'{cities[0].text} is not relevant result of search'

