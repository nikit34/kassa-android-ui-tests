from time import sleep
import math
from PIL import Image, ImageDraw
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import numpy as np

from locators.seat_selection_locators import SeatSelectionLocators
from utils.factory_screenshots import Screenshot
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class SeatSelectionPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.seat_selection_locators = SeatSelectionLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    class SelectorSeat:
        def __init__(self, driver):
            self.height, self.width = Action.get_size_page(driver)
            self.epsilon = 0.05

        def form_clusters(self, area_coords):
            epsilon_y = round(self.height * self.epsilon)
            epsilon_x = round(self.width * self.epsilon)

            i_clusters = 0
            clusters = [{'arg': area_coords[i_clusters], 'num': 1},]

            area_coords = iter(area_coords)
            next(area_coords)
            for area_coord in area_coords:
                if abs(clusters[i_clusters]['arg'][0] - area_coord[0]) < epsilon_x \
                        and abs(clusters[i_clusters]['arg'][1] - area_coord[1]) < epsilon_y:
                    x = round((clusters[i_clusters]['arg'][0] * clusters[i_clusters]['num'] + area_coord[0]) / (clusters[i_clusters]['num'] + 1), 2)
                    y = round((clusters[i_clusters]['arg'][1] * clusters[i_clusters]['num'] + area_coord[1]) / (clusters[i_clusters]['num'] + 1), 2)
                    clusters[i_clusters]['arg'] = (x, y)
                    clusters[i_clusters]['num'] += 1
                elif len(clusters) - 1 != i_clusters:
                    i_clusters += 1
                else:
                    clusters.append({'arg': area_coord, 'num': 1})
                    i_clusters = 0
            return np.array(clusters)

        def validate_select_seat(self, path, coords):
            image = Image.open(path)
            width = image.size[0]
            height = image.size[1]
            draw = ImageDraw.Draw(image)
            for p in coords:
                x1 = (p['arg'][0] * width / self.width - 20)
                y1 = (p['arg'][1] * height / self.height - 20)
                x2 = (p['arg'][0] * width / self.width + 20)
                y2 = (p['arg'][1] * height / self.height + 20)
                draw.ellipse((x1, y1, x2, y2), fill='red', outline='red')
            image.show()

        def cut_image(self, width, height):
            return width * 0.15, width * 0.85, height * 0.45, height * 0.9

        def get_round_board(self, pix):
            height, width = Screenshot.get_size_image(pix)
            left_board, right_board, top_board, bottom_board = self.cut_image(width, height)
            return math.floor(left_board), math.ceil(right_board) ,math.floor(top_board), math.ceil(bottom_board)

        def area_coords(self, pix):
            height, width = Screenshot.get_size_image(pix)
            left_round_board, right_round_board, top_round_board, bottom_round_board = self.get_round_board(pix)
            area_coords = []
            for x in range(left_round_board, right_round_board, 5):
                for y in range(top_round_board, bottom_round_board, 5):
                    r = pix[y, x][0]
                    g = pix[y, x][1]
                    b = pix[y, x][2]
                    if r < 20 and 90 < g < 180 and b > 230:
                        x_normalize = x / width
                        y_normalize = y / height
                        x_screen = round(x_normalize * self.width, 2)
                        y_screen = round(y_normalize * self.height, 2)
                        area_coords.append((x_screen, y_screen))
            return np.array(area_coords)

    class ActionSelector(TouchAction):
        def __init__(self, driver, valid_locator):
            super().__init__(driver=driver)
            self.driver = driver
            self.valid_locator = valid_locator

        def tap_places(self, clusters, count_places=1):
            for i, cluster in np.ndenumerate(clusters):
                self.tap(x=cluster['arg'][0], y=cluster['arg'][1])
                self.perform()
                sleep(1)
                if self._valid_tap(count_places=count_places):
                    return True
            return False

        def _valid_tap(self, count_places=1):
            valid_str_tap = ''
            if count_places == 1:
                valid_str_tap = str(count_places) + ' билет'
            elif 1 < count_places < 5:
                valid_str_tap = str(count_places) + ' билета'
            elif count_places == 5:
                valid_str_tap = str(count_places) + ' билетов'
            else:
                raise ValueError(f'[FAILED] count_places: {count_places} - invalid interval counts')
            try:
                elem = self.driver.find_element(*self.valid_locator)
                assert elem.text == valid_str_tap
                return True
            except (NoSuchElementException, AssertionError) as error:
                error.args += ('[ERROR] tickets count is invalid',)
                print('[ERROR] tickets count is invalid')
            return False

    def skip_seat_selection(self, count_places=1, dbg_select_seat=False):
        sleep(1)
        screenshot = Screenshot(self.driver)
        self.select_seat(screenshot.path, count_places=count_places, dbg_select_seat=dbg_select_seat)
        del screenshot.file

    def select_seat(self, path, count_places=1, dbg_select_seat=False):
        selector_seat = self.SelectorSeat(self.driver)

        pix = Screenshot.convert_img_pixels(path)
        area_coords = selector_seat.area_coords(pix)
        clusters = selector_seat.form_clusters(area_coords)

        last_wait = self.get_last_wait()
        self.set_custom_wait(5)

        if dbg_select_seat:
            selector_seat.validate_select_seat(path, clusters)

        act_selector = self.ActionSelector(self.driver, self.seat_selection_locators.text_count_ticket)
        if not act_selector.tap_places(clusters, count_places=count_places):
            raise Exception("[FAILED] No seats have been chosen")
        self.set_custom_wait(last_wait)






