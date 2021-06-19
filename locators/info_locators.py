from selenium.webdriver.common.by import By


class InfoPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.btn_tv_covid_term = (self.ID, 'ru.rambler.kassa:id/tvCovidTerms')
        self.btn_cb_covid_term = (self.ID, 'ru.rambler.kassa:id/cbCovidTerms')
        self.btn_covid_cancel = (self.ID, 'ru.rambler.kassa:id/btnCovidCancel')
        self.btn_covid_next = (self.ID, 'ru.rambler.kassa:id/btnCovidNext')