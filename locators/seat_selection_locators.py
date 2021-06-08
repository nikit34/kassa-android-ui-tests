from selenium.webdriver.common.by import By


class SeatSelectionLocators:
    back_button = (By.ID, 'ru.rambler.kassa.beta:id/leftIconContainer')
    place_name = (By.ID, 'ru.rambler.kassa.beta:id/tvPlaceName')
    place_sessions_rv = (By.ID, 'ru.rambler.kassa.beta:id/rvPlaceSessions')
    place_session = (By.ID, 'ru.rambler.kassa.beta:id/layoutPlaceSession')  # find_elements # selected
    place_session_tag = (By.ID, 'ru.rambler.kassa.beta:id/tvPlaceSessionTag')
    place_session_time = (By.ID, 'ru.rambler.kassa.beta:id/tvPlaceSessionTime')
    place_session_price = (By.ID, 'ru.rambler.kassa.beta:id/tvPlaceSessionPrice')
    hall_scheme = (By.ID, 'ru.rambler.kassa.beta:id/fragmentContainer')
    continue_btn = (By.ID, 'ru.rambler.kassa.beta:id/continueBtn')
