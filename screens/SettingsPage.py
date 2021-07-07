from locators.settings_locators import SettingsPageLocators
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout
from utils.factory_screenshots import Screenshot


class SettingsPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.settings_locators = SettingsPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_settings_list(self):
        rows_settings = self.driver.find_elements(*self.settings_locators.profile_item_title)
        valid_rows = ['Мои карты', 'Бонусные карты', 'Техподдержка', 'FAQ', 'Геолокация', 'Москва', 'Уведомления', 'Темы', 'О приложении']
        for i, row_templates in enumerate(valid_rows):
            assert rows_settings[i].text == row_templates, f'no comparison: {rows_settings[i].text} - {row_templates}'

    def check_switch_city(self, input_city, valid_city, old_city=None):
        elem_city = self.driver.find_elements(*self.settings_locators.profile_item_title)[5]
        assert elem_city.text == old_city, f'[ERROR] invalid city: {elem_city.text} != {old_city}'
        self.click_elem(elem_city)
        self.input(input_city, *self.settings_locators.input)
        cities = self.find_element(*self.settings_locators.city)
        assert valid_city == cities.text, f'[ERROR] invalid city: {cities}'
        self.click(*self.settings_locators.city)
        elem_city = self.driver.find_elements(*self.settings_locators.profile_item_title)[5]
        assert elem_city.text == valid_city, f'[ERROR] invalid city: {elem_city.text} != {old_city}'

    def check_techsupport_contacts(self):
        elem_contacts = self.driver.find_elements(*self.settings_locators.text_support_contacts)
        valid_rows = ['8 (800) 505 67 91', 'kassa@rambler-co.ru', 'Instagram', 'Facebook', 'Vk', 'Twitter', 'm.kassa@rambler-co.ru']
        for i, row_templates in enumerate(valid_rows):
            assert elem_contacts[i].text == row_templates, f'no comparison: {elem_contacts[i].text} - {row_templates}'

    def check_text_theme(self):
        elem_switchers = self.driver.find_elements(*self.settings_locators.rows_text_theme_switcher)
        assert elem_switchers[0].text == 'Системная тема ON', f'[ERROR] text system theme is not valid'
        assert elem_switchers[1].text == 'Светлая тема OFF', f'[ERROR] text light theme is not valid'
        assert elem_switchers[2].text == 'Тёмная тема OFF', f'[ERROR] text dark theme is not valid'

    def switch_theme(self, num_mode_theme):
        if num_mode_theme > 2:
            raise ValueError('Application has only three modes')
        elem_switchers = self.driver.find_elements(*self.settings_locators.rows_text_theme_switcher)
        self.click_elem(elem_switchers[num_mode_theme])

    def check_dark_theme(self, dark):
        screenshot = Screenshot(self.driver)
        pixs = Screenshot.convert_img_pixels(screenshot.path)
        if dark:
            if pixs.sum() > 250000000:
                raise AssertionError('[FAILED] light theme app')
        else:
            if pixs.sum() < 1500000000:
                raise AssertionError('[FAILED] dark theme app')