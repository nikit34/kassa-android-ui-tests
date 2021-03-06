from selenium.webdriver.common.by import By


class CheckoutPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.text_total_price = (self.ID, 'ru.rambler.kassa.dev:id/totalPriceTv')
        self.text_event_title = (self.ID, 'ru.rambler.kassa.dev:id/titleEventTv')
        self.btn_continue = (self.ID, 'ru.rambler.kassa.dev:id/continueBtn')
        self.input_email = (self.ID, 'ru.rambler.kassa.dev:id/emailEdit')
        self.input_phone = (self.ID, 'ru.rambler.kassa.dev:id/numberEdit')