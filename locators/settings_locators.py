from selenium.webdriver.common.by import By


class SettingsPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.back_button = (self.ID, 'ru.rambler.kassa.dev:id/leftIconContainer')
        self.title = (self.ID, 'ru.rambler.kassa.dev:id/titleTextView')
        self.profile_item_title = (self.ID, 'ru.rambler.kassa.dev:id/profileItemTitle')
        self.search = (self.ID, 'ru.rambler.kassa.dev:id/search')
        self.input = (self.ID, 'ru.rambler.kassa.dev:id/input')
        self.list_of_cities = (self.ID, 'ru.rambler.kassa.dev:id/citiesRv')
        self.city = (self.ID, 'ru.rambler.kassa.dev:id/cityTitle')
        self.img_card_empty = (self.ID, 'ru.rambler.kassa.dev:id/itemCardImage')
        self.text_support_contacts = (self.ID, 'ru.rambler.kassa.dev:id/profileItemTitle')
        self.rows_text_theme_switcher = (self.ID, 'ru.rambler.kassa.dev:id/themeSwitch')