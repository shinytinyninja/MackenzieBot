# MackenzieBot
## Welcome!!

MackenzieBot was initially built as a way for us to keep track of item prices from a local auction house. We found that these auctions, which often deal with thousands of items, took too much of our time to parse through and keep up to date with item prices. As such, we created a program in Python to fulfill our goals.

This program, written in the Python language, uses Tkinter for its GUI, and HTMLParser and BeautifulSoup to acquire and process the data.

---

## Project Structure & Files

- **`Launcher.py`**
  - Houses the majority of the code needed to run the Tkinter GUI.
- **`InitialBookParse.py`**
  - Uses BeautifulSoup to parse an HTML file of saved bookmarks (e.g., a bulk download from Google Chrome).
  - This initial set-up bridges the gap since we could not directly communicate with Chrome.
  - As such, a small amount of human computation/input is required.
- **`DataParse`**
  - Stores trimmed item names and full URLs in an easy-to-parse and read format (CSV).
  - Handles real-time scraping of current bids, time left, and disparity checking against your set maximum prices.

---

## Initial Brainstorming and Thought Processes

![image](https://user-images.githubusercontent.com/43597960/150020087-a7e4f679-3e41-4598-93b9-b9769dc08c3e.png)