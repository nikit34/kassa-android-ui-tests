from selenium.webdriver.common.by import By


class AuthPageLocators:
    profile_settings_icon = (By.ID, 'ru.rambler.kassa.beta:id/profileSettingIcon')
    settings_btn = (By.ID, 'ru.rambler.kassa.beta:id/settingBtn')
    login_button = (By.ID, 'ru.rambler.kassa.beta:id/loginBtn')
    profile_name = (By.ID, 'ru.rambler.kassa.beta:id/profileName')
