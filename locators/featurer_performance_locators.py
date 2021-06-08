from selenium.webdriver.common.by import By


class PerformancePageLocators:
    events = (By.ID, 'ru.rambler.kassa.beta:id/tab')
    title = (By.ID, 'ru.rambler.kassa.beta:id/title')
    event_name = (By.ID, 'ru.rambler.kassa.beta:id/eventName')
    session_day_of_month = (By.ID, 'ru.rambler.kassa.beta:id/sessionDayOfMonth')
    session_day_of_week_hour_minutes = (By.ID, 'ru.rambler.kassa.beta:id/sessionDayOfWeekHourMinutes')
    session_min_price = (By.ID, 'ru.rambler.kassa.beta:id/sessionMinPrice')
    compilation_img = (By.ID, 'ru.rambler.kassa.beta:id/compilationImg')
    event_title = (By.ID, 'ru.rambler.kassa.beta:id/eventTitle')
    event_genre = (By.ID, 'ru.rambler.kassa.beta:id/eventGenre')
    carousel_rv = (By.ID, 'ru.rambler.kassa.beta:id/carouselRv')
    single_session_view = (By.ID, 'ru.rambler.kassa.beta:id/singleSessionView')