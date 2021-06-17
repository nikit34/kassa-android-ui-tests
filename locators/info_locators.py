from selenium.webdriver.common.by import By


class InfoPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.tv_covid_term_btn = (self.ID, 'ru.rambler.kassa:id/tvCovidTerms')
        self.cb_covid_term_btn = (self.ID, 'ru.rambler.kassa:id/cbCovidTerms')
        self.covid_cancel_btn = (self.ID, 'ru.rambler.kassa:id/btnCovidCancel')
        self.covid_next_btn = (self.ID, 'ru.rambler.kassa:id/btnCovidNext')