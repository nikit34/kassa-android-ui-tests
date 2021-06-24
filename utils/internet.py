from appium.webdriver.common.mobileby import MobileBy
import os

from templates.action import Action


AIRPLANE_MODE = (MobileBy.ACCESSIBILITY_ID, 'Airplane mode')


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
    supposed_ip = ['10.60.20.152', '10.60.20.108']
    output = os.popen('ifconfig').read()
    for s_ip in supposed_ip:
        if s_ip in output:
            return s_ip
    else:
        raise ValueError('ip has been changed')