from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    total_price = (By.ID, 'ru.rambler.kassa.beta:id/totalPriceTv')
    checkout_section_title = (By.ID, 'ru.rambler.kassa.beta:id/checkoutSectionTitle')
    continue_btn = (By.ID, 'ru.rambler.kassa.beta:id/continueBtn')
