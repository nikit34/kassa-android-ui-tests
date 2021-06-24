from selenium.webdriver.common.by import By


class FeedPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.input_search = (By.ID, 'ru.rambler.kassa.dev:id/input')
        self.btn_filters = (By.ID, 'ru.rambler.kassa.dev:id/optionName')
        self.img_events = (By.ID, 'ru.rambler.kassa.dev:id/eventCover')
        self.btn_back = (By.ID, 'ru.rambler.kassa.dev:id/leftIcon')
        self.btn_fast_buy = (By.ID, 'ru.rambler.kassa.dev:id/buyTicket')
        self.btn_events_name = (By.ID, 'ru.rambler.kassa.dev:id/eventName')
