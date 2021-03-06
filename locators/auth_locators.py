from selenium.webdriver.common.by import By


class AuthPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.btn_settings = (self.ID, 'ru.rambler.kassa.dev:id/settingBtn')
        self.btn_login = (self.ID, 'ru.rambler.kassa.dev:id/loginBtn')
        self.btn_sber_login = (self.ID, 'ru.rambler.kassa.dev:id/loginSberbankBtn')
        self.text_conditions = (self.ID, 'ru.rambler.kassa.dev:id/tvTermsAndConditionsAgreements')
