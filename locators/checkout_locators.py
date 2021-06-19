from selenium.webdriver.common.by import By


class CheckoutPageLocators(By):
    def __init__(self):
        super(By, self).__init__()

        self.total_price = (self.ID, 'ru.rambler.kassa:id/totalPriceTv')
        self.checkout_section_title = (self.ID, 'ru.rambler.kassa:id/checkoutSectionTitle')
        self.btn_continue = (self.ID, 'ru.rambler.kassa:id/continueBtn')
