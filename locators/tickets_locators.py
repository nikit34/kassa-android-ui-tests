from selenium.webdriver.common.by import By


class TicketsPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.title = (self.ID, 'ru.rambler.kassa.dev:id/TextView')
        self.ticket_carousel = (self.ID, 'ru.rambler.kassa.dev:id/myTicketsRv')
        self.info_btn = (self.ID, 'ru.rambler.kassa.dev:id/moreInfo')
        self.return_btn = (self.ID, 'ru.rambler.kassa.dev:id/myTicketsBtn')