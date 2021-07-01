from selenium.webdriver.common.by import By


class SearchPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.tab = (self.ID, 'ru.rambler.kassa.dev:id/tab')
        self.input_search_field = (self.ID, 'ru.rambler.kassa.dev:id/searchView')
        self.btn_search_filter = (self.ID, 'ru.rambler.kassa.dev:id/optionName')
        self.btn_data_details_movie = (self.ID, 'ru.rambler.kassa.dev:id/searchEventSessionDayOfMonth')
        self.btn_min_price_shedule_movie = (self.ID, 'u.rambler.kassa.dev:id/searchEventSessionMinPrice')
        self.img_movie = (self.ID, 'ru.rambler.kassa.dev:id/searchEventImg')
        self.text_title_movie = (self.ID, 'ru.rambler.kassa.dev:id/searchEventName')
        self.btn_rating_movie = (self.ID, 'ru.rambler.kassa.dev:id/ratingTextView')