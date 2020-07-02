from bs4 import BeautifulSoup
import requests
import csv

class dataParse:
    DictOfItems = {}

    def __init__(self, dict_lots):
        self.dict_items = dict_lots

    def create_csv(self, name_of_csv):
        name_of_csv += '.csv'
        with open(name_of_csv, 'w') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
            file_writer.writerow([len(self.DictOfItems), 'link'])

            for key in self.dict_items:
                file_writer.writerow([key, self.dict_items[key]])
        
        self.update_values(name_of_csv)
        
    def update_values(self, name_of_csv):
        with open(str(name_of_csv)) as csv_file:       
            file_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
            file_writer.writerow([len(self.dict_items), 'link'])

        for key in self.dict_items:
            url = self.dict_items[key]
            html_content = requests.get(url).text
            soup = BeautifulSoup(html_content, features="html.parser")
            current_bid = soup.find("span", {'class':'lot-high-bid'}).get_text(' ', strip = True)
            time_left = soup.find("span", {'class':'lot-time-left'}).get_text(' ', strip = True)
            


def main():
    test_dict = {"mug":"https://mckenzieauction.hibid.com/lot/63737535/strata-black-12-piece-melamine-dinnerware-set/?sortOrder=4&cpage=14&ipp=100&q=&ref=catalog", "potato":"https://mckenzieauction.hibid.com/lot/63737293/origin-cutting-board-13-75-/?sortOrder=4&cpage=14&ipp=100&q=&ref=catalog"}
    data = dataParse(test_dict)
    data.create_csv("testingFile")

if __name__ == "__main__":
    main()

