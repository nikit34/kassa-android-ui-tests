from selenium.webdriver.common.by import By


class SettingsPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.back_button = (self.ID, 'ru.rambler.kassa:id/leftIconContainer')
        self.title = (self.ID, 'ru.rambler.kassa:id/titleTextView')
        self.profile_item_title = (self.ID, 'ru.rambler.kassa:id/profileItemTitle')
        self.search = (self.ID, 'ru.rambler.kassa:id/search')
        self.input = (self.ID, 'ru.rambler.kassa:id/input')
        self.list_of_cities = (self.ID, 'ru.rambler.kassa:id/citiesRv')
        self.city = (self.ID, 'ru.rambler.kassa:id/cityTitle')



