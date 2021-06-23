from appium.webdriver.common.mobileby import MobileBy

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