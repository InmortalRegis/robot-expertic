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
    link_list = SpreadSheet(sheet='Creación de cursos 2018-2',
                            worksheet='Cursos 2018-2', values_list='AU3:AU276').get_link_list()

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        
        prefs = {'download.default_directory' : 'G:\\Mi unidad\\1_ExperTIC\\03_Ejecucion\\2019\\02_ProcesosPrimarios\\07_TrabajoconAuxiliares\\Descarga de Notas\\2018-2'}
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
        self.driver.get("http://tic.uis.edu.co/")

    def test_log_in_experticava25(self):
        """
         Test login experticava25. Ingresa a la plataforma con las credenciales especificas
            :param self:
        """
        # Log in
        login_page = page.LoginPage(self.driver)
        self.driver.find_element_by_id("posgrado-head").click()
        login_page.username_element = 'exper-tic'
        login_page.password_element = 'exper-tic'
        login_page.click_login_button()
        # Select report
        for link in self.link_list:
            print(link)
            if(link==''):
                pass
            else:
                self.driver.get(link)
                self.driver.find_element_by_id("id_submitbutton").click()
                time.sleep(5)
                pass
    

        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(exit=False)
    
