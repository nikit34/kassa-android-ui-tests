import os
from datetime import datetime
import numpy as np
from PIL import Image


class Screenshot:
    def __init__(self, driver, location=None):
        self.path = location
        self.file = driver.get_screenshot_as_file(self._path)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, location=None):
        now = datetime.now().strftime('%d_%m_%Y__%H_%M_%S')
        absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../kassa-ui-tests"))
        if location is None:
            self._path = absolute_path + f'/screenshots/session_{now}.png'
        else:
            self._path = absolute_path + f'/tests/{location}/screenshots/session_{now}.png'

    @path.deleter
    def path(self):
        del self._path

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = file

    @file.deleter
    def file(self):
        os.remove(self._path)
        del self._file

    @staticmethod
    def convert_img_pixels(path):
        try:
            image = Image.open(path)
        except IOError:
            raise BaseException("Image did not open")
        pix = np.array(image.convert('RGB'))
        return pix

    @staticmethod
    def get_size_image(pix):
        return pix.shape[0], pix.shape[1]

    @staticmethod
    def compare_images(first_pix, second_pix):
        if first_pix.shape[0] != second_pix.shape[0] or first_pix.shape[1] != second_pix.shape[1]:
            return False
        sum_difference = np.array([0, 0, 0])
        for y in range(first_pix.shape[0]):
            for x in range(first_pix.shape[1]):
                sum_difference[0] += abs(first_pix[y][x][0] - second_pix[y][x][0])
                sum_difference[1] += abs(first_pix[y][x][1] - second_pix[y][x][1])
                sum_difference[2] += abs(first_pix[y][x][2] - second_pix[y][x][2])
            if np.sum(sum_difference) > 20:
                return False
        return True





