from bs4 import BeautifulSoup
import os

class initialBookParse:
    def __init__(self, inputFileName):
        wantedTags = {}
        try:
            with open(str(inputFileName)) as fp:
                soup = BeautifulSoup(fp, "html.parser")
        except OSError as e:
            print(e.filename)
            
        for item in soup.find_all('a'):
            link = str(item['href'])
            title = str(item.contents)

            if "lot" in link and "McKenzie" in title:
                title = title.replace('"', '')
                title = title.replace("'", '')
                title = title[1:-36]
                wantedTags[title] = link
        return (wantedTags)
        
    def searchForFile(self):
        htmlFiles = []
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print(f[-5:])
            if f[-5:] == ".html":
                htmlFiles.append(f)
        return (htmlFiles)

def main(): 
    self.initialBookParse(input("Enter a fileName"))

if __name__ == '__main__':
    main()