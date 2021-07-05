import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators

#
# @pytest.mark.usefixtures('driver_noCache')
# class TestOnboardingPage:
#     @classmethod
#     def setup_class(cls):
#         cls.onboarding_locators = OnboardingPageLocators()
#
#     def test_001(self, driver):
#         with allure.step('OnboardingPage'):
#             self.onboarding_page = OnboardingPage(driver)
#             self.onboarding_page.set_custom_wait(20)
#             self.onboarding_page.find_element(*self.onboarding_locators.go_button)
#             self.onboarding_page.find_element(*self.onboarding_locators.page_title)
#             self.onboarding_page.find_element(*self.onboarding_locators.page_label)
#
#     def test_002(self, driver):
#         with allure.step('OnboardingPage'):
#             self.onboarding_page = OnboardingPage(driver)
#             self.onboarding_page.set_custom_wait(20)
#             self.onboarding_page.click(*self.onboarding_locators.go_button)
#             self.onboarding_page.click(*self.onboarding_locators.select_city_button)
#             self.onboarding_page.find_element(*self.onboarding_locators.search_field)
#             self.onboarding_page.find_element(*self.onboarding_locators.input_field)
#             self.onboarding_page.find_element(*self.onboarding_locators.back_button)
#
#     def test_003(self, driver):
#         with allure.step('OnboardingPage'):
#             self.onboarding_page = OnboardingPage(driver)
#             self.onboarding_page.set_custom_wait(20)
#             self.onboarding_page.click(*self.onboarding_locators.go_button)
#             self.onboarding_page.click(*self.onboarding_locators.select_city_button)
#             self.onboarding_page.click(*self.onboarding_locators.search_field)
#             self.onboarding_page.check_city_list()
#             self.onboarding_page.click(*self.onboarding_locators.city)
#
#     def test_004(self, driver):
#         with allure.step('OnboardingPage'):
#             self.onboarding_page = OnboardingPage(driver)
#             self.onboarding_page.set_custom_wait(20)
#             self.onboarding_page.click(*self.onboarding_locators.go_button)
#             self.onboarding_page.click(*self.onboarding_locators.select_city_button)
#             self.onboarding_page.find_element(*self.onboarding_locators.input_field)
#             self.onboarding_page.click(*self.onboarding_locators.back_button)
#             self.onboarding_page.find_element(*self.onboarding_locators.select_city_button)
#             self.onboarding_page.find_element(*self.onboarding_locators.allow_location_button)
#
#     def test_005(self, driver):
#         with allure.step('OnboardingPage'):
#             self.onboarding_page = OnboardingPage(driver)
#             self.onboarding_page.set_custom_wait(20)
#             self.onboarding_page.click(*self.onboarding_locators.go_button)
#             self.onboarding_page.click(*self.onboarding_locators.allow_location_button)
#             self.onboarding_page.find_element(*self.onboarding_locators.pemission_message)
#             self.onboarding_page.click(*self.onboarding_locators.permission_allow_button)
#
#     def test_006(self, driver):
#         with allure.step('OnboardingPage'):
#             self.onboarding_page = OnboardingPage(driver)
#             self.onboarding_page.set_custom_wait(20)
#             self.onboarding_page.skip_onboarding()
#         with allure.step('MoviesPage'):
#             self.movies_page = MoviesPage(driver)
#             self.movies_page.set_custom_wait(20)
#             self.movies_page.check_popup()
#             self.movies_page.pass_popup()