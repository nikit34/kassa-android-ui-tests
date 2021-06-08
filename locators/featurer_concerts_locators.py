from selenium.webdriver.common.by import By


class ConcertsPageLocators:
    tab = (By.ID, 'ru.rambler.kassa.beta:id/tab')
    event_name = (By.ID, 'ru.rambler.kassa.beta:id/eventName')
    session_day_of_month = (By.ID, 'ru.rambler.kassa.beta:id/sessionDayOfMonth')
    session_min_price = (By.ID, 'ru.rambler.kassa.beta:id/sessionMinPrice')
    session_day_of_week_hour_minutes = (By.ID, 'ru.rambler.kassa.beta:id/sessionDayOfWeekHourMinutes')
    title = (By.ID, 'ru.rambler.kassa.beta:id/title')
    event_img = (By.ID, 'ru.rambler.kanamessa.beta:id/eventImg')
    carousel_rv = (By.ID, 'ru.rambler.kassa.beta:id/carouselRv')
    single_session_view = (By.ID, 'ru.rambler.kassa.beta:id/singleSessionView')