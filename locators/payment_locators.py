from selenium.webdriver.common.by import By


class PaymentPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.payment_button = (self.ID, 'ru.rambler.kassa.beta:id/inPaymentBtn')
