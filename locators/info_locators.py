from selenium.webdriver.common.by import By


class InfoPageLocators:
    tv_covid_term_btn = (By.ID, 'ru.rambler.kassa.beta:id/tvCovidTerms')
    cb_covid_term_btn = (By.ID, 'ru.rambler.kassa.beta:id/cbCovidTerms')
    covid_cancel_btn = (By.ID, 'ru.rambler.kassa.beta:id/btnCovidCancel')
    covid_next_btn = (By.ID, 'ru.rambler.kassa.beta:id/btnCovidNext')