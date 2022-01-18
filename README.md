# MackenzieBot
## Welcome!!

MackenzieBot was initally built as a way for us to keep track of item prices from a local auction house. We found that these auctions, which often deal with thousands of items, took too much of our time to parse through and keep up to date with item prices. As such, we created a program in Python to fulfill our goals.

This program, written in the Python language, uses Tkinter for its GUI, and htmpParser and BeautifulSoup to aquire and process the data.

## Launcher.py
    - Houses majority of the code needed to run the Tkinter GUI

## InitialBookParse.py
    - Uses BeautifulSoup to parse an html file of saved bookmarks. 
    - I.E. a bulk download from Google chrome.
    - This intial set-up, as we could not directly communitcate with chrome. 
    - As such, a small amount of human compulation is required.

## DataParse
    - Stores a trimmed item name and full url in an easy to parse and read format. A csv

Initial brainstorming and thought processes
![image](https://user-images.githubusercontent.com/43597960/150020087-a7e4f679-3e41-4598-93b9-b9769dc08c3e.png)

