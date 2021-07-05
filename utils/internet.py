from time import sleep
from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException
from appium.webdriver.common.mobileby import MobileBy
import os

from templates.action import Action
from utils.emulator_act import reboot_emulator


AIRPLANE_MODE = (MobileBy.ACCESSIBILITY_ID, 'Airplane mode')
BTN_SETTINGS = (MobileBy.ACCESSIBILITY_ID, 'Open settings.')
BTN_ROW_TITLE_SETTINGS = (MobileBy.ID, 'android:id/title')
BTN_MODIFY_NETWORK = (MobileBy.ACCESSIBILITY_ID, 'Modify')
BTN_ROW_ADVANCED_NETWORK_DETAILS = (MobileBy.ID, 'com.android.settings:id/wifi_advanced_togglebox')
BTN_ROW_PROXY_NETWORK_DETAILS = (MobileBy.ID, 'com.android.settings:id/proxy_settings')
BTN_ROW_PROXY_MODES_NETWORK_DETAILS = (MobileBy.ID, 'android:id/text1')
BTN_SAVE_MODIFY = (MobileBy.ID, 'android:id/button1')
INPUT_PROXY_HOSTNAME = (MobileBy.ID, 'com.android.settings:id/proxy_hostname')
INPUT_PROXY_PORT = (MobileBy.ID, 'com.android.settings:id/proxy_port')


def switch_airplane_mode(driver, to_state=True):
    act = Action(driver)
    act.swipe(50, 0, 50, 80)
    act.swipe(50, 15, 50, 50)
    act.swipe(90, 30, 10, 30)
    elem = driver.find_element(*AIRPLANE_MODE)
    if to_state:
        assert elem.text == 'Off', f'[ERROR] state Internet connection is not valid'
    else:
        assert elem.text == 'On', f'[ERROR] state Internet connection is not valid'
    elem.click()
    act.swipe(50, 90, 50, 30)


def contains_ip():
    output = os.popen('ifconfig').read()
    left_index = 0
    right_index = 17
    while right_index - left_index != 18 and right_index - left_index != 19:
        try:
            while right_index - left_index > 18:
                left_index = output.index('inet ', left_index + 1)
            while right_index - left_index < 18:
                right_index = output.index('netmask', right_index + 1)
        except ValueError as error:
            print('[ERROR] ip has been changed', error)
    return output[left_index+5:right_index-1]


def _click_by_text(driver, *locator, text):
    elems = driver.find_elements(*locator)
    for elem in elems:
        if elem.text == text:
            elem.click()
            break


def switch_proxy_mode(driver, to_state=True):
    try:
        act = Action(driver)
        act.swipe(50, 0, 50, 80)
        act.swipe(50, 15, 50, 50)
        driver.find_element(*BTN_SETTINGS).click()
        sleep(1)
        _click_by_text(driver, *BTN_ROW_TITLE_SETTINGS, text='Network & internet')
        sleep(1)
        _click_by_text(driver, *BTN_ROW_TITLE_SETTINGS, text='Wi‑Fi')
        sleep(1)
        _click_by_text(driver, *BTN_ROW_TITLE_SETTINGS, text='AndroidWifi')
        driver.find_element(*BTN_MODIFY_NETWORK).click()
    except (NoSuchElementException, InvalidElementStateException):
        reboot_emulator()
        switch_proxy_mode(driver, to_state)
    try:
        if to_state:
            driver.find_element(*BTN_ROW_ADVANCED_NETWORK_DETAILS).click()
            driver.find_element(*BTN_ROW_PROXY_NETWORK_DETAILS).click()
            driver.find_elements(*BTN_ROW_PROXY_MODES_NETWORK_DETAILS)[1].click()
            elem = driver.find_element(*INPUT_PROXY_HOSTNAME)
            elem.clear()
            elem.send_keys(contains_ip())
            elem = driver.find_element(*INPUT_PROXY_PORT)
            elem.clear()
            elem.send_keys('8080')
        else:
            driver.find_element(*BTN_ROW_PROXY_NETWORK_DETAILS).click()
            driver.find_elements(*BTN_ROW_PROXY_MODES_NETWORK_DETAILS)[0].click()
    except NoSuchElementException:
        print('proxy mode has already been set')
    driver.find_element(*BTN_SAVE_MODIFY).click()
    for _ in range(4):
        sleep(1)
        driver.back()

