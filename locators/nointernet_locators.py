from selenium.webdriver.common.by import By


class NoInternetPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.img_reload = (self.ID, 'ru.rambler.kassa:id/emptyImage')
        self.btn_reload = (self.ID, 'ru.rambler.kassa:id/emptyBtn')