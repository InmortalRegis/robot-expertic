import unittest
from selenium import webdriver
import page
from spreadsheet import SpreadSheet
import time

class TestCase(unittest.TestCase):
    """ Clase para probar objectos de página.

    Arguments:
        unittest {library} -- Python unittesting framework
    """
    link_list = SpreadSheet(sheet='Creación de cursos 2018-1',
                            worksheet='Cursos Bucaramanga', values_list='BE3:BE5').get_link_list()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://tic.uis.edu.co/ava25/")

    def test_log_in_experticava25(self):
        """
         Test login experticava25. Ingresa a la plataforma con las credenciales especificas
            :param self:
        """
        # Log in
        login_page = page.LoginPage(self.driver)
        login_page.username_element = 'exper-tic'
        login_page.password_element = '123581mapa'
        login_page.click_login_button()

       
        # Select report
        self.driver.get(self.link_list[0])
        statistics_page = page.StatisticsPage(self.driver)
        statistics_page.menu_report_element = '55'
        statistics_page.menu_time_element = '16'
        statistics_page.click_vista_button()
        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(exit=False)
    
