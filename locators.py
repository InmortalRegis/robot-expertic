from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    "Todos los localizadores de la página Login van aquí. "

    LOGIN_BUTTON = (By.ID, 'send')


class StatisticsPageLocators(object):
    """ Todos los localizadores de la página Statistics van aquí. """

    TYPE_REPORT_SELECT = (By.ID, 'menureport')
    TIME_SELECT = (By.ID, 'menutime')
    VISTA_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
