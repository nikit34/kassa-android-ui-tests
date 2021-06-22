from random import randrange

from locators.concerts_locators import ConcertsPageLocators

from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class ConcertsPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.concerts_locators = ConcertsPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_carousel(self):
        base_canvas = self.find_element(*self.concerts_locators.carousel_rv)
        base_canvas_row = base_canvas.find_element(*self.concerts_locators.single_session_view)

        random_num = randrange(16, 63)  # 1000 to 3333 in 4 notation
        while True:
            current_check = random_num % 4

            if current_check == 0:
                base_canvas.find_element(*self.concerts_locators.event_name)
            elif current_check == 1:
                base_canvas_row.find_element(*self.concerts_locators.session_day_month)
            elif current_check == 2:
                base_canvas_row.find_element(*self.concerts_locators.session_day_week)
            elif current_check == 3:
                base_canvas_row.find_element(*self.concerts_locators.session_price)

            random_num //= 4
            if random_num == 0:
                break
            self.act.swipe(80, 30, 20, 30)
