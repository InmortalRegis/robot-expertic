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
                            worksheet='Cursos Bucaramanga', values_list='AG3:AG188').get_link_list()

    def setUp(self):
        #chrome_options = webdriver.ChromeOptions()
        
        #prefs = {'download.default_directory' : 'G:\\Mi unidad\\1_ExperTIC\\03_Ejecucion\\2019\\02_ProcesosPrimarios\\07_TrabajoconAuxiliares\\Descarga de Notas\\2018-2'}
        #chrome_options.add_experimental_option('prefs', prefs)
        #self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
        self.driver = webdriver.Firefox()
        self.driver.get("http://tic.uis.edu.co/ava25")

    def test_log_in_experticava25(self):
        """ 
         Test login experticava25. Ingresa a la plataforma con las credenciales especificas
            :param self:
        """
        # Log in
        login_page = page.LoginPage(self.driver)
        #login_page.click_posgrado_button()
        login_page.username_element = 'exper-tic'
        #login_page.password_element = 'exper-tic'
        login_page.password_element = '123581mapa'
        login_page.click_login_button_ava25()
        # Select report
        for link in self.link_list:
            print(link)
            if(link==''):
                pass
            else:
                self.driver.get(link)
                export_xls_page = page.ExportXlsPage(self.driver)   
                export_xls_page.click_enviar_button()
                export_xls_page.click_descargar_button()
                time.sleep(10)
                pass
    

        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(exit=False)
    
