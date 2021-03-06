from selenium.webdriver.common.by import By


class TheatersPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.title = (self.ID, 'ru.rambler.kassa.dev:id/title')
        self.event_name = (self.ID, 'ru.rambler.kassa.dev:id/eventName')
        self.session_day_month = (self.ID, 'ru.rambler.kassa.dev:id/sessionDayOfMonth')
        self.session_day_week = (self.ID, 'ru.rambler.kassa.dev:id/sessionDayOfWeekHourMinutes')
        self.session_price = (self.ID, 'ru.rambler.kassa.dev:id/sessionMinPrice')
        self.img_popular_movies = (self.ID, 'ru.rambler.kassa.dev:id/compilationImg')
        self.event_title = (self.ID, 'ru.rambler.kassa.dev:id/eventTitle')
        self.event_genre = (self.ID, 'ru.rambler.kassa.dev:id/eventGenre')
        self.carousel_rv = (self.ID, 'ru.rambler.kassa.dev:id/carouselRv')
        self.text_place_label = (self.ID, 'ru.rambler.kassa.dev:id/placeLabel')
        self.single_session_view = (self.ID, 'ru.rambler.kassa.dev:id/singleSessionView')