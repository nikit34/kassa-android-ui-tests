from selenium.webdriver.common.by import By


class ComboPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.btn_continue = (self.ID, '')