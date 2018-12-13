from oauth2client.service_account import ServiceAccountCredentials
from config import *
import pprint
import gspread


class SpreadSheet():

    client = gspread.authorize(creds)

    def __init__(self, sheet, worksheet, values_list):
        self.sheet = self.client.open(sheet)
        self.worksheet = self.sheet.worksheet(worksheet)
        self.values_list = self.worksheet.range(values_list)

    def get_link_list(self):
        link_list = []

        for cell in self.values_list:
            link_list.append(cell.value)

        return link_list

    def print_list(self, link_list):
        pp = pprint.PrettyPrinter()

        for link in link_list:
            pp.pprint(link)


if __name__ == "__main__":
    sh = SpreadSheet('Creación de cursos 2018-1',
                     'Cursos Bucaramanga', 'BE3:BE5')
    link_list = sh.get_link_list()
    sh.print_list(link_list)
