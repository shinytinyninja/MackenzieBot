from bs4 import BeautifulSoup
from os import listdir
from os import path

class initialBookParse:
    soup = BeautifulSoup()
    input_file = ""

    def __init__(self, input):
        self.input_file = input

    def get_list(self):
        if not self.input_file[-5:] == ".html":
            self.input_file = self.input_file + ".html"

        with open(str(self.input_file)) as fp:
            self.soup = BeautifulSoup(fp, features="html.parser")

        wanted_tags = {}
        for item in self.soup.find_all('a'):
            link = str(item['href'])
            title = str(item.contents)

            if "lot" in link and "McKenzie" in title:
                title = title.replace('"', '')
                title = title.replace("'", '')
                title = title[1:-36]
                wanted_tags[title] = link
        return (wanted_tags)

    def search_for(self):
        html_files = []
        files = [f for f in listdir('.') if path.isfile(f)]
        for f in files:
            if f[-5:] == ".html":
                html_files.append(f)
        return (html_files)

def main(): 
    initialBookParse(input("Enter a fileName"))

if __name__ == '__main__':
    main()