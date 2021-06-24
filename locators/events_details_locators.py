from selenium.webdriver.common.by import By


class EventsDetailsPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.back_button = (self.ID, 'ru.rambler.kassa.dev:id/leftIcon')
        self.like_button = (self.ID, 'ru.rambler.kassa.dev:id/favoriteBtn')
        self.title = (self.ID, 'ru.rambler.kassa.dev:id/title')
        self.description = (self.ID, 'ru.rambler.kassa.dev:id/description')
        self.btn_shedule_ticket = (self.ID, 'ru.rambler.kassa.dev:id/buyTicketBtn')
