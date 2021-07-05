import pytest
import os
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from utils.emulator_act import reboot_emulator

from .config import \
    APPIUM_HOST, \
    APPIUM_LOCAL, \
    DESIRED_CAPS_HOST, \
    DESIRED_CAPS_NO_CACHE_HOST, \
    DESIRED_CAPS_LOCAL, \
    DESIRED_CAPS_NO_CACHE_LOCAL
from testrail_logging import Testrail
from db.db_logging import connect_db, disconnect_db


def pytest_addoption(parser):
    parser.addoption(
        '--host', action='store_true', default=False, help='locally or server running'
    )


def pytest_configure():
    connect_db()
    Testrail.logging_start()
    pytest.count_call_unique_func = 0


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        Testrail.logging_step(result.outcome, result.nodeid, result.duration)
    if result.outcome == 'failed':
        reboot_emulator()


@pytest.fixture(scope='function')
def driver_noCache(request):
    if request.config.getoption('--host'):
        DESIRED_CAPS_NO_CACHE_HOST['app'] = os.getcwd() + '/app/app-kassa-debug.apk'
        driver = webdriver.Remote(APPIUM_HOST, desired_capabilities=DESIRED_CAPS_NO_CACHE_HOST)
    else:
        driver = webdriver.Remote(APPIUM_LOCAL, desired_capabilities=DESIRED_CAPS_NO_CACHE_LOCAL)
    driver.implicitly_wait(10)
    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver(request):
    if request.config.getoption('--host'):
        DESIRED_CAPS_HOST['app'] = os.getcwd() + '/app/app-kassa-debug.apk'
        driver = webdriver.Remote(APPIUM_HOST, desired_capabilities=DESIRED_CAPS_HOST)
    else:
        driver = webdriver.Remote(APPIUM_LOCAL, desired_capabilities=DESIRED_CAPS_LOCAL)
    driver.implicitly_wait(10)
    driver.wait = WebDriverWait(driver, 5)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def db_session(request):
    yield
    disconnect_db()

