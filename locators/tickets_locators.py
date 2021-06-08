from selenium.webdriver.common.by import By


class TicketsPageLocators:
    title = (By.ID, 'ru.rambler.kassa.beta:id/TextView')
    ticket_carousel = (By.ID, 'ru.rambler.kassa.beta:id/myTicketsRv')
    info_btn = (By.ID, 'ru.rambler.kassa.beta:id/moreInfo')
    return_btn = (By.ID, 'ru.rambler.kassa.beta:id/myTicketsBtn')