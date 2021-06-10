import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.AuthPage import AuthPage
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators
from locators.common_locators import CommonLocators
from locators.auth_locators import AuthPageLocators


@allure.feature('noCache')
@pytest.mark.usefixtures('driver_noCache')
class TestAuthPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.auth_locators = AuthPageLocators()
        cls.onboarding_locators = OnboardingPageLocators()

    def test_001_auth_onboard_page_is_opened(self, driver):
        with allure.step("OnboardingPage"):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(20)
        with allure.step("MoviesPage"):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(15)
            self.movie_page.waiting_main()
            self.movie_page.pass_popup()
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step("AuthPage"):
            self.auth_page = AuthPage(driver)
            self.auth_page.pass_popup()
            self.auth_page.find_element(*self.auth_locators.settings_btn)
            self.auth_page.find_element(*self.auth_locators.login_button)
