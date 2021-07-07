from time import sleep

import pytest
import allure

from screens.AuthPage import AuthPage
from screens.MoviesPage import MoviesPage
from screens.SettingsPage import SettingsPage
from locators.common_locators import CommonLocators
from locators.auth_locators import AuthPageLocators
from locators.settings_locators import SettingsPageLocators


@pytest.mark.usefixtures('driver')
class TestSettingsPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.auth_locators = AuthPageLocators()
        cls.settings_locators = SettingsPageLocators()

    def test_001(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            self.settings_page.find_element(*self.settings_locators.back_button)
            self.settings_page.matching_text(*self.settings_locators.title, pattern='Настройки')

    def test_002(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            self.settings_page.click(*self.settings_locators.back_button)
        with allure.step('AuthPage'):
            self.auth_page.find_element(*self.auth_locators.btn_login)

    def test_003(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            self.settings_page.check_settings_list()

    def test_004(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            self.settings_page.check_switch_city('сарат', 'Саратов', 'Москва')
            self.settings_page.check_switch_city('моск', 'Москва', 'Саратов')

    def test_005(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            sleep(1)
            elem_card = driver.find_elements(*self.settings_locators.profile_item_title)[0]
            self.settings_page.click_elem(elem_card)
            self.settings_page.find_element(*self.settings_locators.img_card_empty)
            self.settings_page.click(*self.settings_locators.back_button)
            self.settings_page.check_settings_list()

    def test_006(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            sleep(1)
            elem_card = driver.find_elements(*self.settings_locators.profile_item_title)[1]
            self.settings_page.click_elem(elem_card)
            self.settings_page.find_element(*self.settings_locators.img_card_empty)
            self.settings_page.click(*self.settings_locators.back_button)
            self.settings_page.check_settings_list()

    def test_007(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            sleep(1)
            elem_support = driver.find_elements(*self.settings_locators.profile_item_title)[2]
            self.settings_page.click_elem(elem_support)
            self.settings_page.act.swipe(50, 60, 50, 40)
            self.settings_page.check_techsupport_contacts()

    def test_008(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            sleep(1)
            elem_theme = driver.find_elements(*self.settings_locators.profile_item_title)[7]
            self.settings_page.click_elem(elem_theme)
            self.settings_page.check_text_theme()

    def test_009(self, driver):
        with allure.step('MoviesPage'):
            self.movies_page = MoviesPage(driver)
            self.movies_page.set_custom_wait(20)
            self.movies_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(20)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(20)
            sleep(1)
            elem_theme = driver.find_elements(*self.settings_locators.profile_item_title)[7]
            self.settings_page.click_elem(elem_theme)
            self.settings_page.switch_theme(2)
            sleep(1)
            self.settings_page.check_dark_theme(True)
            self.settings_page.switch_theme(0)
            sleep(1)
            self.settings_page.check_dark_theme(False)
