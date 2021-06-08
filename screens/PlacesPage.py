from .action import Action
from .base import Page, Wait
from locators.places_locators import PlacesPageLocators
from locators.popup_locators import PopupLocators


class PlacesPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.act = Action(driver)

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_state_tabs(self):
        tabs = self.driver.find_elements(*PlacesPageLocators.tab)
        for tab in tabs:
            if tab.text == 'Кино':
                assert tab.is_selected(), f'invalid state: {tab}'
            else:
                assert not tab.is_selected(), f'invalid state: {tab}'

    def check_popup(self):
        self.find_element(*PopupLocators.next_btn)
        self.find_element(*PopupLocators.header)
        self.find_element(*PopupLocators.description)

    def pass_popup(self):
        try:
            self.click(*PopupLocators.next_btn)
        except AssertionError as error:
            error.args = ('popup is not worked')
            pass
