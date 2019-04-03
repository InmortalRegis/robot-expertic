from bs4 import BeautifulSoup
import csv

class HistoryPageSoup(object):

    def __init__(self, driver):
        self.driver = driver

    def get_csv_table(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={"class": "gradereport_history"})
        headers = [header.text for header in table.find_all('th')]

        rows = []
        for row in table.find_all('tr'):
            rows.append([val.text for val in row.find_all('td')])
            pass

        with open('output_file.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(row for row in rows if row)
