from bs4 import BeautifulSoup

def initalParse(inputFileName):
    with open(str(inputFileName)) as fp:
        soup = BeautifulSoup(fp, "html.parser")
        wantedTags = {}
        for item in soup.find_all('a'):
            link = str(item['href'])
            title = str(item.contents)

            if "lot" in link and "McKenzie" in title:
                title = title.replace('"', '')
                title = title.replace("'", '')
                title = title[1:-36]
                wantedTags[title] = link
                
    return (wantedTags)