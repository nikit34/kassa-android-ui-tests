import pytest

from screens.MoviesPage import MoviesPage
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators


@pytest.mark.usefixtures('driver_noCache')
class TestOnboardingPage:
    @classmethod
    def setup_class(cls):
        cls.onboarding_locators = OnboardingPageLocators()

    def test_onboarding_is_enabled(self, driver):
        self.onboarding_page = OnboardingPage(driver)
        self.onboarding_page.set_custom_wait(15)
        self.onboarding_page.find_element(*self.onboarding_locators.go_button)
        self.onboarding_page.find_element(*self.onboarding_locators.page_title)
        self.onboarding_page.find_element(*self.onboarding_locators.page_label)

    def test_city_selection_is_enabled(self, driver):
        self.onboarding_page = OnboardingPage(driver)
        self.onboarding_page.set_custom_wait(15)
        self.onboarding_page.click(*self.onboarding_locators.go_button)
        self.onboarding_page.click(*self.onboarding_locators.select_city_button)
        self.onboarding_page.find_element(*self.onboarding_locators.search_field)
        self.onboarding_page.find_element(*self.onboarding_locators.input_field)
        self.onboarding_page.find_element(*self.onboarding_locators.back_button)

    def test_select_city_is_working(self, driver):
        self.onboarding_page = OnboardingPage(driver)
        self.onboarding_page.set_custom_wait(15)
        self.onboarding_page.click(*self.onboarding_locators.go_button)
        self.onboarding_page.click(*self.onboarding_locators.select_city_button)
        self.onboarding_page.click(*self.onboarding_locators.search_field)
        self.onboarding_page.check_city_list()
        self.onboarding_page.click(*self.onboarding_locators.city)

    def test_back_button_is_working(self, driver):
        self.onboarding_page = OnboardingPage(driver)
        self.onboarding_page.set_custom_wait(15)
        self.onboarding_page.click(*self.onboarding_locators.go_button)
        self.onboarding_page.click(*self.onboarding_locators.select_city_button)
        self.onboarding_page.find_element(*self.onboarding_locators.input_field)
        self.onboarding_page.click(*self.onboarding_locators.back_button)
        self.onboarding_page.find_element(*self.onboarding_locators.select_city_button)
        self.onboarding_page.find_element(*self.onboarding_locators.allow_location_button)

    def test_geo_popup_is_come(self, driver):
        self.onboarding_page = OnboardingPage(driver)
        self.onboarding_page.set_custom_wait(15)
        self.onboarding_page.click(*self.onboarding_locators.go_button)
        self.onboarding_page.click(*self.onboarding_locators.allow_location_button)
        self.onboarding_page.find_element(*self.onboarding_locators.pemission_message)
        self.onboarding_page.click(*self.onboarding_locators.permission_allow_button)

    def test_geo_popup_is_com(self, driver):
        self.onboarding_page = OnboardingPage(driver)
        self.onboarding_page.set_custom_wait(15)
        self.onboarding_page.skip_onboarding()
        self.movies_page = MoviesPage(driver)
        self.movies_page.set_custom_wait(15)
        self.movies_page.check_popup()
        self.movies_page.pass_popup()