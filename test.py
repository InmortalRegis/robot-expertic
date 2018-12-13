import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import page


class TestCase(unittest.TestCase):
    """ Clase para probar objectos de página.

    Arguments:
        unittest {library} -- Python unittesting framework
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://tic.uis.edu.co/ava25/")

    def test_log_in_experticava25(self):
        """
         Test login experticava25. Ingresa a la plataforma con las credenciales especificas
            :param self:
        """

        login_page = page.LoginPage(self.driver)
        login_page.username_element = 'exper-tic'
        login_page.password_element = '123581mapa'
        login_page.click_login_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(exit=False)
