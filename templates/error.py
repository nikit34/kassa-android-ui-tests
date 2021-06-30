import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from telegram_bot.client import TGClient


BTN_SYSTEM_CLOSE_APP = (By.ID, ' android:id/aerr_close')

def base_error(driver, error, *object_except, crash_site=None, msg=None):
    try:
        driver.click(*BTN_SYSTEM_CLOSE_APP)
    except NoSuchElementException:
        pass

    if None in [msg, crash_site]:
        raise ValueError("Improper use of custom exception class")

    TGClient.tg_pass_msg_screenshot(driver.get_screenshot_as_png(), *object_except, crash_site=crash_site)
    allure.attach(driver.get_screenshot_as_png(), name=f'[{crash_site}] {object_except}', attachment_type=AttachmentType.PNG)
    print(f'[{crash_site}] {object_except} {msg}')
    error.args = (f'{object_except} {msg}', 'logging error',)
    return error
