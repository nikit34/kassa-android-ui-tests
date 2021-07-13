from time import sleep
from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException, StaleElementReferenceException
from appium.webdriver.common.mobileby import MobileBy
import os
from subprocess import Popen

from templates.action import Action
from utils.emulator_act import reboot_emulator, shut_down_emulator, run_emulator


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
    sleep(1)
    elems = driver.find_elements(*locator)
    for elem in elems:
        if elem.text == text:
            elem.click()
            break


def _click(driver, *locator, num=None):
    sleep(2)
    if num is None:
        driver.find_element(*locator).click()
    else:
        driver.find_elements(*locator)[num].click()


def _input(driver, *locator, text):
    elem = driver.find_element(*locator)
    elem.clear()
    elem.send_keys(text)


def switch_proxy_mode(driver, to_state=True):
    try:
        act = Action(driver)
        act.swipe(50, 0, 50, 80)
        act.swipe(50, 15, 50, 50)
        _click(driver, *BTN_SETTINGS)
        _click_by_text(driver, *BTN_ROW_TITLE_SETTINGS, text='Network & internet')
        _click_by_text(driver, *BTN_ROW_TITLE_SETTINGS, text='Wi‑Fi')
        _click_by_text(driver, *BTN_ROW_TITLE_SETTINGS, text='AndroidWifi')
        _click(driver, *BTN_MODIFY_NETWORK)
    except (NoSuchElementException, InvalidElementStateException):
        reboot_emulator()
        switch_proxy_mode(driver, to_state)
    try:
        if to_state:
            _click(driver, *BTN_ROW_ADVANCED_NETWORK_DETAILS)
            _click(driver, *BTN_ROW_PROXY_NETWORK_DETAILS)
            _click(driver, *BTN_ROW_PROXY_MODES_NETWORK_DETAILS, num=1)
            _input(driver, *INPUT_PROXY_HOSTNAME, text=contains_ip())
            _input(driver, *INPUT_PROXY_PORT, text='8080')
        else:
            _click(driver, *BTN_ROW_PROXY_NETWORK_DETAILS)
            _click(driver, *BTN_ROW_PROXY_MODES_NETWORK_DETAILS, num=0)
    except NoSuchElementException:
        print('proxy mode has already been set')
    _click(driver, *BTN_SAVE_MODIFY)
    for _ in range(4):
        sleep(1)
        driver.back()


def switch_proxy_mode_reboot(to_state=True):
    shut_down_emulator()

    if to_state:
        Popen(f'/home/npermyakov/Android/Sdk/emulator/emulator -avd Pixel_3a_XL_API_30 -no-snapshot-load -gpu guest -memory 3072 -http-proxy http://{contains_ip()}:8080', shell=True)
        Popen(f'/Users/n.permyakov/Library/Android/sdk/emulator/emulator -avd Pixel_3a_XL_API_30 -no-snapshot-load -gpu guest -memory 3072 -http-proxy http://{contains_ip()}:8080', shell=True)
    else:
        run_emulator()



