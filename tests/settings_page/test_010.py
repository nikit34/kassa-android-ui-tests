import pytest
from screens.AuthPage import AuthPage
from screens.MoviesPage import MoviesPage
from screens.SettingsPage import SettingsPage
from locators.common_locators import CommonLocators
from locators.auth_locators import AuthPageLocators
from locators.settings_locators import SettingsPageLocators


# @pytest.mark.skip(reason="Need login")
# @pytest.mark.usefixtures('driver')
# class TestSettingsPage:
#     @classmethod
#     def setup_class(cls):
#         cls.common_locators = CommonLocators()
#         cls.auth_locators = AuthPageLocators()
#         cls.settings_locators = SettingsPageLocators()
#
#     def test_check_open_settings_page(self, driver):
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*self.common_locators.tab_profile)
#         self.auth_page = AuthPage(driver)
#         self.auth_page.set_custom_wait(10)
#         self.auth_page.click(*self.auth_locators.profile_settings_icon)
#         self.settings_page = SettingsPage(driver)
#         self.settings_page.set_custom_wait(10)
#         self.settings_page.find_element(*self.settings_locators.back_button)
#         self.settings_page.matching_text(*self.settings_locators.title, pattern='Настройки')
#
#     def test_check_open_settings_page_and_return_to_profile(self, driver):
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*self.common_locators.tab_profile)
#         self.auth_page = AuthPage(driver)
#         self.auth_page.set_custom_wait(10)
#         self.auth_page.click(*self.auth_locators.profile_settings_icon)
#         self.settings_page = SettingsPage(driver)
#         self.settings_page.set_custom_wait(10)
#         self.settings_page.click(*self.settings_locators.back_button)
#         # self.auth_page.find_element(*self.auth_locators.profile_name)
#
#     def test_check_open_settings_page_has_all_tags(self, driver):
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*self.common_locators.tab_profile)
#         self.auth_page = AuthPage(driver)
#         self.auth_page.set_custom_wait(10)
#         self.auth_page.click(*self.auth_locators.profile_settings_icon)
#         self.settings_page = SettingsPage(driver)
#         self.settings_page.set_custom_wait(10)
#         self.settings_page.check_settings_list()
#
#     def test_check_open_search_city_page(self, driver):
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*self.common_locators.tab_profile)
#         self.auth_page = AuthPage(driver)
#         self.auth_page.set_custom_wait(10)
#         self.auth_page.click(*self.auth_locators.profile_settings_icon)
#         self.settings_page = SettingsPage(driver)
#         self.settings_page.set_custom_wait(10)
#         self.settings_page.check_switch_city('сарат', 'Саратов', 'Москва')
#         self.settings_page.check_switch_city('моск', 'Москва', 'Саратов')