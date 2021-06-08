import pytest

from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators

#
# @pytest.mark.usefixtures('driver_noCache')
# class TestOnboardingPage:
#     def test_onboarding_is_enabled(self, driver):
#         '''Онбординг появился'''
#         self.onboarding_page = OnboardingPage(driver)
#         self.onboarding_page.set_custom_wait(15)
#         self.onboarding_page.find_element(*OnboardingPageLocators.go_button)
#         self.onboarding_page.find_element(*OnboardingPageLocators.page_title)
#         self.onboarding_page.find_element(*OnboardingPageLocators.page_label)