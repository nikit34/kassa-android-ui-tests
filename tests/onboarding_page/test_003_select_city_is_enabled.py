import pytest
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators



# @pytest.mark.usefixtures('driver_noCache')
# class TestOnboardingPage:
#     def test_city_selection_is_enabled(self, driver):
#         '''Экран с выбором города появился'''
#         self.onboarding_page = OnboardingPage(driver)
#         self.onboarding_page.set_custom_wait(15)
#         self.onboarding_page.click(*OnboardingPageLocators.go_button, text='Поехали')
#         self.onboarding_page.click(*OnboardingPageLocators.select_city_button, text='Выбрать город')
#         self.onboarding_page.find_element(*OnboardingPageLocators.search_field)
#         self.onboarding_page.find_element(*OnboardingPageLocators.input_field)
#         self.onboarding_page.find_element(*OnboardingPageLocators.back_button)
