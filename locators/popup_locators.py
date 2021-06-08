from selenium.webdriver.common.by import By


class PopupLocators:
    header = (By.ID, 'ru.rambler.kassa.beta:id/headerTv')
    next_btn = (By.ID, 'ru.rambler.kassa.beta:id/nextBtn')
    description = (By.ID, 'ru.rambler.kassa.beta:id/descriptionTv')

    permission_msg = (By.ID, 'com.android.permissioncontroller:id/permission_message')
    permission_allow_btn = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')
    permission_deny_btn = (By.ID, 'com.android.permissioncontroller:id/permission_deny_button')
    permission_deny_dont_ask = (By.ID, 'com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button')