import unittest
from selenium import webdriver
from page import LoginPage
from spreadsheet import SpreadSheet
import time


class TestCase(unittest.TestCase):
    """ Clase para probar objectos de página.

    Arguments:
        unittest {library} -- Python unittesting framework
    """


    def setUp(self):
        # chrome_options = webdriver.ChromeOptions()

        # prefs = {'download.default_directory' : 'G:\\Mi
        # unidad\\1_ExperTIC\\03_Ejecucion\\2019\\02_ProcesosPrimarios\\07_TrabajoconAuxiliares\\Descarga de
        # Notas\\2018-2'} chrome_options.add_experimental_option('prefs', prefs) self.driver = webdriver.Chrome(
        # executable_path="chromedriver.exe", chrome_options=chrome_options)
        self.driver = webdriver.Firefox()
        self.driver.get("http://tic.uis.edu.co/")

    def test_log_in_experticava25(self):
        """ 
         Test login experticava25. Ingresa a la plataforma con las credenciales especificas
            :param self:
        """
        # Log in
        login_page = LoginPage(self.driver)
        login_page.click_posgrado_button()
        login_page.username_element = 'exper-tic'
        # login_page.password_element = 'exper-tic'
        login_page.password_element = 'exper-tic'

        login_page.click_login_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(exit=False)
