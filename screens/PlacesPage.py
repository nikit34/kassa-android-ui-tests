from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout
from locators.places_locators import PlacesPageLocators
from locators.popup_locators import PopupLocators


class PlacesPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.places_locators = PlacesPageLocators()
        self.popup_locators = PopupLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_state_tabs(self):
        tabs = self.driver.find_elements(*self.places_locators.tab)
        for tab in tabs:
            if tab.text == 'Кино':
                assert tab.is_selected(), f'invalid state: {tab}'
            else:
                assert not tab.is_selected(), f'invalid state: {tab}'

    def check_popup(self):
        self.find_element(*self.popup_locators.next_btn)
        self.find_element(*self.popup_locators.header)
        self.find_element(*self.popup_locators.description)

    def pass_popup(self):
        try:
            self.click(*self.popup_locators.next_btn)
        except AssertionError as error:
            error.args = ('popup is not worked')
            pass
