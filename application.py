from selenium import webdriver
import page
from spreadsheet import SpreadSheet
import time


class Main():
    """ Clase para crear objectos de página.
    """

    # Lista de enlaces seleccionados de un value_list espeficico de una SpreadSheet
    link_list = SpreadSheet(sheet='Creación de cursos 2018-2',
                            worksheet='Cursos 2018-2', values_list='BM180:BM181').get_link_list()

    def __init__(self):
        """Constructor de la clase Main inicializamos el driver en la pagina de inicio
        """

        self.driver = webdriver.Firefox()
        self.driver.get("http://tic.uis.edu.co/")

    def log_in_experticava(self):
        """
        login experticava25. Ingresa a la plataforma con las credenciales especificas
        """
        # Log in
        login_page = page.LoginPage(self.driver)
        login_page.click_posgrado_button()
        login_page.username_element = 'exper-tic'
        login_page.password_element = 'exper-tic'

        login_page.click_login_button()

    def get_history_score(self, url):
        self.driver.get(url)
        history_score_page = page.HistoryScorePage(self.driver)
        history_score_page.click_enviar_button()
        time.sleep(5)
        history_score_page.click_download_button()

        time.sleep(5)

    def select_report(self, url):
        """ Selecciona reporte por cursos en este caso tipo de reporte estudiantes y
        período a mostrar de 6 meses

        Arguments:
            url {string} -- [url para cada página reporte]
        """

        # Select report
        self.driver.get(url)
        statistics_page = page.StatisticsPage(self.driver)
        # Menu report 53 Profesor, 55 Estudiante
        statistics_page.menu_report_element = '55'
        # Page menu 16: 6 months
        statistics_page.menu_time_element = '16'
        statistics_page.click_vista_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    app = Main()
    app.log_in_experticava()
    for url in app.link_list:
        app.get_history_score(url)
        pass
    app.tearDown()
