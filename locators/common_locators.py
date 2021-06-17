from selenium.webdriver.common.by import By


class CommonLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.tab_trend = (self.ID, 'ru.rambler.kassa:id/tab_trend')
        self.tab_search = (self.ID, 'ru.rambler.kassa:id/tab_search')
        self.tab_ticket = (self.ID, 'ru.rambler.kassa:id/tab_ticket')
        self.tab_places = (self.ID, 'ru.rambler.kassa:id/tab_places')
        self.tab_profile = (self.ID, 'ru.rambler.kassa:id/tab_menu')
