import pytest
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators



# @pytest.mark.usefixtures('driver_noCache')
# class TestOnboardingPage:
#     def test_onboarding_choice_is_enabled(self, driver):
#         '''Экран с разрешением геолокации появился'''
#         self.onboarding_page = OnboardingPage(driver)
#         self.onboarding_page.set_custom_wait(15)
#         self.onboarding_page.click(*OnboardingPageLocators.go_button, text='Поехали')
#         self.onboarding_page.click(*OnboardingPageLocators.allow_location_button, text='Разрешить геолокацию')