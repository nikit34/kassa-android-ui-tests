from .base import Page


class Action(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()

        def get_size_page():
            size = self.driver.get_window_size()
            return size['height'], size['width']

        self.height, self.width = get_size_page()

    # def calc_coords_to_percent(self, x, y):
    #     px = float(x) / self.width * 100
    #     py = float(y) / self.height * 100
    #     return px, py, px2, py2

    def calc_percent_to_coords(self, px, py):
        x = float(px) / 100 * self.width
        y = float(py) / 100 * self.height
        return x, y

    def swipe(self, px1, py1, px2, py2):
        x1, y1 = self.calc_percent_to_coords(px1, py1)
        x2, y2 = self.calc_percent_to_coords(px2, py2)
        self.driver.swipe(x1, y1, x2, y2)
        return True


