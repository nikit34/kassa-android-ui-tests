import pytest
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators



# @pytest.mark.usefixtures('driver_noCache')
# class TestOnboardingPage:
#     def test_geo_popup_is_come(self, driver):
#         '''Разрешаем геолокацию'''
#         self.onboarding_page = OnboardingPage(driver)
#         self.onboarding_page.set_custom_wait(15)
#         self.onboarding_page.click(*OnboardingPageLocators.go_button, text='Поехали')
#         self.onboarding_page.click(*OnboardingPageLocators.allow_location_button, text='Разрешить геолокацию')
#         self.onboarding_page.find_element(*OnboardingPageLocators.pemission_message)
#         self.onboarding_page.click(*OnboardingPageLocators.permission_allow_button)