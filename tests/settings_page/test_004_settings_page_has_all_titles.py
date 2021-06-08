import pytest
from screens.AuthPage import AuthPage
from screens.FeaturerMoviesPage import MoviesPage
from screens.SettingsPage import SettingsPage
from locators.common_locators import CommonLocators
from locators.auth_locators import AuthPageLocators


# @pytest.mark.skip(reason="Need login")
# @pytest.mark.usefixtures('driver')
# class TestSettingsPage:
#     def test_check_open_settings_page_has_all_tags(self, driver):
#         '''На странице настроек указаны все пункты'''
#         self.movie_page = MoviesPage(driver)
#         self.movie_page.set_custom_wait(15)
#         self.movie_page.click(*CommonLocators.tab_profile)
#         self.auth_page = AuthPage(driver)
#         self.auth_page.set_custom_wait(10)
#         self.auth_page.click(*AuthPageLocators.profile_settings_icon)
#         self.settings_page = SettingsPage(driver)
#         self.settings_page.set_custom_wait(10)
#         self.settings_page.check_settings_list()
