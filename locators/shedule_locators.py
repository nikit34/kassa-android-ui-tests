from selenium.webdriver.common.by import By


class ShedulePageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.back_button = (self.ID, 'ru.rambler.kassa:id/leftIcon')
        self.session_sheet = (self.ID, 'ru.rambler.kassa:id/sessionsSheet')
        self.back_bar_button = (self.ID, 'ru.rambler.kassa:id/leftIcon')
        self.event_name = (self.ID, 'ru.rambler.kassa:id/titleTextView')
        self.map_button = (self.ID, 'ru.rambler.kassa:id/firstRightIconContainer')
        self.search_field = (self.ID, 'ru.rambler.kassa:id/input')
        self.filters = (self.ID, 'ru.rambler.kassa:id/filtersRv')
        self.sheduler_place_name = (self.ID, 'ru.rambler.kassa:id/placeName')
        self.sheduler_place_address = (self.ID, 'ru.rambler.kassa:id/placeAddress')
        self.sheduler_geo_location_button = (self.ID, 'ru.rambler.kassa:id/locationBtn')
        self.fastbuy_ticket_id = (self.ID, 'ru.rambler.kassa:id/buyTicket')

