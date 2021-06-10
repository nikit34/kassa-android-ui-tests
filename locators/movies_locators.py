from selenium.webdriver.common.by import By


class MoviesPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.feature_app_bar = (self.ID, 'ru.rambler.kassa.beta:id/featuringAppBar')
        self.tabs_rv = (self.ID, 'ru.rambler.kassa.beta:id/tabsRv')
        self.bottom_menu_id = (self.ID, 'ru.rambler.kassa.beta:id/bottomNavigation')
        self.event_name = (self.ID, 'ru.rambler.kassa.beta:id/eventName')
        self.back_button = (self.ID, 'ru.rambler.kassa.beta:id/leftIcon')
        self.tabs_events_id = (self.ID, 'ru.rambler.kassa.beta:id/tabsRv')
        self.carousel_rv = (self.ID, 'ru.rambler.kassa.beta:id/carouselRv')
        self.list_session_view = (self.ID, 'ru.rambler.kassa.beta:id/listSessionView')
        self.fastbuy_ticket_id = (self.ID, 'ru.rambler.kassa.beta:id/buyTicket')
        self.nearest_place_distance = (self.ID, 'ru.rambler.kassa.beta:id/placeDistanceTv')
        self.place_label = (self.ID, 'ru.rambler.kassa.beta:id/placeLabel')
        self.nearest_place = (self.ID, 'ru.rambler.kassa.beta:id/nearestPlaceName')
        self.arrow_right = (self.ID, 'ru.rambler.kassa.beta:id/forward')
        self.session_date = (self.ID, 'ru.rambler.kassa.beta:id/sessionDate')
        self.session_tags = (self.ID, 'ru.rambler.kassa.beta:id/sessionTags')
        self.session_price = (self.ID, 'ru.rambler.kassa.beta:id/sessionPrice')
        self.movies_title = (self.ID, 'ru.rambler.kassa.beta:id/title')
        self.event_img = (self.ID, 'ru.rambler.kassa.beta:id/eventImg')
        self.compilation_img = (self.ID, 'ru.rambler.kassa.beta:id/compilationImg')
        self.mature_text = (self.ID, 'ru.rambler.kassa.beta:id/matureText')
        self.premier_date = (self.ID, 'ru.rambler.kassa.beta:id/premiereDate')
        self.favorite_container = (self.ID, 'ru.rambler.kassa.beta:id/favoriteBtnContainer')
        self.filters_carousel = (self.ID, 'ru.rambler.kassa.beta:id/filtersRv')
        self.event_title = (self.ID, 'ru.rambler.kassa.beta:id/eventTitle')
        self.right_btn = (self.ID, 'ru.rambler.kassa.beta:id/rightBtn')
        self.title_tv = (self.ID, 'ru.rambler.kassa.beta:id/titleTv')