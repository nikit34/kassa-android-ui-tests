from selenium.webdriver.common.by import By


class OnboardingPageLocators:
    page_title = (By.ID, 'ru.rambler.kassa.beta:id/onboardPageTitle')
    page_label = (By.ID, 'ru.rambler.kassa.beta:id/onboardPageLabel')
    go_button = (By.ID, 'ru.rambler.kassa.beta:id/onboardingGo')
    select_city_button = (By.ID, 'ru.rambler.kassa.beta:id/selectCityBtn')
    allow_location_button = (By.ID, 'ru.rambler.kassa.beta:id/allowLocationBtn')
    pemission_message = (By.ID, 'com.android.permissioncontroller:id/permission_message')
    permission_allow_button = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    search_field = (By.ID, 'ru.rambler.kassa.beta:id/search')
    back_button = (By.ID, 'ru.rambler.kassa.beta:id/iconLeftContainer')
    input_field = (By.ID, 'ru.rambler.kassa.beta:id/input')
    city = (By.ID, 'ru.rambler.kassa.beta:id/cityTitle')
