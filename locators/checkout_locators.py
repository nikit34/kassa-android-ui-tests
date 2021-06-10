from selenium.webdriver.common.by import By


class CheckoutPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.total_price = (self.ID, 'ru.rambler.kassa.beta:id/totalPriceTv')
        self.checkout_section_title = (self.ID, 'ru.rambler.kassa.beta:id/checkoutSectionTitle')
        self.continue_btn = (self.ID, 'ru.rambler.kassa.beta:id/continueBtn')
