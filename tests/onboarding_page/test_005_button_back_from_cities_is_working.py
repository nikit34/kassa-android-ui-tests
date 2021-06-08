import pytest

from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators


# @pytest.mark.usefixtures('driver_noCache')
# class TestOnboardingPage:
#     def test_back_button_is_working(self, driver):
#         '''Кнопка назад работ на экране выбора города'''
#         self.onboarding_page = OnboardingPage(driver)
#         self.onboarding_page.set_custom_wait(15)
#         self.onboarding_page.click(*OnboardingPageLocators.go_button, text='Поехали')
#         self.onboarding_page.click(*OnboardingPageLocators.select_city_button, text='Выбрать город')
#         self.onboarding_page.find_element(*OnboardingPageLocators.input_field)
#         self.onboarding_page.click(*OnboardingPageLocators.back_button)
#         self.onboarding_page.find_element(*OnboardingPageLocators.select_city_button)
#         self.onboarding_page.find_element(*OnboardingPageLocators.allow_location_button)