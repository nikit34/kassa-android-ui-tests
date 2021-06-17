from selenium.webdriver.common.by import By


class PlacesPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.allow_geo_location_button = (self.ID, 'ru.rambler.kassa:id/confirmPermissionBtn')
        self.close_allow_geo_location = (self.ID, 'ru.rambler.kassa:id/closeViewBtn')
        self.tab = (self.ID, 'ru.rambler.kassa:id/tab')
        self.input = (self.ID, 'ru.rambler.kassa:id/input')
        self.events_carousel = (self.ID, 'ru.rambler.kassa:id/eventsRv')
        self.event_img = (self.ID, 'ru.rambler.kassa:id/eventImg')
        self.place_name = (self.ID, 'ru.rambler.kassa:id/placeName')
        self.place_address = (self.ID, 'ru.rambler.kassa:id/placeAddress')
        self.option_name = (self.ID, 'ru.rambler.kassa:id/optionName')
