from selenium.webdriver.common.by import By


class SeatSelectionLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.back_button = (self.ID, 'ru.rambler.kassa.beta:id/leftIconContainer')
        self.place_name = (self.ID, 'ru.rambler.kassa.beta:id/tvPlaceName')
        self.place_sessions_rv = (self.ID, 'ru.rambler.kassa.beta:id/rvPlaceSessions')
        self.place_session = (self.ID, 'ru.rambler.kassa.beta:id/layoutPlaceSession')  # find_elements # selected
        self.place_session_tag = (self.ID, 'ru.rambler.kassa.beta:id/tvPlaceSessionTag')
        self.place_session_time = (self.ID, 'ru.rambler.kassa.beta:id/tvPlaceSessionTime')
        self.place_session_price = (self.ID, 'ru.rambler.kassa.beta:id/tvPlaceSessionPrice')
        self.hall_scheme = (self.ID, 'ru.rambler.kassa.beta:id/fragmentContainer')
        self.continue_btn = (self.ID, 'ru.rambler.kassa.beta:id/continueBtn')
