from selenium.webdriver.common.by import By


class AuthPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.profile_settings_icon = (self.ID, 'ru.rambler.kassa.beta:id/profileSettingIcon')
        self.settings_btn = (self.ID, 'ru.rambler.kassa.beta:id/settingBtn')
        self.login_button = (self.ID, 'ru.rambler.kassa.beta:id/loginBtn')
        self.profile_name = (self.ID, 'ru.rambler.kassa.beta:id/profileName')
