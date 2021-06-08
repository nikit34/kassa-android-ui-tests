from selenium.webdriver.common.by import By


class ShedulePageLocators:
    back_button = (By.ID, 'ru.rambler.kassa.beta:id/leftIcon')
    session_sheet = (By.ID, 'ru.rambler.kassa.beta:id/sessionsSheet')
    back_bar_button = (By.ID, 'ru.rambler.kassa.beta:id/leftIcon')
    event_name = (By.ID, 'ru.rambler.kassa.beta:id/titleTextView')
    map_button = (By.ID, 'ru.rambler.kassa.beta:id/firstRightIconContainer')
    search_field = (By.ID, 'ru.rambler.kassa.beta:id/input')
    filters = (By.ID, 'ru.rambler.kassa.beta:id/filtersRv')
    sheduler_place_name = (By.ID, 'ru.rambler.kassa.beta:id/placeName')
    sheduler_place_address = (By.ID, 'ru.rambler.kassa.beta:id/placeAddress')
    sheduler_geo_location_button = (By.ID, 'ru.rambler.kassa.beta:id/locationBtn')
    fastbuy_ticket_id = (By.ID, 'ru.rambler.kassa.beta:id/buyTicket')

