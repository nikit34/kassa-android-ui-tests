from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout
from locators.search_locators import SearchPageLocators
from app.check_api import CheckAPI


class SearchPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.search_locators = SearchPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_count_btn_filters(self):
        elems = self.driver.find_elements(*self.search_locators.btn_search_filter)
        assert len(elems) > 0, '[FAILED] Search buttons of filter dont display'

    @staticmethod
    def _get_content_filters(content):
        content_filters = []
        try:
            for filters in content['composedFilters']:
                for filter in filters['filters']:
                    for option in filter['options']:
                        content_filters.append(option['title'])
        except KeyError as error:
            print('keys inside \"composedFilters\" is not exist: ', error)
        return content_filters

    def _check_content_btn_filters(self, content_filters):
        count_filters = len(content_filters)
        count_founds_filters = 0
        founds_filters = []
        for _ in range(8):
            elems = self.driver.find_elements(*self.search_locators.btn_search_filter)
            for elem in elems:
                if elem.text in content_filters and elem.text not in founds_filters:
                    count_founds_filters += 1
                    founds_filters.append(elem.text)
            if count_filters == count_founds_filters:
                return
            self.act.swipe(70, 23, 30, 23)
        raise IndexError('Count scrolls completed')

    def check_btn_filters(self, dbg_api):
        for line in dbg_api.read_buffer(name_file='redis_filter.log'):
            content = dbg_api.get_content_response(line)
            content_filters = self._get_content_filters(content)
            self._check_content_btn_filters(content_filters)
            return

    @staticmethod
    def url_creations_movie_schedule_filter(msg):
        line = msg['data'].encode('utf-8')
        if CheckAPI.check_general_page_url('/creations/movie/schedule', line=line, params_after='limit'):
            with open('../../app/redis_filter.log', 'w') as f:
                f.write(line)

    @staticmethod
    def url_creations_performance_schedule_filter(msg):
        line = msg['data'].encode('utf-8')
        if CheckAPI.check_general_page_url('/creations/performance/schedule', line=line, params_after='limit'):
            with open('../../app/redis_filter.log', 'w') as f:
                f.write(line)

    @staticmethod
    def url_creations_concert_schedule_filter(msg):
        line = msg['data'].encode('utf-8')
        if CheckAPI.check_general_page_url('/creations/concert/schedule', line=line, params_after='limit'):
            with open('../../app/redis_filter.log', 'w') as f:
                f.write(line)

    @staticmethod
    def url_creations_event_schedule_filter(msg):
        line = msg['data'].encode('utf-8')
        if CheckAPI.check_general_page_url('/creations/event/schedule', line=line, params_after='limit'):
            with open('../../app/redis_filter.log', 'w') as f:
                f.write(line)

    def click_tab(self, num):
        tabs_elem = self.driver.find_elements(*self.search_locators.tab)
        len_tabs_elem = len(tabs_elem)
        if num < len_tabs_elem:
            self.click_elem(tabs_elem[num])
        else:
            raise IndexError(f'[ERROR] num: {num} beyond limit of number of elements count: {len_tabs_elem}')
