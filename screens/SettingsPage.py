from .action import Action
from .base import Page, Wait
from locators.settings_locators import SettingsPageLocators


class SettingsPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.act = Action(driver)

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_settings_list(self):
        rows_settings = self.driver.find_elements(*SettingsPageLocators.profile_item_title)
        valid_rows = ['Мои карты', 'Бонусные карты', 'Техподдержка', 'FAQ', 'Геолокация', 'Москва', 'Уведомления', 'Темы', 'О приложении', 'Выход']
        for i, row_templates in enumerate(valid_rows):
            assert rows_settings[i].text == row_templates, f'no comparison: {rows_settings[i].text} - {row_templates}'

    def check_switch_city(self, input_city, valid_city, old_city=None):
        self.click(*SettingsPageLocators.profile_item_title, text=old_city)
        self.input(input_city, *SettingsPageLocators.input)
        cities = self.driver.find_elements(*SettingsPageLocators.city)
        assert valid_city == cities[0].text, f'invalid sent {cities[0]}'
        self.click(*SettingsPageLocators.city)

