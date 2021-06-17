from selenium.webdriver.common.by import By


class ConcertsPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.tab = (self.ID, 'ru.rambler.kassa:id/tab')
        self.event_name = (self.ID, 'ru.rambler.kassa:id/eventName')
        self.session_day_of_month = (self.ID, 'ru.rambler.kassa:id/sessionDayOfMonth')
        self.session_min_price = (self.ID, 'ru.rambler.kassa:id/sessionMinPrice')
        self.session_day_of_week_hour_minutes = (self.ID, 'ru.rambler.kassa:id/sessionDayOfWeekHourMinutes')
        self.title = (self.ID, 'ru.rambler.kassa:id/title')
        self.event_img = (self.ID, 'ru.rambler.kanamessa.beta:id/eventImg')
        self.carousel_rv = (self.ID, 'ru.rambler.kassa:id/carouselRv')
        self.single_session_view = (self.ID, 'ru.rambler.kassa:id/singleSessionView')