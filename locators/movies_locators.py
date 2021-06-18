from selenium.webdriver.common.by import By


class MoviesPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.feature_app_bar = (self.ID, 'ru.rambler.kassa:id/featuringAppBar')
        self.tabs_rv = (self.ID, 'ru.rambler.kassa:id/tabsRv')
        self.bottom_menu_id = (self.ID, 'ru.rambler.kassa:id/bottomNavigation')
        self.event_name = (self.ID, 'ru.rambler.kassa:id/eventName')
        self.back_button = (self.ID, 'ru.rambler.kassa:id/leftIcon')
        self.tabs_events_id = (self.ID, 'ru.rambler.kassa:id/tabsRv')
        self.tab = (self.ID, 'ru.rambler.kassa:id/tab')
        self.carousel_rv = (self.ID, 'ru.rambler.kassa:id/carouselRv')
        self.list_session_view = (self.ID, 'ru.rambler.kassa:id/listSessionView')
        self.fastbuy_ticket_id = (self.ID, 'ru.rambler.kassa:id/buyTicket')
        self.nearest_place_distance = (self.ID, 'ru.rambler.kassa:id/placeDistanceTv')
        self.place_label = (self.ID, 'ru.rambler.kassa:id/placeLabel')
        self.nearest_place = (self.ID, 'ru.rambler.kassa:id/nearestPlaceName')
        self.arrow_right = (self.ID, 'ru.rambler.kassa:id/forward')
        self.session_date = (self.ID, 'ru.rambler.kassa:id/sessionDate')
        self.session_tags = (self.ID, 'ru.rambler.kassa:id/sessionTags')
        self.session_price = (self.ID, 'ru.rambler.kassa:id/sessionPrice')
        self.movies_title = (self.ID, 'ru.rambler.kassa:id/title')
        self.event_img = (self.ID, 'ru.rambler.kassa:id/eventImg')
        self.compilation_img = (self.ID, 'ru.rambler.kassa:id/compilationImg')
        self.mature_text = (self.ID, 'ru.rambler.kassa:id/matureText')
        self.premier_date = (self.ID, 'ru.rambler.kassa:id/premiereDate')
        self.favorite_container = (self.ID, 'ru.rambler.kassa:id/favoriteBtnContainer')
        self.filters_carousel = (self.ID, 'ru.rambler.kassa:id/filtersRv')
        self.event_title = (self.ID, 'ru.rambler.kassa:id/eventTitle')
        self.right_btn = (self.ID, 'ru.rambler.kassa:id/rightBtn')
        self.title_tv = (self.ID, 'ru.rambler.kassa:id/titleTv')