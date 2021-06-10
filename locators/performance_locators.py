from selenium.webdriver.common.by import By


class PerformancePageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.events = (self.ID, 'ru.rambler.kassa.beta:id/tab')
        self.title = (self.ID, 'ru.rambler.kassa.beta:id/title')
        self.event_name = (self.ID, 'ru.rambler.kassa.beta:id/eventName')
        self.session_day_of_month = (self.ID, 'ru.rambler.kassa.beta:id/sessionDayOfMonth')
        self.session_day_of_week_hour_minutes = (self.ID, 'ru.rambler.kassa.beta:id/sessionDayOfWeekHourMinutes')
        self.session_min_price = (self.ID, 'ru.rambler.kassa.beta:id/sessionMinPrice')
        self.compilation_img = (self.ID, 'ru.rambler.kassa.beta:id/compilationImg')
        self.event_title = (self.ID, 'ru.rambler.kassa.beta:id/eventTitle')
        self.event_genre = (self.ID, 'ru.rambler.kassa.beta:id/eventGenre')
        self.carousel_rv = (self.ID, 'ru.rambler.kassa.beta:id/carouselRv')
        self.single_session_view = (self.ID, 'ru.rambler.kassa.beta:id/singleSessionView')