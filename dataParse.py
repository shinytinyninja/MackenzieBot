import requests
from bs4 import BeautifulSoup
import csv
import os
import re

class DataParse:
    def __init__(self, dict_lots=None):
        self.dict_items = dict_lots if dict_lots else {}
        # Added a User-Agent to prevent the auction site from blocking the script
        self.req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    def scrape_item(self, url):
        """Helper function to scrape a single URL."""
        try:
            html_content = requests.get(url, headers=self.req_headers).text
            soup = BeautifulSoup(html_content, features="html.parser")
            
            # Find elements, defaulting to "0" or "Unknown" if the auction ended or page changed
            bid_elem = soup.find("span", {'class': 'lot-high-bid'})
            time_elem = soup.find("span", {'class': 'lot-time-left'})
            
            current_bid = bid_elem.get_text(' ', strip=True) if bid_elem else "0"
            time_left = time_elem.get_text(' ', strip=True) if time_elem else "Unknown"
            
            return current_bid, time_left
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return "0", "Unknown"

    def create_csv(self, name_of_csv):
        """Creates the initial CSV with a blank 'Max Price' column for you to fill."""
        filename = f"{name_of_csv}.csv"
        
        # 'newline=""' prevents blank rows in Windows
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # Wrote a proper header row, including the new Max Price column
            writer.writerow(['Item Name', 'URL', 'Current Bid', 'Time Left', 'Max Desired Price'])

            for name, url in self.dict_items.items():
                print(f"Scraping initial data for: {name}")
                current_bid, time_left = self.scrape_item(url)
                writer.writerow([name, url, current_bid, time_left, ''])
                
        print(f"\n✅ Created {filename}. Open it, add your limits under 'Max Price', save, and run check_disparity().\n")

    def parse_price(self, price_str):
        """Converts strings like '$15.50 CAD' into a float 15.50 for math."""
        match = re.search(r'[\d,]+\.?\d*', str(price_str))
        if match:
            return float(match.group().replace(',', ''))
        return 0.0

    def check_disparity(self, name_of_csv):
        """Reads the CSV, scrapes fresh prices, and compares them against your Max Price."""
        filename = f"{name_of_csv}.csv"
        if not os.path.exists(filename):
            print(f"File {filename} not found.")
            return

        within_budget = []
        beyond_limit = []

        with open(filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='|')
            
            for row in reader:
                name = row.get('Item Name')
                url = row.get('URL')
                max_price_str = row.get('Max Desired Price', '').strip()
                
                if not max_price_str:
                    print(f"Skipping '{name}': No Max Price set in CSV.")
                    continue
                    
                max_desired_price = self.parse_price(max_price_str)
                
                print(f"Checking current price for: {name}")
                current_bid_str, time_left = self.scrape_item(url)
                current_bid = self.parse_price(current_bid_str)
                
                disparity = max_desired_price - current_bid
                
                if disparity < 0:
                    beyond_limit.append({
                        'name': name, 
                        'current_bid': current_bid, 
                        'max_desired_price': max_desired_price,
                        'exceeded_by': abs(disparity)
                    })
                else:
                    within_budget.append({
                        'name': name,
                        'current_bid': current_bid,
                        'max_desired_price': max_desired_price,
                        'disparity': disparity,
                        'time_left': time_left
                    })

        print("\n--- RESULTS ---")
        if beyond_limit:
            print("\n🚨 ITEMS BEYOND LIMIT 🚨")
            for item in beyond_limit:
                print(f"- {item['name']}: Current Bid ${item['current_bid']:.2f} (Your max: ${item['max_price']:.2f} | Exceeded by ${item['exceeded_by']:.2f})")
        
        if within_budget:
            print("\n✅ ITEMS WITHIN BUDGET (Sorted by biggest disparity) ✅")
            # Sort so the items with the biggest gap between current price and max price are at the top
            within_budget.sort(key=lambda x: x['disparity'], reverse=True)
            for item in within_budget:
                print(f"- {item['name']}: Current Bid ${item['current_bid']:.2f} (Max: ${item['max_price']:.2f} | Room to bid: ${item['disparity']:.2f}) - {item['time_left']} left")


def main():
    test_dict = {
        "mug": "https://mckenzieauction.hibid.com/lot/63737535/strata-black-12-piece-melamine-dinnerware-set/?sortOrder=4&cpage=14&ipp=100&q=&ref=catalog", 
        "potato": "https://mckenzieauction.hibid.com/lot/63737293/origin-cutting-board-13-75-/?sortOrder=4&cpage=14&ipp=100&q=&ref=catalog"
    }
    
    data = DataParse(test_dict)
    
    # Step 1: Run this once to generate the file. 
    data.create_csv("testingFile")
    
    # Step 2: Open "testingFile.csv" in Excel/Numbers, type "20" and "5" in the Max Price column, and save.
    
    # Step 3: Run this to check your limits.
    # data.check_disparity("testingFile")

if __name__ == "__main__":
    main()