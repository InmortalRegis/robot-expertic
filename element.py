from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")


class UsernameElement(BasePageElement):
    """ Esta clase obtiene el usuario del localizador especificado. """

    # Localizador para el input de usuario donde se ingresa el nombre de usuario
    locator = 'username'


class PasswordElement(BasePageElement):
    """ Esta clase obtiene la contraseña del localizador especifico. """

    # Localizador para el input de la contraseña donde se ingresa la contraseña del usuario
    locator = 'password'


class BaseSelectElement(BasePageElement):

    def __set__(self, obj, value):
        """Sets the select value to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_id(self.locator))
        Select(driver.find_element_by_id(
            self.locator)).select_by_value(value)


class MenuReportElement(BaseSelectElement):
    locator = 'menureport'


class MenuTimeElement(BaseSelectElement):
    locator = 'menutime'


