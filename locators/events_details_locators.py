from selenium.webdriver.common.by import By


class EventsDetailsPageLocators:
    back_button = (By.ID, 'ru.rambler.kassa.beta:id/leftIcon')
    like_button = (By.ID, 'ru.rambler.kassa.beta:id/favoriteBtn')
    title = (By.ID, 'ru.rambler.kassa.beta:id/title')
    description = (By.ID, 'ru.rambler.kassa.beta:id/description')
    event_trailer = (By.ID, 'ru.rambler.kassa.beta:id/eventTrailerPv')
    event_cover = (By.ID, 'ru.rambler.kassa.beta:id/eventCover')
