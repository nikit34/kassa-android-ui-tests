from selenium.webdriver.common.by import By


class TheatersPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.title = (self.ID, 'ru.rambler.kassa:id/title')
        self.event_name = (self.ID, 'ru.rambler.kassa:id/eventName')
        self.session_date = (self.ID, 'ru.rambler.kassa:id/sessionDate')
        self.session_price = (self.ID, 'ru.rambler.kassa:id/sessionPrice')
        self.compilation_img = (self.ID, 'ru.rambler.kassa:id/compilationImg')
        self.event_title = (self.ID, 'ru.rambler.kassa:id/eventTitle')
        self.event_genre = (self.ID, 'ru.rambler.kassa:id/eventGenre')
        self.carousel_rv = (self.ID, 'ru.rambler.kassa:id/carouselRv')
        self.text_place_label = (self.ID, 'ru.rambler.kassa:id/placeLabel')
        self.list_session_view = (self.ID, 'ru.rambler.kassa:id/listSessionView')