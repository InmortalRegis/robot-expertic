from element import *
from locators import LoginPageLocators, StatisticsPageLocators, ExportXlsPageLocators, ReportPageLocators, \
    HistoryScorePageLocators
from selenium.webdriver.support.ui import Select


# from locators import MainPageLocators


class BasePage(object):
    """ Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """Login page. """

    username_element = UsernameElement()
    password_element = PasswordElement()

    def click_posgrado_button(self):
        element = self.driver.find_element(*LoginPageLocators.POSGRADO_BUTTON)
        element.click()

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()

    def click_login_button_ava25(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON_AVA25)
        element.click()


class StatisticsPage(BasePage):
    """Pagina de estadísticas curso. """

    menu_report_element = MenuReportElement()
    menu_time_element = MenuTimeElement()

    def select_time_report(self, value):
        element = self.driver.find_element(
            *StatisticsPageLocators.TIME_SELECT)
        element = Select(element)
        element.select_by_value(value)

    def click_vista_button(self):
        element = self.driver.find_element(
            *StatisticsPageLocators.VISTA_BUTTON)
        element.click()


class ReportPage(BasePage):

    def click_enviar_button(self):
        element = self.driver.find_element(
            *ReportPageLocators.SEND_BUTTON)

        element.click()


class ExportXlsPage(ReportPage):
    """Pagina de exportar califaciones a excel"""

    def click_download_button(self):
        element = self.driver.find_element(
            *ExportXlsPageLocators.DOWNLOAD_BUTTON)
        element.click()


class HistoryScorePage(ReportPage):

    def click_download_button(self):
        element = self.driver.find_element(*HistoryScorePageLocators.DOWNLOAD_BUTTON)
        element.click()
