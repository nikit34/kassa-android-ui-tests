from selenium.webdriver.common.by import By


class EventsDetailsPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.back_button = (self.ID, 'ru.rambler.kassa:id/leftIcon')
        self.like_button = (self.ID, 'ru.rambler.kassa:id/favoriteBtn')
        self.title = (self.ID, 'ru.rambler.kassa:id/title')
        self.description = (self.ID, 'ru.rambler.kassa:id/description')
        self.event_trailer = (self.ID, 'ru.rambler.kassa:id/eventTrailerPv')
        self.event_cover = (self.ID, 'ru.rambler.kassa:id/eventCover')
