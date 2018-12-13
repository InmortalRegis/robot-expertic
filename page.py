from element import BasePageElement
from locators import LoginPageLocators
#from locators import MainPageLocators


class BasePage(object):
    """ Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class UsernameElement(BasePageElement):
    """ Esta clase obtiene el usuario del localizador especificado. """

    # Localizador para el input de usuario donde se ingresa el nombre de usuario
    locator = 'username'


class PasswordElement(BasePageElement):
    """ Esta clase obtiene la contraseña del localizador especifico. """

    # Localizador para el input de la contraseña donde se ingresa la contraseña del usuario
    locator = 'password'


class LoginPage(BasePage):
    """Login page. """

    username_element = UsernameElement()
    password_element = PasswordElement()

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()
