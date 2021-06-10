import pytest
import time
import inspect
from psycopg2 import sql
from datetime import datetime, timezone

from templates.base import Page


class RecordTimeout(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_previous_func = ''

        self.actions = {
            'find_element': super().find_element,
            'click': super().click
        }

    def _timeout_action(self, action, *args, **kwargs):
        ts = time.time()
        elem = self.actions[action](*args, **kwargs)
        timeout = time.time() - ts
        return timeout, elem

    @staticmethod
    def _get_name_current_test():
        inspect_stack = inspect.getouterframes(inspect.currentframe())
        i = 2
        while not inspect_stack[i].function.startswith('test_'):
            i += 1
        return inspect_stack[i].function

    def _count_call_unique_func(self, name_calling_func):
        if self.name_previous_func != name_calling_func:
            self.name_previous_func = name_calling_func
            pytest.count_call_unique_func += 1

    @staticmethod
    def _insert_name_test(name_calling_func):
        insert_query = sql.SQL("INSERT INTO metric_autotests.public.name_test ({}, {}) VALUES ({}, {});").format(
            sql.Identifier("id_test"),
            sql.Identifier("name_test"),

            sql.Literal(pytest.count_call_unique_func),
            sql.Literal(name_calling_func)
        )
        pytest.cursor.execute(insert_query)
        pytest.connection.commit()

    @staticmethod
    def _insert_method(table, **column_value):
        date_time = datetime.now(timezone.utc)
        insert_query = sql.SQL("INSERT INTO {} ({}, {}, {}) VALUES ({}, {}, {});").format(
            sql.Identifier('metric_autotests', 'public', table),

            sql.Identifier("id_test"),
            sql.Identifier(column_value["column"]),
            sql.Identifier("date_time"),

            sql.Literal(pytest.count_call_unique_func),
            sql.Literal(column_value["value"]),
            sql.Literal(date_time)
        )
        pytest.cursor.execute(insert_query)
        pytest.connection.commit()

    def _insert(self, table, **column_value):
        name_calling_func = self._get_name_current_test()
        self._count_call_unique_func(name_calling_func)
        self._insert_name_test(name_calling_func)
        self._insert_method(table, **column_value)

    def find_element(self, *locator, extra_interval=50):
        timeout, elem = self._timeout_action('find_element', *locator, extra_interval=extra_interval)
        self._insert('find_element_timeout', column='find_element', value=timeout)
        return elem

    def click(self, *locator):
        timeout, elem = self._timeout_action('click', *locator)
        self._insert('click_timeout', column='click', value=timeout)
