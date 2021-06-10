from selenium.webdriver.common.by import By


class EventsDetailsPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.back_button = (self.ID, 'ru.rambler.kassa.beta:id/leftIcon')
        self.like_button = (self.ID, 'ru.rambler.kassa.beta:id/favoriteBtn')
        self.title = (self.ID, 'ru.rambler.kassa.beta:id/title')
        self.description = (self.ID, 'ru.rambler.kassa.beta:id/description')
        self.event_trailer = (self.ID, 'ru.rambler.kassa.beta:id/eventTrailerPv')
        self.event_cover = (self.ID, 'ru.rambler.kassa.beta:id/eventCover')
