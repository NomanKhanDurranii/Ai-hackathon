import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome without manual path
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Remove this line if you want to see the browser window
options.add_argument("--window-size=1920,1080")

# Start Chrome browser (auto finds driver if installed correctly via pip)
driver = webdriver.Chrome(options=options)

# Open target page
url = "https://www.tradingview.com/markets/stocks-usa/market-movers-all-stocks/"
driver.get(url)

# Wait for table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-Ngq2xrcG')]"))
)

# Output CSV file
csv_filename = "tradingview.csv"
headers = ["Symbol", "Security Name", "Price", "Change %", "Volume", "Relative Volume", "Market Cap", "P/E Ratio", "EPS Diluted", "EPS Growth", "Dividend Yield", "Sector", "Analyst Rating"]

# Ensure headers written once
file_exists = os.path.exists(csv_filename)
with open(csv_filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(headers)

    stock_data = []
    while True:
        rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'table-Ngq2xrcG')]//tbody/tr")
        if not rows:
            print(" No rows found, page structure may have changed.")
            break

        for row in rows[len(stock_data):]:
            columns = row.find_elements(By.TAG_NAME, "td")
            row_content = [col.text.strip().replace("−", "-") for col in columns]  # optional replacement to avoid unicode error
            stock_data.append(row_content)
            writer.writerow(row_content)

        print(f" Total stocks collected: {len(stock_data)}")

        # Try to click 'Load More' if available
        try:
            load_more = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Load More')]"))
            )
            print(" Loading more data...")
            load_more.click()
            time.sleep(5)
        except:
            print(" All data loaded.")
            break

driver.quit()
print(f" Data saved to: {csv_filename}")
