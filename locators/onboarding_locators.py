from selenium.webdriver.common.by import By


class OnboardingPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.page_title = (self.ID, 'ru.rambler.kassa.dev:id/onboardPageTitle')
        self.page_label = (self.ID, 'ru.rambler.kassa.dev:id/onboardPageLabel')
        self.go_button = (self.ID, 'ru.rambler.kassa.dev:id/onboardingGo')
        self.select_city_button = (self.ID, 'ru.rambler.kassa.dev:id/selectCityBtn')
        self.allow_location_button = (self.ID, 'ru.rambler.kassa.dev:id/allowLocationBtn')
        self.pemission_message = (self.ID, 'com.android.permissioncontroller:id/permission_message')
        self.permission_allow_button = (self.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        self.search_field = (self.ID, 'ru.rambler.kassa.dev:id/search')
        self.back_button = (self.ID, 'ru.rambler.kassa.dev:id/iconLeftContainer')
        self.input_field = (self.ID, 'ru.rambler.kassa.dev:id/input')
        self.city = (self.ID, 'ru.rambler.kassa.dev:id/cityTitle')
