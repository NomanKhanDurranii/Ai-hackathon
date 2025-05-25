import pandas as pd
from bs4 import BeautifulSoup
import requests

# Get the webpage
url = "https://sarmaaya.pk/mutual-funds/"
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')

# Find the table
data_table = soup.find("table", {"id": "funds-table"})

# Extract headers
thead = data_table.find("thead")
header_cells = thead.find_all("th")
headers = ["S.No"] + [cell.text.strip() for cell in header_cells]

# Extract rows
tbody = data_table.find("tbody")
rows = tbody.find_all("tr")

# Extract data
data = []
for i, row in enumerate(rows, start=1):
    cells = row.find_all("td")
    cell_values = [cell.text.strip() for cell in cells]
    data.append([i] + cell_values)

    import pandas as pd
from bs4 import BeautifulSoup
import requests

# Get the webpage
url = "https://sarmaaya.pk/mutual-funds/"
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')

# Find the table
data_table = soup.find("table", {"id": "funds-table"})

# Extract headers
thead = data_table.find("thead")
header_cells = thead.find_all("th")
headers = ["S.No"] + [cell.text.strip() for cell in header_cells]

# Extract rows
tbody = data_table.find("tbody")
rows = tbody.find_all("tr")

# Extract data
data = []
for i, row in enumerate(rows, start=1):
    cells = row.find_all("td")
    cell_values = [cell.text.strip() for cell in cells]
    data.append([i] + cell_values)

# Create DataFrame - import to csv
df = pd.DataFrame(data, columns=headers)

# Export to CSV
df.to_csv("mutual_funds.csv", index=False, encoding="utf-8")

print("Data successfully saved to 'mutual_funds.csv'")