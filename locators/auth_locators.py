from selenium.webdriver.common.by import By


class AuthPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.profile_settings_icon = (self.ID, 'ru.rambler.kassa:id/profileSettingIcon')
        self.settings_btn = (self.ID, 'ru.rambler.kassa:id/settingBtn')
        self.login_button = (self.ID, 'ru.rambler.kassa:id/loginBtn')
        self.profile_name = (self.ID, 'ru.rambler.kassa:id/profileName')
