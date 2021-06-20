from selenium.webdriver.common.by import By


class TheatersPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.events = (self.ID, 'ru.rambler.kassa:id/tab')
        self.title = (self.ID, 'ru.rambler.kassa:id/title')
        self.event_name = (self.ID, 'ru.rambler.kassa:id/eventName')
        self.session_day_of_month = (self.ID, 'ru.rambler.kassa:id/sessionDayOfMonth')
        self.session_day_of_week_hour_minutes = (self.ID, 'ru.rambler.kassa:id/sessionDayOfWeekHourMinutes')
        self.session_min_price = (self.ID, 'ru.rambler.kassa:id/sessionMinPrice')
        self.compilation_img = (self.ID, 'ru.rambler.kassa:id/compilationImg')
        self.event_title = (self.ID, 'ru.rambler.kassa:id/eventTitle')
        self.event_genre = (self.ID, 'ru.rambler.kassa:id/eventGenre')
        self.carousel_rv = (self.ID, 'ru.rambler.kassa:id/carouselRv')
        self.single_session_view = (self.ID, 'ru.rambler.kassa:id/singleSessionView')