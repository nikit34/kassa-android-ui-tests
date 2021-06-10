from selenium.webdriver.common.by import By


class PlacesPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.allow_geo_location_button = (self.ID, 'ru.rambler.kassa.beta:id/confirmPermissionBtn')
        self.close_allow_geo_location = (self.ID, 'ru.rambler.kassa.beta:id/closeViewBtn')
        self.tab = (self.ID, 'ru.rambler.kassa.beta:id/tab')
        self.input = (self.ID, 'ru.rambler.kassa.beta:id/input')
        self.events_carousel = (self.ID, 'ru.rambler.kassa.beta:id/eventsRv')
        self.event_img = (self.ID, 'ru.rambler.kassa.beta:id/eventImg')
        self.place_name = (self.ID, 'ru.rambler.kassa.beta:id/placeName')
        self.place_address = (self.ID, 'ru.rambler.kassa.beta:id/placeAddress')
        self.option_name = (self.ID, 'ru.rambler.kassa.beta:id/optionName')
