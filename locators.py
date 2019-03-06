from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    "Todos los localizadores de la página Login van aquí. "

    LOGIN_BUTTON = (By.ID, 'send')
    LOGIN_BUTTON_AVA25 = (By.ID, 'loginbtn')
    POSGRADO_BUTTON = (By.ID, 'posgrado-head')


class StatisticsPageLocators(object):
    """ Todos los localizadores de la página Statistics van aquí. """

    TYPE_REPORT_SELECT = (By.ID, 'menureport')
    TIME_SELECT = (By.ID, 'menutime')
    VISTA_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')


class ExportXlsPageLocators(object):
    """ Todos los localizadores de la página Statistics van aquí. """

    DESCARGAR_BUTTON = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Exportar'])[2]/following::input[1]")
    ENVIAR_BUTTON = (By.ID, 'id_submitbutton')
    
