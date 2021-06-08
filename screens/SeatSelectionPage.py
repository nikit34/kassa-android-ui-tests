from time import sleep
from PIL import Image
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from .action import Action
from .base import Page, Wait
from locators.seat_selection_locators import SeatSelectionLocators


class SeatSelectionPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.act = Action(driver)

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def select_seat(self, path):
        captures = self.compare_pixel_seat(path)

        left_border = self.act.width * 0.15
        right_border = self.act.width * 0.85
        top_border = self.act.height * 0.45
        bottom_border = self.act.height * 0.9
        area_captures = []
        for cap in captures:
            if (cap[0] > left_border and \
                cap[0] < right_border) and \
                (cap[1] > top_border and \
                cap[1] < bottom_border):
                area_captures.append(cap)

        epsilon_y = round(self.act.height * 0.05)
        epsilon_x = round(self.act.width * 0.05)

        classters = [{'arg': area_captures[0], 'num': 1}]
        for i in range(1, len(area_captures)):
            compared = False
            for classter in classters:
                if abs(classter['arg'][0] - area_captures[i][0]) < epsilon_x and abs(classter['arg'][1] - area_captures[i][1]) < epsilon_y:
                    x = round((classter['arg'][0] * classter['num'] + area_captures[i][0]) / (classter['num'] + 1), 2)
                    y = round((classter['arg'][1] * classter['num'] + area_captures[i][1]) / (classter['num'] + 1), 2)
                    classter.update({'arg': (x, y)})
                    classter['num'] += 1
                    compared = True
            if not compared:
                classters.append({'arg': area_captures[i], 'num': 1})
        actions = TouchAction(self.driver)
        for classter in classters:
            actions.tap(x=classter['arg'][0], y=classter['arg'][1])
            actions.perform()
            sleep(1)
            try:
                self.find_element(*SeatSelectionLocators.continue_btn)
                break
            except (NoSuchElementException, AssertionError) as error:
                error.args = ('classters invalid')
                pass

    def compare_pixel_seat(self, path):
        image = Image.open(path)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        coords = []
        for x in range(width):
            for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                if r < 15 and 115 < g < 130 and b > 240:
                    coords.append((x, y))
        return coords


















