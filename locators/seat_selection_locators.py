from selenium.webdriver.common.by import By


class SeatSelectionLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.back_button = (self.ID, 'ru.rambler.kassa.dev:id/leftIconContainer')
        self.place_name = (self.ID, 'ru.rambler.kassa.dev:id/tvPlaceName')
        self.place_sessions_rv = (self.ID, 'ru.rambler.kassa.dev:id/rvPlaceSessions')
        self.place_session = (self.ID, 'ru.rambler.kassa.dev:id/layoutPlaceSession')  # find_elements # selected
        self.place_session_tag = (self.ID, 'ru.rambler.kassa.dev:id/tvPlaceSessionTag')
        self.place_session_time = (self.ID, 'ru.rambler.kassa.dev:id/tvPlaceSessionTime')
        self.place_session_price = (self.ID, 'ru.rambler.kassa.dev:id/tvPlaceSessionPrice')
        self.hall_scheme = (self.ID, 'ru.rambler.kassa.dev:id/fragmentContainer')
        self.btn_continue = (self.ID, 'ru.rambler.kassa.dev:id/continueBtn')
        self.text_count_ticket = (self.ID, 'ru.rambler.kassa.dev:id/seatsAmount')
