import pytest
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators


#
# @pytest.mark.usefixtures('driver_noCache')
# class TestOnboardingPage:
#     def test_select_city_is_working(self, driver):
#         '''Успешно прошел онбординг'''
#         self.onboarding_page = OnboardingPage(driver)
#         self.onboarding_page.set_custom_wait(15)
#         self.onboarding_page.click(*OnboardingPageLocators.go_button, text='Поехали')
#         self.onboarding_page.click(*OnboardingPageLocators.select_city_button, text='Выбрать город')
#         self.onboarding_page.click(*OnboardingPageLocators.search_field)
#         self.onboarding_page.check_city_list()
#         self.onboarding_page.click(*OnboardingPageLocators.city)
