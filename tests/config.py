APPIUM_HOST = 'http://10.60.21.50:4723/wd/hub'  # host
APPIUM_LOCAL = 'http://0.0.0.0:4723/wd/hub'  # local

DESIRED_CAPS_NO_CACHE_HOST = {
  'platformName': 'Android',
  'appPackage': 'ru.rambler.kassa.dev',
  'appActivity': 'ru.rambler.kassa.presentation.LaunchActivity',
  'appWaitActivity': 'ru.rambler.kassa.presentation.LaunchActivity',
  'noReset': False,
  'wdaLocalPort': 8100,
  'wdaBaseUrl': 'http://localhost'
}

DESIRED_CAPS_HOST = {
  'platformName': 'Android',
  'appPackage': 'ru.rambler.kassa.dev',
  'appActivity': 'ru.rambler.kassa.presentation.LaunchActivity',
  'noReset': True,
  'wdaLocalPort': 8100,
  'wdaBaseUrl': 'http://localhost'
}

DESIRED_CAPS_NO_CACHE_LOCAL = {
  'platformName': 'Android',
  'appPackage': 'ru.rambler.kassa.dev',
  'appActivity': 'ru.rambler.kassa.presentation.LaunchActivity',
  'appWaitActivity': 'ru.rambler.kassa.presentation.LaunchActivity',
  'noReset': False,

}

DESIRED_CAPS_LOCAL = {
  'platformName': 'Android',
  'appPackage': 'ru.rambler.kassa.dev',
  'appActivity': 'ru.rambler.kassa.presentation.LaunchActivity',
  'noReset': True,
}

