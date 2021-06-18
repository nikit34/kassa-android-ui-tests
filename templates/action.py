import os
from subprocess import Popen, TimeoutExpired, PIPE
from appium.webdriver.common.touch_action import TouchAction

from templates.base import Page


class Action(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()

        self.height, self.width = self.get_size_page(self.driver)

    @staticmethod
    def get_size_page(driver):
        size = driver.get_window_size()
        return size['height'], size['width']

    def calc_coords_to_percent(self, x, y):
        px = float(x) / self.width * 100
        py = float(y) / self.height * 100
        return px, py

    def calc_percent_to_coords(self, px, py):
        x = float(px) / 100 * self.width
        y = float(py) / 100 * self.height
        return x, y

    def swipe(self, px1, py1, px2, py2):
        x1, y1 = self.calc_percent_to_coords(px1, py1)
        x2, y2 = self.calc_percent_to_coords(px2, py2)
        action = TouchAction(self.driver)
        action.press(None, x1, y1)
        action.wait(400)
        action.move_to(None, x2, y2)
        action.release()
        action.perform()
        return True

    def click_by_coords(self, px, py):
        x, y = self.calc_percent_to_coords(px, py)
        action = TouchAction(self.driver)
        action.tap(None, x, y)
        action.release()
        action.perform()

