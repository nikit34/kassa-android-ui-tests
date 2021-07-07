import operator
from selenium.common.exceptions import NoSuchElementException
from urllib3.exceptions import ProtocolError

from templates.error import base_error


class Page:
    def __init__(self, driver):
        self.driver = driver

    def _increase_wait_(func):
        def wrapper(self, *args, **kwargs):
            while True:
                if self.repeat == '0':
                    if func(self, *args, **kwargs):
                        break
                    print(f'\n[click -> _increase_wait_ -> state 0] increment implicitly wait on {self.extra_interval} time')
                    self.driver.implicitly_wait(self.extra_interval)
                    print(f'[click -> _increase_wait_ -> state 0] {args} change to state 1: first act is unsuccessful')
                    self.repeat = '1'
                elif self.repeat == '1':
                    if func(self, *args, **kwargs):
                        print(f'[click -> _increase_wait_ -> state 1] {args} change to state 0: second act is successful')
                        self.repeat = '0'
                        break
                    print(f'[click -> _increase_wait_ -> state 1] {args} change to state <error>: first and second act is unsuccessful')
                    self.repeat = 'e'
                elif self.repeat == 'e':
                    print(f'[click -> _increase_wait_ -> state e] {args} repetition was done - final state')
                    raise NoSuchElementException(f'[click -> _increase_wait_ -> state e] {args} repetition was done - final state')
                else:
                    raise UnboundLocalError('[click -> _increase_wait_ -> state Unbound] State Machine is dangerous')
        return wrapper

    def find_element(self, *locator, extra_interval=50):
        try:
            elem = self.driver.find_element(*locator)
            assert elem.is_displayed(), f'[find_element] {locator} is not displayed'
        except (NoSuchElementException, AssertionError) as error:
            print(f'\n[find_element] increment implicitly wait on {extra_interval} time')
            self.driver.implicitly_wait(extra_interval)
            try:
                elem = self.driver.find_element(*locator)
                assert elem.is_enabled(), f'[find_element] {locator} is not enabled'
            except (NoSuchElementException, AssertionError) as error:
                self.driver.implicitly_wait(0)
                base_error(self.driver, *locator, crash_site='find_element -> nested except', msg='is not displayed')
        return elem

    @_increase_wait_
    def click(self, *locator):
        try:
            elements = self.driver.find_elements(*locator[:2])
            for elem in elements:
                assert elem.is_enabled(), f'[find_element] {locator} is not enabled'
                elem.click()
                return True
            raise NoSuchElementException("[click -> find_element] dont find")
        except (NoSuchElementException, AssertionError, ProtocolError) as error:
            base_error(self.driver, *locator, crash_site='click', msg='don`t click')

    def click_elem(self, elem):
        try:
            elem.click()
        except NoSuchElementException as error:
            base_error(self.driver, elem, crash_site='click', msg='don`t click')
            raise error

    def input(self, text, *locator):
        try:
            elem = self.find_element(*locator)
            elem.clear()
            elem.send_keys(text)
        except NoSuchElementException as error:
            base_error(self.driver, *locator, crash_site='input', msg='')
            raise error

    def not_displayed(self, *locator):
        try:
            self.driver.find_element(*locator)
            base_error(self.driver, *locator, crash_site='not_displayed', msg='on the Page')
        except NoSuchElementException:
            return True

    def matching_text(self, *locator, equal=True, pattern=''):
        text_elem = None
        try:
            text_elem = self.find_element(*locator).text
            if equal:
                assert text_elem == pattern, f'{locator} invalid text: {text_elem} != {pattern}'
            else:
                assert text_elem != pattern, f'{locator} matching text: {text_elem}'
            return True
        except (NoSuchElementException, AssertionError) as error:
            base_error(self.driver, *locator, crash_site='matching_text', msg=f'matching text: {text_elem}')
            raise error

    def check_state_selected(self, *locator, state=True):
        elem = self.find_element(*locator)
        try:
            if state:
                assert elem.is_selected(), f'invalid state: {elem}'
            else:
                assert not elem.is_selected(), f'invalid state: {elem}'
        except AssertionError as error:
            base_error(self.driver, *locator, crash_site='is_selected', msg='state is not valid')
            raise error


class Search:
    def __init__(self, token, pattern):
        self.token = token
        self.pattern = pattern

    @classmethod
    def matching_text(cls, token, pattern):
        this = cls(token, pattern)
        if '*' in this.token:
            return this.partially_matches()
        return this.completely_matches()

    def partially_matches(self):
        separate_token = self.token.split('*')[1::2]
        current_pattern = self.pattern
        found_result = []
        for part_token in separate_token:
            found_index = current_pattern.find(part_token)
            if found_index == -1:
                continue
            current_pattern = current_pattern[found_index:]
            found_result.append(part_token)
        return found_result

    def completely_matches(self):
        if self.pattern.find(self.token) == -1:
            return False
        return True

    @classmethod
    def condition_length(cls, length, sign, length_elem):
        if not isinstance(length, int):
            length = int(length)
        if not isinstance(length_elem, int):
            length_elem = int(length_elem)
        operators = {
            '<': operator.lt,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne,
            '>=': operator.ge,
            '>': operator.gt
        }
        if sign not in operators:
            raise KeyError('[ERROR] operator sign is invalid')
        operation = operators[sign]
        return operation(length, length_elem)


class Wait:
    def set_wait(self, context_driver, new_wait):
        self.custom_wait = new_wait
        try:
            context_driver.implicitly_wait(int(self.custom_wait))
        except TimeoutError as e:
            print(f'[ERROR] timeout was not installed - {e}')

    def get_last_wait(self):
        try:
            return self.custom_wait
        except AttributeError:
            print('Timeout was not installed')
            self.custom_wait = 0