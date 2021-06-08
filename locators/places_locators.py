from selenium.webdriver.common.by import By


class PlacesPageLocators:
    allow_geo_location_button = (By.ID, 'ru.rambler.kassa.beta:id/confirmPermissionBtn')
    close_allow_geo_location = (By.ID, 'ru.rambler.kassa.beta:id/closeViewBtn')
    tab = (By.ID, 'ru.rambler.kassa.beta:id/tab')
    input = (By.ID, 'ru.rambler.kassa.beta:id/input')
    events_carousel = (By.ID, 'ru.rambler.kassa.beta:id/eventsRv')
    event_img = (By.ID, 'ru.rambler.kassa.beta:id/eventImg')
    place_name = (By.ID, 'ru.rambler.kassa.beta:id/placeName')
    place_address = (By.ID, 'ru.rambler.kassa.beta:id/placeAddress')
    option_name = (By.ID, 'ru.rambler.kassa.beta:id/optionName')
