from selenium.webdriver.common.by import By


class PopupLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.header = (self.ID, 'ru.rambler.kassa.beta:id/headerTv')
        self.next_btn = (self.ID, 'ru.rambler.kassa.beta:id/nextBtn')
        self.description = (self.ID, 'ru.rambler.kassa.beta:id/descriptionTv')
        self.permission_msg = (self.ID, 'com.android.permissioncontroller:id/permission_message')
        self.permission_allow_btn = (self.ID, 'com.android.permissioncontroller:id/permission_allow_button')
        self.permission_deny_btn = (self.ID, 'com.android.permissioncontroller:id/permission_deny_button')
        self.permission_deny_dont_ask = (self.ID, 'com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button')